from typing import Union

from rich import print
from rich.tree import Tree

from .api import Api
from .coreutils import data_broker, log

ITALIC = "[italic]"
BOLD_BRIGHT_BLUE = "bold bright_blue"
BLUE = "[blue]"
RESET = "[/]"
BOLD = "[bold]"
DIM = "dim"


class Masonry:
    def __init__(self):
        self.api = Api(base_api_endpoint="https://api.github.com")

    def add_branch(
        self,
        target_tree: Tree,
        branch_title: str,
        branch_data: Union[dict, list],
        additional_text: str = None,
        additional_data: [(str, Union[dict, list])] = None,
    ):
        """
        Populates a branch with the given data and adds it to the specified tree.

        :param target_tree: The existing Tree to add the branch to.
        :param branch_title: The title for the new branch.
        :param branch_data: The data for the new branch in dictionary or list format.
        :param additional_text: Additional text (e.g., Bio in user profile, Description in repo/organization).
        :param additional_data: A list of tuples containing additional data, such as License (for repositories),
               Topics (for repositories), Files (for gists), etc.
        :returns: A populated branch.
        """
        branch = target_tree.add(f"{BOLD}{branch_title}{RESET}", guide_style="blue")
        if type(branch_data) in [dict, list]:
            if isinstance(branch_data, dict):
                for key, value in branch_data.items():
                    branch.add(f"{key.capitalize()}: {value}", style=DIM)
                if additional_data:
                    for title, data in additional_data:
                        if data:
                            if isinstance(data, dict):
                                self.add_branch(
                                    target_tree=branch,
                                    branch_title=title,
                                    branch_data=data,
                                )
                            else:
                                self.add_branch(
                                    target_tree=branch,
                                    branch_title=title,
                                    branch_data=data,
                                )
            else:
                for count, item in enumerate(branch_data, start=1):
                    branch.add(f"{count}. {item}")

            if additional_text:
                branch.add(additional_text, style="italic")

            return target_tree

    def create_tree(
        self,
        tree_title: str,
        tree_data: dict = None,
        additional_text: str = None,
        additional_data: [(str, Union[dict, list])] = None,
    ) -> Tree:
        """
        Creates a tree structure and populates it with the given data.

        :param tree_title: Title of the tree.
        :param tree_data: Data to populate the tree with.
        :param additional_text: Additional text (e.g., Bio in user profile, Description in repo/organization).
        :param additional_data: A list of tuples containing additional data, such as License (for repositories),
               Topics (for repositories), Files (for gists), etc.
        :returns: A populated tree structure if tree_data is not None, otherwise returns an empty tree.
        """
        if not tree_data:
            return Tree(tree_title, guide_style=BOLD_BRIGHT_BLUE)

        tree = Tree(f"{BOLD}{tree_title}{RESET}", guide_style=BOLD_BRIGHT_BLUE)
        for key, value in tree_data.items():
            tree.add(f"{key}: {value}", style=DIM)

        if additional_data:
            for title, data in additional_data:
                if data:
                    self.add_branch(
                        target_tree=tree,
                        branch_title=title,
                        branch_data=data,
                    )

        if additional_text:
            tree.add(additional_text, style="italic")

        return tree

    def repos_tree(
        self,
        repos_type: str,
        repos_limit: int,
        repos_source: str,
        additional_repos_source: str = None,
    ):
        """
        Populates a tree with repository data and prints it.

        :param repos_type: Type of repositories to retrieve (e.g., "user_repos" or "org_repos").
        :param repos_limit: The maximum number of repositories to retrieve.
        :param repos_source: The source of the repositories data (e.g., username or organization name).
        :param additional_repos_source: An optional string representing an additional source
               for data retrieval (used with "repo_forks" type).
        """
        repos = self.api.get_repos(
            repos_type=repos_type,
            repos_limit=repos_limit,
            repos_source=repos_source,
            additional_repos_source=additional_repos_source,
        )
        if repos:
            repos_tree = self.create_tree(
                tree_title=f"Showing {repos_limit} {'Repository' if len(repos) < 2 else 'Repositories'} "
                f"from {repos_type}.",
            )
            for repo in repos:
                brokered_data = data_broker(
                    raw_data=repo, data_file="repo/profile.json"
                )
                self.add_branch(
                    target_tree=repos_tree,
                    branch_title=repo.get("full_name"),
                    branch_data=brokered_data,
                    additional_data=[
                        ("License", repo.get("license")),
                        ("Topics", repo.get("topics")),
                    ],
                )

            print(repos_tree)
        else:
            log.info(f"No {repos_type} found.")

    def users_tree(
        self,
        users_type: str,
        users_limit: int,
        users_source: str,
        additional_users_source: str = None,
    ):
        """
        Populates a tree with user data and prints it.

        :param users_type: Type of users to retrieve (e.g., "user_followers" or "repo_contributors").
        :param users_limit: The maximum number of users to retrieve.
        :param users_source: The source of the users data (e.g., username or repository name).
        :param additional_users_source: An optional string representing an additional source
               for data retrieval (used with "repo_contributors" or "repo_stargazers" type).
        """
        users = self.api.get_users(
            users_type=users_type,
            users_source=users_source,
            users_limit=users_limit,
            additional_users_source=additional_users_source,
        )
        if users:
            contributors_tree = self.create_tree(
                tree_title=f"Showing {users_limit} {users_type}",
            )
            for user in users:
                brokered_data = data_broker(
                    raw_data=user, data_file="user/summary.json"
                )
                self.add_branch(
                    target_tree=contributors_tree,
                    branch_title=user.get("login"),
                    branch_data=brokered_data,
                )
            print(contributors_tree)
        else:
            log.info(f"No {users_type} found.")

    def user_emails_tree(self, username: str):
        """
        Retrieve and display email addresses from the user's PushEvents.

        :param username: User to get emails from.
        """
        emails = self.api.get_user_emails(username=username)
        if emails:
            emails_tree = self.create_tree(
                tree_title=f"Showing {len(emails)} "
                f"{'Email' if len(emails) < 2 else 'Emails'} from {username}'s PushEvents.",
            )
            for count, email in enumerate(emails, start=1):
                emails_tree.add(f"{count}. {email}")

            print(emails_tree)
        else:
            log.warning("No emails found.")

    def user_follows(self, primary_user: str, secondary_user: str):
        """
        Check if the primary user follows the secondary user and log the result.

        :param primary_user: The username of the primary user.
        :param secondary_user: The username of the secondary user.
        """
        invalid_users = []

        for user in [primary_user, secondary_user]:
            user_status = self.api.get_data(
                endpoint=f"{self.api.user_data_endpoint}/{user}",
                get_status_codes=True,
            )
            if user_status == 404:
                invalid_users.append(user)

        if invalid_users:
            log.warning(
                f"Check unsuccessful: "
                # This is the part where I wish I used Python 3.12
                f"{f'User (@{user}) does not exist.' if len(invalid_users) < 2 else f'Users {invalid_users} do not exists.'}"
            )
            return

        # Perform the follower check only if both users' requests return a 200 status code.
        status_code = self.api.get_data(
            endpoint=f"{self.api.user_data_endpoint}/{primary_user}/following/{secondary_user}",
            get_status_codes=True,
        )

        if status_code == 204:
            log.info(f"{primary_user} [bold]follows[/] @{secondary_user}")
        elif status_code == 403:
            log.warning("API rate limit exceeded.")
        else:
            log.info(f"@{primary_user} [bold]does not follow[/] @{secondary_user}.")

    def user_gists_tree(self, username: str, limit: int):
        """
        Retrieve and display the user's gists.

        :param username: User to get gists from.
        :param limit: The maximum number of gists to display.
        """
        raw_gists = self.api.get_user_gists(username=username, limit=limit)
        if raw_gists:
            gists_tree = self.create_tree(
                tree_title=f"Showing {limit} "
                f"{'Gist' if len(raw_gists) < 2 else 'Gists'} from user (@{username})",
            )
            for gist in raw_gists:
                brokered_data = data_broker(raw_data=gist, data_file="other/gist.json")
                self.add_branch(
                    target_tree=gists_tree,
                    branch_title=gist.get("id"),
                    branch_data=brokered_data,
                    additional_text=gist.get("description"),
                )
            print(gists_tree)
        else:
            log.info(f"User (@{username}) does not have (public) gists.")

    def user_orgs_tree(self, username: str, limit: int):
        """
        Retrieve and display the organisations the user belongs to.

        :param username: User to get organisations from.
        :param limit: The maximum number of organisations to display.
        """
        raw_organisations = self.api.get_user_orgs(username=username, limit=limit)
        if raw_organisations:
            organisations_tree = self.create_tree(
                tree_title=f"Showing {limit} {'Organisation' if len(raw_organisations) < 2 else 'Organisations'} "
                f"from user (@{username})",
            )
            for organisation in raw_organisations:
                brokered_data = data_broker(
                    raw_data=organisation, data_file="user/org.json"
                )
                self.add_branch(
                    target_tree=organisations_tree,
                    branch_title=organisation.get("login"),
                    branch_data=brokered_data,
                    additional_text=organisation.get("description"),
                )
            print(organisations_tree)
        else:
            log.info(
                f"User (@{username}) does not own/belong to any (public) organisations."
            )

    def events_tree(self, events_type: str, events_source: str, events_limit: int):
        """
        Retrieve and displays events from the specified source.

        :param events_type: Type of events to visualise.
        :param events_source: The source of the events.
        :param events_limit: The maximum number of events to display.
        """
        raw_events = self.api.get_events(
            events_type=events_type,
            events_source=events_source,
            events_limit=events_limit,
        )
        if raw_events:
            events_tree = self.create_tree(
                tree_title=f"Showing {events_limit} {'Event' if len(raw_events) < 2 else 'Events'} "
                f"from @{events_source}"
            )
            for event in raw_events:
                self.add_branch(
                    target_tree=events_tree,
                    branch_title=event.get("id"),
                    branch_data={
                        "Actor": event.get("actor").get("login"),
                        "Type": event.get("type"),
                        "Repository": event.get("repo").get("name"),
                        "Created At": event.get("created_at"),
                    },
                    additional_text=f"[green]{event.get('payload')}[/]",
                )
            print(events_tree)
        else:
            log.info(f"@{events_source} does not have (public) events.")

    def is_org_member(self, organisation: str, username: str):
        user_status = self.api.get_data(
            endpoint=f"{self.api.user_data_endpoint}/{username}",
            get_status_codes=True,
        )
        org_status = self.api.get_data(
            endpoint=f"{self.api.orgs_data_endpoint}/{organisation}",
            get_status_codes=True,
        )
        if user_status == 404:
            log.warning(f"User (@{username}) does not exist.")
        if org_status == 404:
            log.warning(f"Organisation (@{organisation}) does not exist")

        membership_status = self.api.get_data(
            endpoint=f"{self.api.orgs_data_endpoint}/{organisation}/public_members/{username}"
        )
        if membership_status == 204:
            log.info(
                f"User (@{username}) [bold]is a public member[/] of the organisation (@{organisation})"
            )
        elif membership_status == 403:
            log.warning("API rate limit exceeded.")
        else:
            log.info(
                f"User (@{username}) [bold]is not a public member[/] of the organisation (@{organisation})"
            )

    def profile_tree(
        self,
        profile_type: str,
        profile_source: str,
        profile_data_file: str,
        additional_profile_source: str = None,
    ):
        """
        Populates a tree with profile data and prints it.

        :param profile_type: Type of profile to visualise (e.g., "user_profile" or "repo_profile").
        :param profile_source: The source of the profile data (e.g., username or organization name).
        :param profile_data_file: The file to use for formatting profile data.
        :param additional_profile_source: An optional string representing an additional source
               for data retrieval (typically used with "repo_profile").
        """
        profile = self.api.get_profile(
            profile_type=profile_type,
            profile_source=profile_source,
            additional_profile_source=additional_profile_source,
        )
        if profile:
            formatted_profile = data_broker(
                raw_data=profile, data_file=profile_data_file
            )
            profile_title = (
                profile.get("full_name")
                if profile_type == "repo_profile"
                else profile.get("name")
            )

            additional_text = None
            if profile_type == "user_profile":
                additional_text = profile.get("bio")
            elif profile_type == "org_profile" or "repo_profile":
                additional_text = profile.get("description")
            else:
                log.critical(f"Unknown profile type: {profile_type}")

            print(
                self.create_tree(
                    tree_title=f"[bold]{profile_title}[/]",
                    tree_data=formatted_profile,
                    additional_text=additional_text,
                    additional_data=(
                        [
                            ("License", profile.get("license")),
                            ("Topics", profile.get("topics")),
                        ]
                        if profile_type == "repo_profile"
                        else None
                    ),
                )
            )
        else:
            log.warning(f"{profile_type} not found.")

    def repo_issues_tree(self, repo_name: str, repo_owner: str, issues_limit: int):
        raw_issues = self.api.get_repo_issues(
            repo_name=repo_name, repo_owner=repo_owner, limit=issues_limit
        )
        if raw_issues:
            issues_tree = self.create_tree(
                tree_title=f"Showing {issues_limit} {'issue' if len(raw_issues) < 2 else 'issues'} "
                f"for repository ({repo_name})",
            )
            for issue in raw_issues:
                brokered_data = data_broker(raw_data=issue, data_file="repo/issue.json")
                self.add_branch(
                    target_tree=issues_tree,
                    branch_title=issue.get("title"),
                    branch_data=brokered_data,
                    additional_data=[("Reactions", issue.get("reactions"))],
                )

            print(issues_tree)
        else:
            log.info(f"Repository ({repo_name}) does not have open issues.")

    def repo_releases_tree(self, repo_name: str, repo_owner: str, releases_limit: int):
        raw_releases = self.api.get_repo_releases(
            repo_name=repo_name, repo_owner=repo_owner, limit=releases_limit
        )
        if raw_releases:
            release_tree = self.create_tree(
                tree_title=f"Showing {releases_limit} {'release' if len(raw_releases) < 2 else 'releases'} "
                f"for repository ({repo_name})",
            )
            for release in raw_releases:
                brokered_data = data_broker(
                    raw_data=release, data_file="repo/release.json"
                )
                self.add_branch(
                    target_tree=release_tree,
                    branch_title=release.get("name"),
                    branch_data=brokered_data,
                )

            print(release_tree)
        else:
            log.info(f"Repository ({repo_name}) does not have releases.")
