# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

import aiohttp

from .api import (
    get_data,
    get_accounts,
    get_profile,
    get_repositories,
    USER_DATA_ENDPOINT,
    REPOS_DATA_ENDPOINT,
)
from .data import (
    Account,
    process_repositories,
    Repository,
    User,
    process_accounts,
    Organisation,
    UserOrg,
    Content,
)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


class OctoUser:
    # ----------------------------------------------------------------- #

    def __init__(self, username: str):
        self.username = username

    # ----------------------------------------------------------------- #

    async def profile(self, session: aiohttp.ClientSession) -> User:
        user: dict = await get_profile(
            profile_source=self.username, profile_type="user", session=session
        )
        if "node_id" in user:
            return User(
                name=user.get("name"),
                username=user.get("login"),
                bio=user.get("bio"),
                email=user.get("email"),
                id=user.get("id"),
                node_id=user.get("node_id"),
                avatar_url=user.get("avatar_url"),
                blog=user.get("blog"),
                location=user.get("location"),
                followers=user.get("followers"),
                following=user.get("following"),
                twitter_x_username=user.get("twitter_username"),
                public_gists=user.get("public_gists"),
                public_repositories=user.get("public_repos"),
                organisation=user.get("company"),
                is_open_to_work=user.get("hireable"),
                is_site_admin=user.get("site_admin"),
                profile_url=user.get("html_url"),
                joined_at=user.get("created_at"),
                update_at=user.get("updated_at"),
            )

    # ----------------------------------------------------------------- #

    async def emails(self, session: aiohttp.ClientSession) -> set[str]:
        from .api import get_data, USER_DATA_ENDPOINT

        events = await get_data(
            endpoint=f"{USER_DATA_ENDPOINT}/{self.username}/events", session=session
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

    # ----------------------------------------------------------------- #

    async def followers(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Account]:
        raw_followers: list = await get_accounts(
            accounts_type="user_followers",
            accounts_source=self.username,
            limit=limit,
            session=session,
        )

        return process_accounts(accounts=raw_followers)

    # ----------------------------------------------------------------- #

    async def following(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Account]:
        raw_followings: list = await get_accounts(
            accounts_type="user_followings",
            accounts_source=self.username,
            limit=limit,
            session=session,
        )

        return process_accounts(accounts=raw_followings)

    # ----------------------------------------------------------------- #

    async def starred(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Repository]:
        repositories: list = await get_repositories(
            repos_source=self.username,
            repos_type="user_starred",
            limit=limit,
            session=session,
        )
        return process_repositories(raw_repositories=repositories)

    # ----------------------------------------------------------------- #

    async def repos(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Repository]:
        repositories: list = await get_repositories(
            repos_source=self.username,
            repos_type="user_repos",
            limit=limit,
            session=session,
        )
        return process_repositories(raw_repositories=repositories)

    # ----------------------------------------------------------------- #

    async def orgs(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Organisation]:
        user_orgs = await get_data(
            endpoint=f"{USER_DATA_ENDPOINT}/{self.username}/orgs?per_page={limit}",
            session=session,
        )
        orgs_list: list = []
        for org in user_orgs:
            orgs_list.append(
                UserOrg(
                    login=org.get("login"),
                    id=org.get("id"),
                    node_id=org.get("node_id"),
                    about=org.get("description"),
                )
            )

        return orgs_list


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


class OctoRepo:
    # ----------------------------------------------------------------- #

    def __init__(self, repo_name: str, repo_owner: str):
        self.repo_name = repo_name
        self.repo_owner = repo_owner

    # ----------------------------------------------------------------- #

    async def profile(self, session: aiohttp.ClientSession) -> Repository:
        repo: dict = await get_profile(
            profile_source=self.repo_owner,
            additional_source=self.repo_name,
            profile_type="repository",
            session=session,
        )
        if "node_id" in repo:
            return Repository(
                name=repo.get("full_name"),
                id=repo.get("id"),
                node_id=repo.get("node_id"),
                description=repo.get("description"),
                stars=repo.get("stargazers_count"),
                forks=repo.get("forks"),
                watchers=repo.get("watchers"),
                default_branch=repo.get("default_branch"),
                language=repo.get("language"),
                open_issues=repo.get("open_issues"),
                homepage=repo.get("homepage"),
                license=repo.get("license"),
                topics=repo.get("topics"),
                is_fork=repo.get("fork"),
                allow_forking=repo.get("allow_forking"),
                is_archived=repo.get("archived"),
                is_template=repo.get("is_template"),
                has_wiki=repo.get("has_wiki"),
                has_pages=repo.get("has_pages"),
                has_projects=repo.get("has_projects"),
                has_issues=repo.get("has_issues"),
                has_downloads=repo.get("has_downloads"),
                clone_url=repo.get("clone_url"),
                ssh_url=repo.get("ssh_url"),
                pushed_at=repo.get("pushed_at"),
                created_at=repo.get("created_at"),
                updated_at=repo.get("updated_at"),
            )

    # ----------------------------------------------------------------- #

    async def forks(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Repository]:
        repositories: list = await get_repositories(
            repos_source=self.repo_owner,
            additional_source=self.repo_name,
            repos_type="repo_forks",
            limit=limit,
            session=session,
        )
        return process_repositories(raw_repositories=repositories)

    # ----------------------------------------------------------------- #

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

        return process_accounts(accounts=raw_stargazers)

    # ----------------------------------------------------------------- #

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

        return process_accounts(accounts=raw_contributors)

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


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


class OctoOrg:
    def __init__(self, organisation: str):
        self._organisation = organisation

    # ----------------------------------------------------------------- #

    async def profile(self, session: aiohttp.ClientSession) -> Organisation:
        org: dict = await get_profile(
            profile_type="organisation",
            profile_source=self._organisation,
            session=session,
        )
        if "node_id" in org:
            return Organisation(
                name=org.get("name"),
                login=org.get("login"),
                id=org.get("id"),
                node_id=org.get("node_id"),
                avatar_url=org.get("avatar_url"),
                email=org.get("email"),
                about=org.get("description"),
                blog=org.get("blog"),
                location=org.get("location"),
                followers=org.get("followers"),
                following=org.get("following"),
                twitter_x_username=org.get("twitter_username"),
                public_repositories=org.get("public_repos"),
                public_gists=org.get("public_gists"),
                type=org.get("type"),
                is_verified=org.get("is_verified"),
                has_organisation_projects=org.get("has_organization_projects"),
                has_repository_projects=org.get("has_repository_projects"),
                url=org.get("html_url"),
                created_at=org.get("created_at"),
                updated_at=org.get("updated_at"),
            )

    # ----------------------------------------------------------------- #

    async def repos(
        self, limit: int, session: aiohttp.ClientSession
    ) -> list[Repository]:
        repositories: list = await get_repositories(
            repos_source=self._organisation,
            repos_type="org_repos",
            limit=limit,
            session=session,
        )
        return process_repositories(raw_repositories=repositories)

    # ----------------------------------------------------------------- #

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
            return process_accounts(accounts=raw_members)
