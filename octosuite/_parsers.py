from octosuite.data import Event, Account, Repository


def parse_repos(repos: list[dict]) -> list[Repository]:
    repos_list: list = []
    for repo in repos:
        repos_list.append(
            Repository(
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
        )
    return repos_list


def parse_accounts(accounts: list[dict]) -> list[Account]:
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


def parse_events(events: list[dict]) -> list[Event]:
    events_list: list = []
    for event in events:
        events_list.append(
            Event(
                type=event.get("type"),
                repository=event.get("repo").get("name"),
                actor=event.get("actor").get("login"),
                created_at=event.get("created_at"),
            )
        )

    return events_list
