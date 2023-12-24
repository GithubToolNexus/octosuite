from dataclasses import dataclass


@dataclass
class Account:
    username: str
    id: str
    node_id: str
    gravatar_id: str
    avatar_url: str
    type: str
    is_site_admin: bool
    profile_url: str


@dataclass
class User:
    name: str
    username: str
    twitter_x_username: str
    avatar_url: str
    id: str
    node_id: str
    email: str
    bio: str
    blog: str
    location: str
    followers: int
    following: int
    public_repositories: int
    public_gists: int
    organisation: str
    profile_url: str
    is_site_admin: bool
    is_open_to_work: bool
    joined_at: str
    update_at: str


@dataclass
class UserOrg:
    login: str
    id: str
    node_id: str
    about: str


@dataclass
class Organisation:
    name: str
    login: str
    id: str
    node_id: str
    avatar_url: str
    email: str
    about: str
    blog: str
    location: str
    followers: int
    following: int
    twitter_x_username: str
    public_repositories: int
    public_gists: int
    type: str
    is_verified: bool
    has_organisation_projects: bool
    has_repository_projects: bool
    url: str
    created_at: str
    updated_at: str


@dataclass
class Content:
    type: str
    name: str
    path: str
    size: int
    url: str
    download_url: str


@dataclass
class Repository:
    name: str
    id: str
    description: str
    stars: int
    forks: int
    watchers: int
    default_branch: int
    language: str
    open_issues: int
    homepage: str
    license: dict
    topics: list
    is_fork: bool
    allow_forking: bool
    is_archived: bool
    is_template: bool
    has_wiki: bool
    has_pages: bool
    has_projects: bool
    has_issues: bool
    has_downloads: bool
    clone_url: str
    ssh_url: str
    pushed_at: str
    created_at: str
    updated_at: str


def process_repositories(raw_repositories: list[dict]) -> list[Repository]:
    repositories_list: list = []
    for raw_repository in raw_repositories:
        repository = Repository(
            name=raw_repository.get("full_name"),
            id=raw_repository.get("id"),
            description=raw_repository.get("description"),
            stars=raw_repository.get("stargazers_count"),
            forks=raw_repository.get("forks"),
            watchers=raw_repository.get("watchers"),
            default_branch=raw_repository.get("default_branch"),
            language=raw_repository.get("language"),
            open_issues=raw_repository.get("open_issues"),
            homepage=raw_repository.get("homepage"),
            license=raw_repository.get("license"),
            topics=raw_repository.get("topics"),
            is_fork=raw_repository.get("fork"),
            allow_forking=raw_repository.get("allow_forking"),
            is_archived=raw_repository.get("archived"),
            is_template=raw_repository.get("is_template"),
            has_wiki=raw_repository.get("has_wiki"),
            has_pages=raw_repository.get("has_pages"),
            has_projects=raw_repository.get("has_projects"),
            has_issues=raw_repository.get("has_issues"),
            has_downloads=raw_repository.get("has_downloads"),
            clone_url=raw_repository.get("clone_url"),
            ssh_url=raw_repository.get("ssh_url"),
            pushed_at=raw_repository.get("pushed_at"),
            created_at=raw_repository.get("created_at"),
            updated_at=raw_repository.get("updated_at"),
        )
        repositories_list.append(repository)
    return repositories_list


def process_accounts(accounts: list[dict]) -> list[Account]:
    accounts_list: list = []
    for account in accounts:
        accounts_list.append(
            Account(
                username=account.get("login"),
                id=account.get("id"),
                node_id=account.get("node_id"),
                gravatar_id=account.get("gravatar_id"),
                avatar_url=account.get("avatar_url"),
                is_site_admin=account.get("site_admin"),
                type=account.get("type"),
                profile_url=account.get("html_url"),
            )
        )

    return accounts_list
