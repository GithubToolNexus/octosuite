import argparse

from rich.prompt import Prompt

from octosuite.masonry import Masonry


class Executor:
    def __init__(self, arguments: argparse, tree_masonry: Masonry):
        self.arguments: argparse = arguments
        self.tree_masonry: Masonry = tree_masonry
        self.handler = self.Handlers(executor=self)

    def execute_cli_arguments(self):
        """
        Orchestrates the execution of command line arguments based on the current command-line mode.
        """
        data_limit = self.arguments.limit or Prompt.ask(
            "Set output data limit", default="10"
        )
        target: str = self.arguments.target or Prompt.ask(
            "Select target entity to get data from",
            choices=["user", "org", "repo", "search"],
        )
        if target == "user":
            self.handler.user_mode_handler(
                username=self.arguments.username
                if hasattr(self.arguments, "username")
                else Prompt.ask("Enter entity (user) username"),
                secondary_username=self.arguments.secondary_username
                if hasattr(self.arguments, "secondary_username")
                else Prompt.ask("Enter entity (user) secondary username", default=None),
                data_limit=data_limit,
            )
        elif target == "org":
            self.handler.org_mode_handler(
                organisation=self.arguments.organisation
                if hasattr(self.arguments, "organisation")
                else Prompt.ask("Enter entity (organisation) username"),
                data_limit=data_limit,
                username=self.arguments.username
                if hasattr(self.arguments, "username")
                else Prompt.ask("Enter entity (user) username"),
            )
        elif target == "repo":
            self.handler.repo_mode_handler(
                repo_name=self.arguments.repo_name
                if hasattr(self.arguments, "repo_name")
                else Prompt.ask("Enter entity (repository) name"),
                repo_owner=self.arguments.repo_owner
                if hasattr(self.arguments, "repo_owner")
                else Prompt.ask("Enter entity (repository) owner username"),
                data_limit=data_limit,
            )

    class Handlers:
        def __init__(self, executor):
            self.arguments = executor.arguments
            self.tree_masonry = executor.tree_masonry

        def get_action(self, actions_map: dict, default_action: str) -> str:
            """
            Gets the action based on command-line arguments or interactive input.

            :param actions_map: A dictionary mapping action names to their corresponding functions.
            :param default_action: The default action to choose if no command-line argument is provided.
            :return: The chosen action name.
            """
            # Determine action from CLI arguments, default to None if not found
            action: str = next(
                (
                    action_name
                    for action_name in actions_map
                    if getattr(self.arguments, action_name, False)
                ),
                None,
            )

            # If no CLI argument for action, ask user interactively
            return action or Prompt.ask(
                "What type of data would you like to get?",
                choices=list(actions_map.keys()),
                default=default_action,
            )

        def user_mode_handler(
            self, username: str, data_limit: int, secondary_username: str = None
        ):
            """
            Executes user mode operations by mapping command line arguments to the respective user-related methods.

            :param username:
            :param secondary_username: A secondary username
                (used with -fff/--follows, to check if a `primary_user` follows a `secondary user`)
            :param data_limit: The limit for the amount of data to retrieve in bulk operations.
            """
            user_actions_map: dict = {
                "profile": lambda: self.tree_masonry.profile_tree(
                    profile_type="user_profile",
                    profile_source=username,
                    profile_data_file="user/profile.json",
                ),
                "emails": lambda: self.tree_masonry.user_emails_tree(username=username),
                "repos": lambda: self.tree_masonry.repos_tree(
                    repos_type="user_repos",
                    repos_source=username,
                    repos_limit=data_limit,
                ),
                "gists": lambda: self.tree_masonry.user_gists_tree(
                    username=username, limit=data_limit
                ),
                "orgs": lambda: self.tree_masonry.user_orgs_tree(limit=data_limit),
                "events": lambda: self.tree_masonry.events_tree(
                    events_type="user_events",
                    events_source=username,
                    events_limit=data_limit,
                ),
                "starred": lambda: self.tree_masonry.repos_tree(
                    repos_type="user_starred",
                    repos_source=username,
                    repos_limit=data_limit,
                ),
                "follows": lambda: self.tree_masonry.user_follows(
                    primary_user=username,
                    secondary_user=secondary_username,
                ),
                "followers": lambda: self.tree_masonry.users_tree(
                    users_type="user_followers",
                    users_limit=data_limit,
                    users_source=username,
                ),
                "following": lambda: self.tree_masonry.users_tree(
                    users_type="user_followings",
                    users_limit=data_limit,
                    users_source=username,
                ),
            }

            action: str = self.get_action(
                actions_map=user_actions_map, default_action="profile"
            )
            user_actions_map.get(action)()

        def repo_mode_handler(self, repo_name: str, repo_owner: str, data_limit: int):
            repo_actions_map: dict = {
                "profile": lambda: self.tree_masonry.profile_tree(
                    profile_type="repo_profile",
                    profile_source=repo_name,
                    additional_profile_source=repo_owner,
                    profile_data_file="repo/profile.json",
                ),
                "contributors": lambda: self.tree_masonry.users_tree(
                    users_type="repo_contributors",
                    users_source=repo_name,
                    additional_users_source=repo_owner,
                    contributors_limit=data_limit,
                ),
                "stargazers": lambda: self.tree_masonry.users_tree(
                    users_type="repo_stargazers",
                    users_source=repo_name,
                    additional_users_source=repo_owner,
                    users_limit=data_limit,
                ),
                "forks": lambda: self.tree_masonry.repos_tree(
                    repos_type="repo_forks",
                    repos_source=repo_name,
                    additional_repos_source=repo_owner,
                    forks_limit=data_limit,
                ),
                "issues": lambda: self.tree_masonry.repo_issues_tree(
                    repo_name=repo_name, repo_owner=repo_owner, issues_limit=data_limit
                ),
                "releases": lambda: self.tree_masonry.repo_releases_tree(
                    repo_name=repo_name,
                    repo_owner=repo_owner,
                    releases_limit=data_limit,
                ),
            }

            action: str = self.get_action(
                actions_map=repo_actions_map, default_action="profile"
            )
            repo_actions_map.get(action)()

        def org_mode_handler(
            self, organisation: str, data_limit: int, username: str = None
        ):
            """
            Executes user mode operations by mapping command line arguments to the respective
            organisation-related methods.

            :param organisation:
            :param username:
            :param data_limit: The limit for the amount of data to retrieve in bulk operations.
            """

            org_actions_map: dict = {
                "profile": lambda: self.tree_masonry.profile_tree(
                    profile_type="org_profile",
                    profile_source=organisation,
                    profile_data_file="org/profile.json",
                ),
                "repos": lambda: self.tree_masonry.repos_tree(
                    repos_type="org_repos",
                    repos_source=organisation,
                    repos_limit=data_limit,
                ),
                "events": lambda: self.tree_masonry.events_tree(
                    events_type="org_events",
                    events_source=organisation,
                    events_limit=data_limit,
                ),
                "is_member": lambda: self.tree_masonry.is_org_member(
                    organisation=organisation, username=username
                ),
            }

            action: str = self.get_action(
                actions_map=org_actions_map, default_action="profile"
            )
            org_actions_map.get(action)()
