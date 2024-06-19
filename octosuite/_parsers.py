from typing import Literal


def parse_profile(profile: dict, profile_type: Literal["user", "org", "repo"]) -> dict:
    """
    Parses a GitHub entity's profile into an Object.

    :param profile: Raw profile data to be parsed.
    :type profile: dict
    :param profile_type: Type of the profile being parsed.
    :type profile_type: Literal
    :return: A dict object parsed with profile data.
    :rtype: dict
    """
    type_mapping: dict = {
        "user": {
            "name": profile.get("name"),
            "username": profile.get("login"),
            "bio": profile.get("bio"),
            "email": profile.get("email"),
            "id": profile.get("id"),
            "node_id": profile.get("node_id"),
            "avatar_url": profile.get("avatar_url"),
            "blog": profile.get("blog"),
            "location": profile.get("location"),
            "followers": profile.get("followers"),
            "following": profile.get("following"),
            "x_username": profile.get("twitter_username"),
            "public_gists": profile.get("public_gists"),
            "public_repositories": profile.get("public_repos"),
            "organisation": profile.get("company"),
            "is_open_to_work": profile.get("hireable"),
            "is_site_admin": profile.get("site_admin"),
            "profile_url": profile.get("html_url"),
            "joined_at": profile.get("created_at"),
            "update_at": profile.get("updated_at"),
        },
        "org": {
            "name": profile.get("name"),
            "login": profile.get("login"),
            "id": profile.get("id"),
            "node_id": profile.get("node_id"),
            "avatar_url": profile.get("avatar_url"),
            "email": profile.get("email"),
            "about": profile.get("description"),
            "blog": profile.get("blog"),
            "location": profile.get("location"),
            "followers": profile.get("followers"),
            "following": profile.get("following"),
            "twitter_x_username": profile.get("twitter_username"),
            "public_repositories": profile.get("public_repos"),
            "public_gists": profile.get("public_gists"),
            "type": profile.get("type"),
            "is_verified": profile.get("is_verified"),
            "has_organisation_projects": profile.get("has_organization_projects"),
            "has_repository_projects": profile.get("has_repository_projects"),
            "url": profile.get("html_url"),
            "created_at": profile.get("created_at"),
            "updated_at": profile.get("updated_at"),
        },
        "repo": {
            "name": profile.get("full_name"),
            "id": profile.get("id"),
            "node_id": profile.get("node_id"),
            "description": profile.get("description"),
            "stars": profile.get("stargazers_count"),
            "forks": profile.get("forks"),
            "watchers": profile.get("watchers"),
            "default_branch": profile.get("default_branch"),
            "language": profile.get("language"),
            "open_issues": profile.get("open_issues"),
            "homepage": profile.get("homepage"),
            "license": profile.get("license"),
            "topics": profile.get("topics"),
            "is_fork": profile.get("fork"),
            "allow_forking": profile.get("allow_forking"),
            "is_archived": profile.get("archived"),
            "is_template": profile.get("is_template"),
            "has_wiki": profile.get("has_wiki"),
            "has_pages": profile.get("has_pages"),
            "has_projects": profile.get("has_projects"),
            "has_issues": profile.get("has_issues"),
            "has_downloads": profile.get("has_downloads"),
            "clone_url": profile.get("clone_url"),
            "ssh_url": profile.get("ssh_url"),
            "pushed_at": profile.get("pushed_at"),
            "created_at": profile.get("created_at"),
            "updated_at": profile.get("updated_at"),
        },
    }

    if profile:
        return type_mapping.get(profile_type)
    else:
        return {}


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def parse_repos(repos: list[dict]) -> list[dict]:
    """
    Parses raw repositories into a list of dict objects.

    :param repos: A list of repositories to process.
    :type repos: list[dict]
    :return: A list of dict objects, each containing processed repository data.
    :rtype: list[dict]
    """
    repos_list: list = []
    for repo in repos:
        repos_list.append(
            {
                "name": repo.get("full_name"),
                "id": repo.get("id"),
                "node_id": repo.get("node_id"),
                "description": repo.get("description"),
                "stars": repo.get("stargazers_count"),
                "forks": repo.get("forks"),
                "watchers": repo.get("watchers"),
                "default_branch": repo.get("default_branch"),
                "language": repo.get("language"),
                "open_issues": repo.get("open_issues"),
                "homepage": repo.get("homepage"),
                "license": repo.get("license"),
                "topics": repo.get("topics"),
                "is_fork": repo.get("fork"),
                "allow_forking": repo.get("allow_forking"),
                "is_archived": repo.get("archived"),
                "is_template": repo.get("is_template"),
                "has_wiki": repo.get("has_wiki"),
                "has_pages": repo.get("has_pages"),
                "has_projects": repo.get("has_projects"),
                "has_issues": repo.get("has_issues"),
                "has_downloads": repo.get("has_downloads"),
                "clone_url": repo.get("clone_url"),
                "ssh_url": repo.get("ssh_url"),
                "pushed_at": repo.get("pushed_at"),
                "created_at": repo.get("created_at"),
                "updated_at": repo.get("updated_at"),
            }
        )

    if repos:
        return repos_list
    else:
        return [{}]


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def parse_accounts(accounts: list[dict]) -> list[dict]:
    """
    Parses a list of raw accounts into a list of dict objects.

    :param accounts: A list of accounts to process.
    :type accounts: list[dict]
    :return: A list of dict objects, each containing processed account data.
    :rtype: list[dict]
    """
    accounts_list: list = []
    for account in accounts:
        accounts_list.append(
            {
                "username": account.get("login"),
                "id": account.get("id"),
                "node_id": account.get("node_id"),
                "gravatar_id": account.get("gravatar_id"),
                "avatar_url": account.get("avatar_url"),
                "is_site_admin": account.get("site_admin"),
                "type": account.get("type"),
                "profile_url": account.get("html_url"),
            }
        )

    if accounts:
        return accounts_list
    else:
        return [{}]


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def parse_events(events: list[dict]) -> list[dict]:
    """
    Parses a list of raw events into a list of dict objects.

    :param events: A list of events to process.
    :type events: list[dict]
    :return: A list of dict objects, each containing processed event data.
    :rtype: list[dict]
    """
    events_list: list = []
    for event in events:
        events_list.append(
            {
                "type": event.get("type"),
                "repository": event.get("repo").get("name"),
                "actor": event.get("actor").get("login"),
                "created_at": event.get("created_at"),
            }
        )

    if events:
        return events_list
    else:
        return [{}]


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def parse_gists(gists: list[dict]) -> list[dict]:
    """
    Parses a list of raw gists into a list of dict objects.

    :param gists: A list of gists to process.
    :type gists: list[dict]
    :return: A list of dict objects, each containing processed gist data.
    :rtype: list[dict]
    """
    gists_list: list = []
    for gist in gists:
        gists_list.append(
            {
                "id": gist.get("id"),
                "node_id": gist.get("node_id"),
                "files": gist.get("files"),
                "description": gist.get("description"),
                "comments": gist.get("comments"),
                "created_at": gist.get("created_at"),
                "updated_at": gist.get("updated_at"),
            }
        )

    if gists:
        return gists_list
    else:
        return [{}]


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def parse_releases(releases: list[dict]) -> list[dict]:
    """
    Parses a list of raw releases into a list of dict objects.

    :param releases: A list of releases to process.
    :type releases: list[dict]
    :return: A list of dict objects, each containing processed release data.
    :rtype: list[dict]
    """
    releases_list: list = []
    for release in releases:
        releases_list.append(
            {
                "author": release.get("author").get("login"),
                "tag": release.get("tag_name"),
                "body": release.get("body"),
                "id": release.get("id"),
                "node_id": release.get("node_id"),
                "branch": release.get("target_commitish"),
                "is_prerelease": release.get("prerelease"),
                "url": release.get("html_url"),
                "created_at": release.get("created_at"),
                "published_at": release.get("published_at"),
            }
        )

    if releases:
        return releases_list
    else:
        return [{}]


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def parse_issues(issues: list[dict]) -> list[dict]:
    """
    Parses a list of raw issues into a list of dict objects.

    :param issues: A list of issues to process.
    :type issues: list[dict]
    :return: A list of dict objects, each containing processed issue data.
    :rtype: list[dict]
    """
    issues_list: list = []
    for issue in issues:
        issues_list.append(
            {
                "author": issue.get("user").get("login"),
                "number": issue.get("number"),
                "title": issue.get("title"),
                "body": issue.get("body"),
                "id": issue.get("id"),
                "node_id": issue.get("node_id"),
                "url": issue.get("html_url"),
                "created_at": issue.get("created_at"),
                "updated_at": issue.get("updated_at"),
            }
        )

    if issues:
        return issues_list
    else:
        return [{}]


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def parse_commits(commits: list[dict]) -> list[dict]:
    """
    Parses a list of raw commits into a list of dict objects.

    :param commits: A list of commits to process.
    :type commits: list[dict]
    :return: A list of dict objects, each containing processed commit data.
    :rtype: list[dict]
    """
    commits_list: list = []
    for commit in commits:
        commits_list.append(
            {
                "message": commit.get("commit").get("message"),
                "author": commit.get("commit").get("author").get("name"),
                "author_email": commit.get("commit").get("author").get("email"),
                "repository": commit.get("repository").get("full_name"),
                "url": commit.get("html_url"),
                "date": commit.get("commit").get("author").get("date"),
            }
        )

    if commits:
        return commits_list
    else:
        return [{}]


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def parse_topics(topics: list[dict]) -> list[dict]:
    """
    Parses a list of raw topics into a list of dict objects.

    :param topics: A list of topics to process.
    :type topics: list[dict]
    :return: A list of dict objects, each containing processed topic data.
    :rtype: list[dict]
    """
    topics_list: list = []
    for topic in topics:
        topics_list.append(
            {
                "name": topic.get("name"),
                "display_name": topic.get("display_name"),
                "short_description": topic.get("short_description"),
                "description": topic.get("description"),
                "created_by": topic.get("created_by"),
                "created_at": topic.get("created_at"),
                "updated_at": topic.get("updated_at"),
            }
        )

    if topics:
        return topics_list
    else:
        return [{}]


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
