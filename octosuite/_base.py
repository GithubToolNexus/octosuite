# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

import aiohttp

from ._api import (
    get_data,
    get_accounts,
    get_profile,
    get_repos,
    REPOS_DATA_ENDPOINT,
    ORGS_DATA_ENDPOINT,
    USER_DATA_ENDPOINT,
    get_events,
    get_search,
)
from ._parsers import (
    parse_repos,
    parse_events,
    parse_accounts,
    parse_profile,
    parse_gists,
    parse_releases,
    parse_issues,
    parse_commits,
    parse_topics,
)
from .data import (
    Account,
    Repository,
    User,
    Organisation,
    Org,
    Content,
    Event,
    Gist,
    Release,
    Issue,
    Commit,
    Topic,
)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


class GitHubUser:
    """Represents a GitHub user, and provides methods fro getting data from the specified User."""

    # ---------------------------------------------------------------------------------- #

    def __init__(self, username: str):
        """
        Initialises a GitHubUser instance for fetching profile, repos, emails, followers, following,
        follows, starred, events, gists and orgs from a specified user.

        :param username: Username to get data from.
        :type username: str
        """
        self._username = username

    # ---------------------------------------------------------------------------------- #

    async def profile(self, session: aiohttp.ClientSession) -> User:
        """
        Asynchronously gets a user's profile.

        :param session: An aiohttp session to use for the request.
        :type session: aiohttp.ClientSession
        :return: A User object containing a user's profile data.
        :rtype: User
        """
        user: dict = await get_profile(
            profile_source=self._username, profile_type="user", session=session
        )
        return parse_profile(profile=user, profile_type="user")

    # ---------------------------------------------------------------------------------- #

    async def emails(self, session: aiohttp.ClientSession) -> set[str]:
        """
        Asynchronously gets emails from PushEvents on a user's repositories.

        :param session: An aiohttp session to use for the request.
        :type session: aiohttp.ClientSession
        :return: A set of emails from PushEvents
        :rtype: set
        """
        events = await get_data(
            endpoint=f"{USER_DATA_ENDPOINT}/{self._username}/events", session=session
        )
        emails = set()
        for event in events:
            if event.get("type") == "PushEvent":
                # Extracting commits from the push event
                commits = event.get("payload").get("commits")
                for commit in commits:
                    # Check if 'author' and 'email' keys exist
                    if "author" in commit and "email" in commit["author"]:
                        email = commit["author"]["email"]
                        if email not in emails:
                            emails.add(email)

        return emails

    # ---------------------------------------------------------------------------------- #

    async def followers(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Account]:
        """
        Asynchronously gets a user's followers.

        :param limit: Maximum number of followers to return.
        :type limit: int
        :param session: An aiohttp session to use for the request.
        :type session: aiohttp.ClientSession
        :return: A list of Account objects, each containing data of a follower.
        :rtype: list[Account]
        """
        raw_followers: list = await get_accounts(
            accounts_type="user_followers",
            accounts_source=self._username,
            limit=limit,
            session=session,
        )

        return parse_accounts(accounts=raw_followers)

    # ---------------------------------------------------------------------------------- #

    async def following(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Account]:
        """
        Asynchronously gets accounts that a user is following.

        :param limit: Maximum number of accounts to return.
        :type limit: int
        :param session: An aiohttp session to use for the request.
        :type session: aiohttp.ClientSession
        :return: A list of account objects, each containing data of an account.
        :rtype: list[Account]
        """
        raw_followings: list = await get_accounts(
            accounts_type="user_followings",
            accounts_source=self._username,
            limit=limit,
            session=session,
        )

        return parse_accounts(accounts=raw_followings)

    # ---------------------------------------------------------------------------------- #

    async def follows(self, user: str, session: aiohttp.ClientSession) -> str:
        """
        Asynchronously checks the following status of the target user with the specified second user.

        :param user: A user to check the following status with.
        :type user: str
        :param session: An aiohttp session to use for the request.
        :type session: aiohttp.ClientSession
        :return: A confirmation of the follow status between the two users.
        :rtype: str
        """
        async with session.get(
            f"{USER_DATA_ENDPOINT}/{self._username}/following/{user}"
        ) as response:
            status: str = (
                f"Target (@{self._username}) FOLLOWS user (@{user})."
                if response.status == 204
                else f"Target (@{self._username}) DOES NOT follow user (@{user}). "
                f"Also, check if one of or both provided usernames are valid."
            )
            return status

    # ---------------------------------------------------------------------------------- #

    async def starred(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Repository]:
        """
        Asynchronously gets a user's starred repositories.

        :param limit: Maximum number of repositories to return.
        :type limit: int
        :param session: An aiohttp session to use for the request.
        :type session: aiohttp.ClientSession
        :return: A list of Repository objects, each containing data of a repository.
        :rtype: list[Repository]
        """
        repositories: list = await get_repos(
            repos_source=self._username,
            repos_type="user_starred",
            limit=limit,
            session=session,
        )
        return parse_repos(repos=repositories)

    # ---------------------------------------------------------------------------------- #

    async def repos(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Repository]:
        """
        Asynchronously gets a user's repositories.

        :param limit: Maximum number of repositories to return.
        :type limit: int
        :param session: An aiohttp session to use for the request.
        :type session: aiohttp.ClientSession
        :return: A list of Repository objects, each containing data of a repository.
        :rtype: list[Repository]
        """
        repositories: list = await get_repos(
            repos_source=self._username,
            repos_type="user_repos",
            limit=limit,
            session=session,
        )
        return parse_repos(repos=repositories)

    # ---------------------------------------------------------------------------------- #

    async def events(self, limit: int, session: aiohttp.ClientSession) -> list[Event]:
        """
        Asynchronously gets a user's events.

        :param limit: Maximum number of events to return.
        :type limit: int
        :param session: An aiohttp session to use for the request.
        :type session: aiohttp.ClientSession
        :return: A list of Event objects, each containing data of an event.
        :rtype: list[Event]
        """
        user_events: list = await get_events(
            limit=limit,
            events_type="user",
            events_source=self._username,
            session=session,
        )

        return parse_events(events=user_events)

    # ---------------------------------------------------------------------------------- #

    async def gists(self, limit: int, session: aiohttp.ClientSession) -> list[Gist]:
        """
        Asynchronously gets a user's gists.

        :param limit: Maximum number of gists to return.
        :type limit: int
        :param session: An aiohttp session to use for the request.
        :type session: aiohttp.ClientSession
        :return: A list of Gist objects, each containing data of a gist.
        :rtype: list[Gist]
        """
        user_gists: list = await get_data(
            endpoint=f"{USER_DATA_ENDPOINT}/{self._username}/gists?per_page={limit}",
            session=session,
        )
        return parse_gists(gists=user_gists)

    # ---------------------------------------------------------------------------------- #

    async def orgs(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Organisation]:
        """
        Asynchronously gets a user's organisations.

        :param limit: Maximum number of organisations to return.
        :type limit: int
        :param session: An aiohttp session to use for the request.
        :type session: aiohttp.ClientSession
        :return: A list of Organisation objects, each containing data of an organisation.
        :rtype: list[Organisation]
        """
        user_orgs = await get_data(
            endpoint=f"{USER_DATA_ENDPOINT}/{self._username}/orgs?per_page={limit}",
            session=session,
        )
        orgs_list: list = []
        for org in user_orgs:
            orgs_list.append(
                Org(
                    login=org.get("login"),
                    id=org.get("id"),
                    node_id=org.get("node_id"),
                    about=org.get("description"),
                )
            )

        return orgs_list


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


