import re
import time
import logging
from rich.tree import Tree
from rich import print as xprint
from octosuite.config import Emojis
from octosuite.messages import Message
from rich.prompt import Prompt, Confirm
from requests.auth import HTTPBasicAuth
from octosuite.attributes import Attributes
from octosuite.csv_loggers import CsvLoggers
from octosuite.miscellaneous import send_request


class Octosuite:
    def __init__(self):
        # GitHub API endpoint
        self.__endpoint = "https://api.github.com"

        # Initialise the Emojis instance.
        self.__emoji = Emojis()

        # Initialise the Message instance.
        self.__message = Message()

        # Initialise the CsvLoggers instance.
        self.__logger = CsvLoggers()

        # Initialise the Attributes instance,
        self.__attribute = Attributes()

    def get_user_profile(self, args):
        username = args.username or Prompt.ask(f"{self.__emoji.NAME_BADGE} (username)")
        response = send_request(f"{self.__endpoint}/users/{username}")

        if response[0] == 404:
            xprint(self.__message.user_not_found(username=username))
        elif response[0] == 200:
            user_profile_tree = Tree(f"\n{response[1]['name']}")
            for attr in self.__attribute.user_profile_attributes()[0]:
                user_profile_tree.add(
                    f"{self.__attribute.user_profile_attributes()[1][attr]}: {response[1][attr]}"
                )
            xprint(user_profile_tree)

            if args.log_to_csv or Confirm.ask(self.__message.prompt_log_csv()):
                self.__logger.log_user_profile(response[1])
        else:
            xprint(response[1])

    def get_repository_profile(self, args):
        username = args.username or Prompt.ask(f"{self.__emoji.NAME_BADGE} (username)")
        repository = args.repository or Prompt.ask(
            f"{self.__emoji.FILE_CABINET} (repository)"
        )

        response = send_request(f"{self.__endpoint}/repos/{username}/{repository}")
        if response[0] == 404:
            xprint(
                self.__message.repo_or_user_not_found(
                    repository=repository, username=username
                )
            )
        elif response[0] == 200:
            repository_profile_tree = Tree(f"\n{response[1]['full_name']}")
            for attr in self.__attribute.repository_profile_attributes()[0]:
                repository_profile_tree.add(
                    f"{self.__attribute.repository_profile_attributes()[1][attr]}: {response[1][attr]}"
                )
            xprint(repository_profile_tree)

            if args.log_to_csv or Confirm.ask(self.__message.prompt_log_csv()):
                self.__logger.log_repo_profile(response[1])
        else:
            xprint(response[1])

    def get_repository_path_contents(self, args):
        repository = args.repository or Prompt.ask(
            f"{self.__emoji.FILE_CABINET} (repository)"
        )
        repository_owner = args.username or Prompt.ask(
            f"{self.__emoji.NAME_BADGE} (owner)"
        )
        path_name = args.path_name or Prompt.ask(
            f"{self.__emoji.FILE_FOLDER} ~/path/name"
        )

        response = send_request(
            f"{self.__endpoint}/repos/{repository_owner}/{repository}/contents/{path_name}"
        )
        if response[0] == 404:
            xprint(
                self.__message.information_not_found(
                    param1=repository, param2=path_name, param3=repository_owner
                )
            )
        elif response[0] == 200:
            for content_count, content in enumerate(response[1], start=1):
                path_contents_tree = Tree(f"\n{content['name']}")
                for attr in self.__attribute.path_attributes()[0]:
                    path_contents_tree.add(
                        f"{self.__attribute.path_attributes()[1][attr]}: {content[attr]}"
                    )
                xprint(path_contents_tree)
                self.__logger.log_repo_path_contents(content, repository)
                xprint(f"Found {content_count} file(s) in {repository}/{path_name}.")
        else:
            xprint(response[1])

    def get_repository_contributors(self, args):
        repository = args.repository or Prompt.ask(
            f"{self.__emoji.FILE_CABINET} (repository)"
        )
        repository_owner = args.repository or Prompt.ask("-> (@Owner)")
        limit = args.limit or Prompt.ask(
            self.__message.limit_output(title="Repository contributors")
        )

        response = send_request(
            f"{self.__endpoint}/repos/{repository_owner}/"
            f"{repository}/contributors?per_page={limit}"
        )
        if response[0] == 404:
            xprint(
                self.__message.repo_or_user_not_found(
                    repository=repository, username=repository_owner
                )
            )
        elif response[0] == 200:
            for contributor in response[1]:
                contributor_tree = Tree(f"\n{contributor['login']}")
                for attr in self.__attribute.user_summary_attributes()[0]:
                    contributor_tree.add(
                        f"{self.__attribute.user_summary_attributes()[1][attr]}: {contributor[attr]}"
                    )
                xprint(contributor_tree)

                if args.log_to_csv or Confirm.ask(self.__message.prompt_log_csv()):
                    self.__logger.log_repo_contributors(
                        contributor=contributor, repo_name=repository
                    )
            else:
                xprint(response[1])

    def get_repository_stargazers(self, args):
        repository = args.repository or Prompt.ask(
            f"{self.__emoji.FILE_CABINET} (repository)"
        )
        repository_owner = args.username or Prompt.ask("-> (@Owner)")
        limit = args.limit or Prompt.ask(
            self.__message.limit_output(title="Repository stargazers")
        )

        response = send_request(
            f"{self.__endpoint}/repos/{repository_owner}/{repository}/stargazers?per_page={limit}"
        )
        if response[0] == 404:
            xprint(
                self.__message.repo_or_user_not_found(
                    repository=repository, username=repository_owner
                )
            )
        elif response[0] == {}:
            xprint(
                self.__message.repo_does_not_have(
                    title="stargazers", repository=repository, username=repository_owner
                )
            )
        elif response[0] == 200:
            for stargazer in response[1]:
                stargazer_tree = Tree(f"\n{stargazer['login']}")
                for attr in self.__attribute.user_summary_attributes()[0]:
                    stargazer_tree.add(
                        f"{self.__attribute.user_summary_attributes()[1][attr]}: {stargazer[attr]}"
                    )
                xprint(stargazer_tree)

                if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                    self.__logger.log_repo_stargazers(
                        stargazer=stargazer, repo_name=repository
                    )
        else:
            xprint(response[1])

    # repo forks
    def get_repository_forks(self, args):
        repository = args.repository or Prompt.ask(
            f"{self.__emoji.FILE_CABINET} (repository)"
        )
        repository_owner = args.username or Prompt.ask("-> (@Owner)")
        limit = args.limit or Prompt.ask(
            self.__message.limit_output(title="Repository forks")
        )

        response = send_request(
            f"{self.__endpoint}/repos/{repository_owner}/{repository}/forks?per_page={limit}"
        )
        if response[0] == 404:
            xprint(
                self.__message.repo_or_user_not_found(
                    repository=repository, username=repository_owner
                )
            )
        elif response[0] == {}:
            xprint(
                self.__message.repo_does_not_have(
                    title="forks", repository=repository, username=repository_owner
                )
            )
        elif response[0] == 200:
            for count, fork in enumerate(response):
                fork_tree = Tree(f"\n{fork['full_name']}")
                for attr in self.__attribute.repository_profile_attributes()[0]:
                    fork_tree.add(
                        f"{self.__attribute.repository_profile_attributes()[1][attr]}: {fork[attr]}"
                    )
                xprint(fork_tree)

                if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                    self.__logger.log_repo_forks(fork=fork, count=count)
        else:
            xprint(response)

    def get_repository_issues(self, args):
        repository = args.repository or Prompt.ask(
            f"{self.__emoji.FILE_CABINET} (repository)"
        )
        repository_owner = args.username or Prompt.ask("-> (@Owner)")
        limit = args.limit or Prompt.ask(
            self.__message.limit_output(title="Repository Issues")
        )

        response = send_request(
            f"{self.__endpoint}/repos/{repository_owner}/{repository}/issues?per_page={limit}"
        )
        if response[0] == 404:
            xprint(
                self.__message.repo_or_user_not_found(
                    repository=repository, username=repository_owner
                )
            )
        elif not response[1]:
            xprint(
                self.__message.repo_does_not_have(
                    title="open issues",
                    repository=repository,
                    username=repository_owner,
                )
            )
        elif response[0] == 200:
            for issue in response[1]:
                issues_tree = Tree(f"\n{issue['title']}")
                for attr in self.__attribute.repository_issues_attributes()[0]:
                    issues_tree.add(
                        f"{self.__attribute.repository_issues_attributes()[1][attr]}: {issue[attr]}"
                    )
                xprint(issues_tree)
                xprint(issue["body"])
                if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                    self.__logger.log_repo_issues(issue=issue, repo_name=repository)
        else:
            xprint(response[0])

    def get_repository_releases(self, args):
        repository = args.repository or Prompt.ask(
            f"{self.__emoji.FILE_CABINET} (repository)"
        )
        repository_owner = args.username or Prompt.ask(f"-> (@Owner)")
        limit = args.limit or Prompt.ask(
            self.__message.limit_output(title="Repository Releases")
        )

        response = send_request(
            f"{self.__endpoint}/repos/{repository_owner}/{repository}/releases?per_page={limit}"
        )
        if response[0] == 404:
            xprint(
                self.__message.repo_or_user_not_found(
                    repository=repository, username=repository_owner
                )
            )
        elif not response[0]:
            xprint(
                self.__message.repo_does_not_have(
                    title="releases", repository=repository, username=repository_owner
                )
            )
        elif response[0] == 200:
            for release in response[1]:
                releases_tree = Tree(f"\n{release['name']}")
                for attr in self.__attribute.repo_releases_attributes()[0]:
                    releases_tree.add(
                        f"{self.__attribute.repo_releases_attributes()[1][attr]}: {release[attr]}"
                    )
                xprint(releases_tree)
                xprint(release["body"])

                if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                    self.__logger.log_repo_releases(
                        release=release, repo_name=repository
                    )
        else:
            xprint(response[1])

    def get_organisation_profile(self, args):
        organisation = args.organisation or Prompt.ask(
            f"{self.__emoji.OFFICE_BUILDING} (organisation)"
        )
        response = send_request(f"{self.__endpoint}/orgs/{organisation}")

        if response[0] == 404:
            xprint(self.__message.org_not_found(organisation=organisation))
        elif response[0] == 200:
            organisation_profile_tree = Tree(f"\n{response[1]['name']}")
            for attr in self.__attribute.organisation_profile_attributes()[0]:
                organisation_profile_tree.add(
                    f"{self.__attribute.organisation_profile_attributes()[1][attr]}: {response[1][attr]}"
                )
            xprint(organisation_profile_tree)

            if args.log_to_csv or Confirm.ask(self.__message.prompt_log_csv()):
                self.__logger.log_organisation_profile(response=response[1])
        else:
            xprint(response[1])

    def get_organisation_repositories(self, args):
        organisation = args.organisation or Prompt.ask(
            f"{self.__emoji.OFFICE_BUILDING} (organisation)"
        )
        limit = args.limit or Prompt.ask(
            self.__message.limit_output("Organisation Repositories")
        )

        response = send_request(
            f"{self.__endpoint}/orgs/{organisation}/repos?per_page={limit}"
        )
        if response[0] == 404:
            xprint(self.__message.org_not_found(organisation=organisation))
        elif response[0] == 200:
            for repository in response[1]:
                repos_tree = Tree(f"\n{repository['full_name']}")
                for attr in self.__attribute.repository_profile_attributes()[0]:
                    repos_tree.add(
                        f"{self.__attribute.repository_profile_attributes()[1][attr]}: {repository[attr]}"
                    )
                xprint(repos_tree)

                if args.log_csv or Prompt.ask(self.__message.prompt_log_csv()):
                    self.__logger.log_organisation_repos(
                        repository=repository, organisation=organisation
                    )
        else:
            xprint(response[1])

    # organisation events
    def get_organisation_events(self, args):
        organisation = args.organisation or Prompt.ask(
            f"{self.__emoji.OFFICE_BUILDING} (organisation)"
        )
        limit = args.limit or Prompt.ask(
            self.__message.limit_output("Organisation Events")
        )

        response = send_request(
            f"{self.__endpoint}/orgs/{organisation}/events?per_page={limit}"
        )
        if response[0] == 404:
            xprint(self.__message.org_not_found(organisation=organisation))
        elif response[0] == 200:
            for event in response[1]:
                events_tree = Tree(f"\n{event['id']}")
                events_tree.add(f"Type: {event['type']}")
                events_tree.add(f"Created at: {event['created_at']}")
                xprint(events_tree)
                xprint(event["payload"])
                self.__logger.log_organisation_events(
                    event=event, organisation=organisation
                )
        else:
            xprint(response[1])

    # organisation member
    def is_organisation_member(self, args):
        username = args.username or Prompt.ask(f"{self.__emoji.NAME_BADGE} (username)")
        organisation = args.organisation or Prompt.ask(
            f"{self.__emoji.OFFICE_BUILDING} (organisation)"
        )

        response = send_request(
            f"{self.__endpoint}/orgs/{organisation}/public_members/{username}"
        )
        if response[0] == 204:
            xprint(
                f"@{username} (user) is a public member of @{organisation} (organisation)"
            )
        else:
            xprint(response[1]["message"])

    # Fetching user repositories
    def get_user_repositories(self, args):
        username = args.username or Prompt.ask(f"{self.__emoji.NAME_BADGE} (username)")
        limit = args.limit or Prompt.ask(
            self.__message.limit_output("User Repositories")
        )

        response = send_request(
            f"{self.__endpoint}/users/{username}/repos?per_page={limit}"
        )
        if response[0] == 404:
            xprint(self.__message.user_not_found(username=username))
        elif response[0] == 200:
            for repository in response[1]:
                repos_tree = Tree(f"\n{repository['full_name']}")
                for attr in self.__attribute.repository_profile_attributes()[0]:
                    repos_tree.add(
                        f"{self.__attribute.repository_profile_attributes()[1][attr]}: {repository[attr]}"
                    )
                xprint(repos_tree)

                if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                    self.__logger.log_user_repositories(
                        repository=repository, username=username
                    )
        else:
            xprint(response[1])

    def get_user_gists(self, args):
        username = args.username or Prompt.ask(f"{self.__emoji.NAME_BADGE} (username)")
        limit = args.limit or Prompt.ask(self.__message.limit_output("User Gists"))

        response = send_request(
            f"{self.__endpoint}/users/{username}/gists?per_page={limit}"
        )
        if not response[1]:
            xprint(f"@{username} (user) does not have gists.")
        elif response[0] == 404:
            xprint(self.__message.user_not_found(username=username))
        elif response[0] == 200:
            for gist in response[1]:
                gists_tree = Tree(f"\n{gist['id']}")
                for attr in self.__attribute.gist_attributes()[0]:
                    gists_tree.add(
                        f"{self.__attribute.gist_attributes()[1][attr]}: {gist[attr]}"
                    )
                xprint(gists_tree)

                if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                    self.__logger.log_user_gists(gist=gist)
        else:
            xprint(response[1])

    # Fetching a list of organisations that a user owns or belongs to
    def get_user_organisations(self, args):
        username = args.username or Prompt.ask(f"{self.__emoji.NAME_BADGE} (username)")
        limit = args.limit or Prompt.ask(
            self.__message.limit_output("User Organisations")
        )

        response = send_request(
            f"{self.__endpoint}/users/{username}/orgs?per_page={limit}"
        )
        if not response[1]:
            xprint(f"@{username} (user) does not belong to/own any organisations.")
        elif response[0] == 404:
            xprint(self.__message.user_not_found(username=username))
        elif response[0] == 200:
            for organisation in response[1]:
                org_tree = Tree(f"\n{organisation['login']}")
                for attr in self.__attribute.user_orgs_information_attributes()[0]:
                    org_tree.add(
                        f"{self.__attribute.user_orgs_information_attributes()[1][attr]}: "
                        f"{organisation[attr]}"
                    )
                xprint(org_tree)

                if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                    self.__logger.log_user_organisations(
                        organisation=organisation, username=username
                    )
        else:
            xprint(response[1])

    def get_user_events(self, args):
        username = args.username or Prompt.ask(f"{self.__emoji.NAME_BADGE} (username)")
        limit = args.limit or Prompt.ask(self.__message.limit_output("User Events"))

        response = send_request(
            f"{self.__endpoint}/users/{username}/events/public?per_page={limit}"
        )
        if response[0] == 404:
            xprint(self.__message.user_not_found(username=username))
        elif response[0] == 200:
            for event in response[1]:
                events_tree = Tree(f"\n{event['id']}")
                events_tree.add(f"Actor: {event['actor']['login']}")
                events_tree.add(f"Type: {event['type']}")
                events_tree.add(f"Repository: {event['repo']['name']}")
                events_tree.add(f"Created at: {event['created_at']}")
                xprint(events_tree)
                xprint(event["payload"])
                self.__logger.log_user_events(event=event)
        else:
            xprint(response[1])

    def get_user_subscriptions(self, args):
        username = args.username or Prompt.ask(f"{self.__emoji.NAME_BADGE} (username)")
        limit = args.limit or Prompt.ask(
            self.__message.limit_output("User Subscriptions")
        )

        response = send_request(
            f"{self.__endpoint}/users/{username}/subscriptions?per_page={limit}"
        )
        if not response[1]:
            xprint(f"@{username} (user) does not have any subscriptions.")
        elif response[0] == 404:
            xprint(self.__message.user_not_found(username=username))
        elif response[0] == 200:
            for repository in response[1]:
                subscriptions_tree = Tree(f"\n{repository['full_name']}")
                for attr in self.__attribute.repository_profile_attributes()[0]:
                    subscriptions_tree.add(
                        f"{self.__attribute.repository_profile_attributes()[1][attr]}: "
                        f"{repository[attr]}"
                    )
                xprint(subscriptions_tree)

                if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                    self.__logger.log_user_subscriptions(
                        repository=repository, username=username
                    )
        else:
            xprint(response[1])

    # Fetching a list of users the target follows
    def get_user_following(self, args):
        username = args.username or Prompt.ask(f"{self.__emoji.NAME_BADGE} (username)")
        limit = args.limit or Prompt.ask(self.__message.limit_output("User Following"))

        response = send_request(
            f"{self.__endpoint}/users/{username}/following?per_page={limit}"
        )
        if not response[1]:
            xprint(f"@{username} (user) does not follow anyone.")
        elif response[0] == 404:
            xprint(self.__message.user_not_found(username=username))
        elif response[0] == 200:
            for user in response[1]:
                following_tree = Tree(f"\n{user['login']}")
                for attr in self.__attribute.user_summary_attributes()[0]:
                    following_tree.add(
                        f"{self.__attribute.user_summary_attributes()[1][attr]}: {user[attr]}"
                    )
                xprint(following_tree)

                if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                    self.__logger.log_user_following(user=user, username=username)
        else:
            xprint(response[1])

    def get_user_followers(self, args):
        username = args.username or Prompt.ask(f"{self.__emoji.NAME_BADGE} (username)")
        limit = args.limit or Prompt.ask(self.__message.limit_output("User Followers"))

        response = send_request(
            f"{self.__endpoint}/users/{username}/followers?per_page={limit}"
        )
        if not response[1]:
            xprint(f"@{username} (user) does not have followers.")
        elif response[0] == 404:
            xprint(self.__message.user_not_found(username=username))
        elif response[0] == 200:
            for follower in response[1]:
                followers_tree = Tree(f"\n{follower['login']}")
                for attr in self.__attribute.user_summary_attributes()[0]:
                    followers_tree.add(
                        f"{self.__attribute.user_summary_attributes()[1][attr]}: {follower[attr]}"
                    )
                xprint(followers_tree)

                if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                    self.__logger.log_user_followers(
                        follower=follower, username=username
                    )
        else:
            xprint(response[1])

    def check_if_user_follows(self, args):
        user_a = args.username or Prompt.ask(
            f"{self.__emoji.NAME_BADGE}{self.__emoji.LETTER_A} (username)"
        )
        user_b = args.username_b or Prompt.ask(
            f"{self.__emoji.NAME_BADGE}{self.__emoji.LETTER_B} (username)"
        )

        response = send_request(f"{self.__endpoint}/users/{user_a}/following/{user_b}")
        if response[0] == 204:
            xprint(f"@{user_a} follows @{user_b}")
        else:
            xprint(f"@{user_a} does not follow @{user_b}")

    def search_users(self, args):
        query = args.query or Prompt.ask(
            f"{self.__emoji.MAGNIFYING_GLASS_LEFT}{self.__emoji.MAGNIFYING_GLASS_LEFT}"
            f" (query)"
        )
        limit = args.limit or Prompt.ask(self.__message.limit_output("User Search"))

        response = send_request(
            f"{self.__endpoint}/search/users?q={query}&per_page={limit}"
        )
        for user in response[1]["items"]:
            users_search_tree = Tree(f"\n{user['login']}")
            for attr in self.__attribute.user_summary_attributes()[0]:
                users_search_tree.add(
                    f"{self.__attribute.user_summary_attributes()[1][attr]}: {user[attr]}"
                )
            xprint(users_search_tree)

            if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                self.__logger.log_users_search(user=user, query=query)

    def search_repositories(self, args):
        query = args.query or Prompt.ask(
            f"{self.__emoji.FILE_CABINET}{self.__emoji.MAGNIFYING_GLASS_LEFT}"
            f" (repository) (search)"
        )
        limit = args.limit or Prompt.ask(
            self.__message.limit_output("Repository Search")
        )

        response = send_request(
            f"{self.__endpoint}/search/repositories?q={query}&per_page={limit}"
        )
        for repository in response[1]["items"]:
            repos_search_tree = Tree(f"\n{repository['full_name']}")
            for attr in self.__attribute.repository_profile_attributes()[0]:
                repos_search_tree.add(
                    f"{self.__attribute.repository_profile_attributes()[1][attr]}: "
                    f"{repository[attr]}"
                )
            xprint(repos_search_tree)

            if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                self.__logger.log_repos_search(repository=repository, query=query)

    # Topics search
    def search_topics(self, args):
        query = args.query or Prompt.ask("-> (;Topic) (search)")
        limit = args.limit or Prompt.ask(self.__message.limit_output("Topic Search"))

        response = send_request(
            f"{self.__endpoint}/search/topics?q={query}&per_page={limit}"
        )
        for topic in response[1]["items"]:
            topics_search_tree = Tree(f"\n{topic['name']}")
            for attr in self.__attribute.topic_information_attributes()[0]:
                topics_search_tree.add(
                    f"{self.__attribute.topic_information_attributes()[1][attr]}: {topic[attr]}"
                )
            xprint(topics_search_tree)

            if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                self.__logger.log_topics_search(topic, query)

    def search_issues(self, args):
        query = args.query or Prompt.ask("-> (!Issue) (search)")
        limit = args.limit or Prompt.ask(self.__message.limit_output("Issue Search"))

        response = send_request(
            f"{self.__endpoint}/search/issues?q={query}&per_page={limit}"
        )
        for issue in response[1]["items"]:
            issues_search_tree = Tree(f"\n{issue['title']}")
            for attr in self.__attribute.repository_issues_attributes()[0]:
                issues_search_tree.add(
                    f"{self.__attribute.repository_issues_attributes()[1][attr]}: {issue[attr]}"
                )
            xprint(issues_search_tree)
            xprint(issue["body"])

            if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                self.__logger.log_issues_search(issue, query)

    def search_commits(self, args):
        query = args.query or Prompt.ask("-> Commit (search)")
        limit = args.limit or Prompt.ask(self.__message.limit_output("Commit Search"))

        response = send_request(
            f"{self.__endpoint}/search/commits?q={query}&per_page={limit}"
        )
        for commit in response[1]["items"]:
            commits_search_tree = Tree(f"\n{commit['commit']['tree']['sha']}")
            commits_search_tree.add(f"Author: {commit['commit']['author']['name']}")
            commits_search_tree.add(f"Username: {commit['author']['login']}")
            commits_search_tree.add(f"Email: {commit['commit']['author']['email']}")
            commits_search_tree.add(
                f"Commiter: {commit['commit']['committer']['name']}"
            )
            commits_search_tree.add(f"Repository: {commit['repository']['full_name']}")
            commits_search_tree.add(f"URL: {commit['html_url']}")
            xprint(commits_search_tree)
            xprint(commit["commit"]["message"])

            if args.log_csv or Confirm.ask(self.__message.prompt_log_csv()):
                self.__logger.log_commits_search(commit=commit, query=query)

    def exit_session(self):
        exit_prompt = Confirm.ask(self.__message.prompt_close_session())
        if exit_prompt:
            logging.info(self.__message.session_closed(str(time.asctime())))
            xprint(self.__message.session_closed(str(time.asctime())))
            exit()

    @staticmethod
    def __get_email_from_contributor(
        username: str, repository: str, contributor: str
    ) -> str:
        """
        Get the email address of a contributor in a GitHub repository.

        :param username: GitHub username
        :param repository: GitHub repository name
        :param contributor: Contributor's username
        :return: Email address of the contributor (None if not found)

        https://github.com/s0md3v/Zen/blob/master/zen.py#L84-L105
        """
        commits_url = (
            f"https://github.com/{username}/{repository}/commits?author={contributor}"
        )
        response = send_request(
            commits_url, authentication=HTTPBasicAuth(username, "")
        )[1]
        latest_commit_match = re.search(
            rf'href="/{username}/{repository}/commit/(.*?)"', response
        )
        latest_commit = latest_commit_match.group(1) if latest_commit_match else "dummy"
        commit_details_url = (
            f"https://github.com/{username}/{repository}/commit/{latest_commit}.patch"
        )
        commit_details = send_request(
            endpoint=commit_details_url, authentication=HTTPBasicAuth(username, "")
        )[1]
        email_match = re.search(r"<(.*)>", commit_details)
        email = email_match.group(1) if email_match else None
        return email

    def __get_unforked_repositories(self, username: str) -> list:
        """
        Get a list of unforked repositories for a GitHub user.

        :param username: GitHub username
        :return: List of unforked repository names
        """
        repos_url = f"{self.__endpoint}/users/{username}/repos?per_page=100&sort=pushed"
        response = send_request(
            endpoint=repos_url, authentication=HTTPBasicAuth(username, "")
        )
        unforked_repositories = [repo["name"] for repo in response if not repo["fork"]]
        return unforked_repositories

    def get_user_email(self, args):
        """
        Prompt the user for a GitHub username and retrieve the email address for the user's latest commit.

        :return: None

        https://github.com/s0md3v/Zen/blob/master/zen.py#L107-L113
        """
        username = args.username or Prompt.ask(f"{self.__emoji.NAME_BADGE} (username)")
        repos = self.__get_unforked_repositories(username)
        for repo in repos:
            email = self.__get_email_from_contributor(username, repo, username)
            if email:
                xprint(f"{username}: {email}")
                break
