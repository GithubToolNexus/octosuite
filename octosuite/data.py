# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

from dataclasses import dataclass

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


@dataclass
class Event:
    type: str
    repository: str
    actor: str
    created_at: str


# -------------------------------------------------------------------------------------- #


@dataclass
class Account:
    username: str
    id: int
    node_id: str
    gravatar_id: str
    avatar_url: str
    type: str
    is_site_admin: bool
    profile_url: str


# ------------------------------------------------------------------------------------- #


@dataclass
class User:
    name: str
    username: str
    twitter_x_username: str
    avatar_url: str
    id: int
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


# ------------------------------------------------------------------------------------- #


@dataclass
class UserOrg:
    login: str
    id: int
    node_id: str
    about: str


# ------------------------------------------------------------------------------------- #


@dataclass
class Organisation:
    name: str
    login: str
    id: int
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


# ------------------------------------------------------------------------------------- #


@dataclass
class Content:
    type: str
    name: str
    path: str
    size: int
    url: str
    download_url: str


# ------------------------------------------------------------------------------------- #


@dataclass
class Repository:
    name: str
    description: str
    id: int
    node_id: str
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


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