class GitHubRepo:
    """Represents a GitHub repository, and provides methods for getting data from the specified repository."""

    # ---------------------------------------------------------------------------------- #

    def __init__(self, repo_name: str, repo_owner: str):
        self.repo_name = repo_name
        self.repo_owner = repo_owner

    # ---------------------------------------------------------------------------------- #

    async def profile(self, session: aiohttp.ClientSession) -> Repository:
        repo: dict = await get_profile(
            profile_source=self.repo_owner,
            additional_source=self.repo_name,
            profile_type="repo",
            session=session,
        )
        return parse_profile(profile=repo, profile_type="repo")

    # ---------------------------------------------------------------------------------- #

    async def forks(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Repository]:
        repositories: list = await get_repos(
            repos_source=self.repo_owner,
            additional_source=self.repo_name,
            repos_type="repo_forks",
            limit=limit,
            session=session,
        )
        return parse_repos(repos=repositories)

    # ---------------------------------------------------------------------------------- #

    async def stargazers(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Account]:
        raw_stargazers: list = await get_accounts(
            accounts_source=self.repo_owner,
            additional_source=self.repo_name,
            accounts_type="repo_stargazers",
            limit=limit,
            session=session,
        )

        return parse_accounts(accounts=raw_stargazers)

    # ---------------------------------------------------------------------------------- #

    async def contributors(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Account]:
        raw_contributors: list = await get_accounts(
            accounts_source=self.repo_owner,
            additional_source=self.repo_name,
            accounts_type="repo_contributors",
            limit=limit,
            session=session,
        )

        return parse_accounts(accounts=raw_contributors)

    # ---------------------------------------------------------------------------------- #

    async def contents(
        self, session: aiohttp.ClientSession, path: str = "/"
    ) -> list[Content]:
        is_path: str = f"contents/{path}" if path != "/" else "contents"
        raw_contents: list = await get_data(
            endpoint=f"{REPOS_DATA_ENDPOINT}/{self.repo_owner}/{self.repo_name}/{is_path}",
            session=session,
        )
        contents_lists: list = []
        for content in raw_contents:
            contents_lists.append(
                Content(
                    type=content.get("type"),
                    name=content.get("name"),
                    path=content.get("path"),
                    size=content.get("size") if content.get("type") == "file" else "",
                    url=content.get("html_url"),
                    download_url=content.get("download_url")
                    if content.get("type") == "file"
                    else "",
                )
            )

        return contents_lists

    # ---------------------------------------------------------------------------------- #

    async def releases(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Release]:
        repo_releases: list = await get_data(
            endpoint=f"{REPOS_DATA_ENDPOINT}/{self.repo_owner}/{self.repo_name}/releases?per_page={limit}",
            session=session,
        )

        if repo_releases:
            return parse_releases(releases=repo_releases)

    # ---------------------------------------------------------------------------------- #

    async def issues(self, limit: int, session: aiohttp.ClientSession) -> list[Issue]:
        repo_issues: list = await get_data(
            endpoint=f"{REPOS_DATA_ENDPOINT}/{self.repo_owner}/{self.repo_name}/issues?per_page={limit}",
            session=session,
        )
        if repo_issues:
            return parse_issues(issues=repo_issues)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


class GitHubOrg:
    def __init__(self, organisation: str):
        self._organisation = organisation

    # ---------------------------------------------------------------------------------- #

    async def profile(self, session: aiohttp.ClientSession) -> Organisation:
        org: dict = await get_profile(
            profile_type="org",
            profile_source=self._organisation,
            session=session,
        )
        return parse_profile(profile=org, profile_type="org")

    # ---------------------------------------------------------------------------------- #

    async def repos(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Repository]:
        repositories: list = await get_repos(
            repos_source=self._organisation,
            repos_type="org_repos",
            limit=limit,
            session=session,
        )
        return parse_repos(repos=repositories)

    # ---------------------------------------------------------------------------------- #

    async def is_member(self, user: str, session: aiohttp.ClientSession) -> str:
        async with session.get(
            f"{ORGS_DATA_ENDPOINT}/{self._organisation}/members/{user}"
        ) as response:
            status: str = (
                f"User (@{user}) IS a public member of the organisation (@{self._organisation})."
                if response.status == 204
                else f"User (@{user}) IS NOT a public member of the organisation (@{self._organisation}). "
                f"Also, check if the provided user and organisation names are valid."
            )

            return status

    # ---------------------------------------------------------------------------------- #

    async def members(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Account]:
        raw_members: list = await get_accounts(
            accounts_source=self._organisation,
            accounts_type="org_members",
            limit=limit,
            session=session,
        )
        if raw_members:
            return parse_accounts(accounts=raw_members)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


class GitHubSearch:
    @staticmethod
    async def users(
        query: str, limit: int, session: aiohttp.ClientSession
    ) -> list[Account]:
        results: list = await get_search(
            search_type="users", query=query, limit=limit, session=session
        )

        if results:
            return parse_accounts(accounts=results)

        # ---------------------------------------------------------------------------------- #

    @staticmethod
    async def repos(
        query: str, limit: int, session: aiohttp.ClientSession
    ) -> list[Repository]:
        results: list = await get_search(
            search_type="repos", query=query, limit=limit, session=session
        )

        if results:
            return parse_repos(repos=results)

        # ---------------------------------------------------------------------------------- #

    @staticmethod
    async def issues(
        query: str, limit: int, session: aiohttp.ClientSession
    ) -> list[Issue]:
        results: list = await get_search(
            search_type="issues", query=query, limit=limit, session=session
        )

        if results:
            return parse_issues(issues=results)

        # ---------------------------------------------------------------------------------- #

    @staticmethod
    async def commits(
        query: str, limit: int, session: aiohttp.ClientSession
    ) -> list[Commit]:
        results: list = await get_search(
            search_type="commits", query=query, limit=limit, session=session
        )

        if results:
            return parse_commits(commits=results)

        # ---------------------------------------------------------------------------------- #

    @staticmethod
    async def topics(
        query: str, limit: int, session: aiohttp.ClientSession
    ) -> list[Topic]:
        results: list = await get_search(
            search_type="topics", query=query, limit=limit, session=session
        )

        if results:
            return parse_topics(topics=results)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
