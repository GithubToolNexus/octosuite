import os
import csv
from rich import print as xprint
from octosuite.messages import Message
from octosuite.attributes import Attributes


class CsvLoggers:
    def __init__(self):
        self.__attribute = Attributes()

    @staticmethod
    def __write_to_csv_file(fields: list, row: list, filename: str):
        """
        Write data to a CSV file.

        :param fields: List of field names for the CSV header.
        :param row: List of values for a single row in the CSV.
        :param filename: Name of the CSV file.
        :returns: None
        """
        from octosuite.config import OUTPUT_DIRECTORY

        file_path = os.path.join(OUTPUT_DIRECTORY, f"{filename}.csv")
        message = Message()

        with open(file_path, "w") as file:
            # Create a CSV writer object
            write_csv = csv.writer(file)

            # Write the header row to the CSV file
            write_csv.writerow(fields)

            # Write the data row to the CSV file
            write_csv.writerow(row)

            # Print a confirmation message
            xprint(f"{message.logged_to_csv(file.name)}")

    def log_organisation_profile(self, response: dict):
        fields = self.__attribute.organisation_profile_attributes()[0]
        fields.insert(1, "Organisation")

        row = [
            response["avatar_url"],
            response["name"],
            response["login"],
            response["id"],
            response["node_id"],
            response["email"],
            response["description"],
            response["location"],
            response["blog"],
            response["followers"],
            response["following"],
            response["twitter_username"],
            response["public_gists"],
            response["public_repos"],
            response["type"],
            response["is_verified"],
            response["has_organisation_projects"],
            response["has_repository_projects"],
            response["created_at"],
            response["updated_at"],
        ]

        self.__write_to_csv_file(fields=fields, row=row, filename=response["name"])

    def log_user_profile(self, response: dict):
        fields = self.__attribute.user_profile_attributes()[0]
        fields.insert(1, "name")

        row = [
            response["avatar_url"],
            response["name"],
            response["login"],
            response["id"],
            response["node_id"],
            response["bio"],
            response["blog"],
            response["location"],
            response["followers"],
            response["following"],
            response["twitter_username"],
            response["public_gists"],
            response["public_repos"],
            response["company"],
            response["hireable"],
            response["site_admin"],
            response["created_at"],
            response["updated_at"],
        ]

        self.__write_to_csv_file(fields=fields, row=row, filename=response["login"])

    def log_repo_profile(self, response: dict):
        fields = self.__attribute.repository_profile_attributes()[0]
        fields.insert(0, "Repository")

        row = [
            response["full_name"],
            response["name"],
            response["id"],
            response["description"],
            response["forks"],
            response["stargazers_count"],
            response["watchers"],
            response["license"],
            response["default_branch"],
            response["visibility"],
            response["language"],
            response["open_issues"],
            response["topics"],
            response["homepage"],
            response["clone_url"],
            response["ssh_url"],
            response["fork"],
            response["allow_forking"],
            response["private"],
            response["archived"],
            response["is_template"],
            response["has_wiki"],
            response["has_pages"],
            response["has_projects"],
            response["has_issues"],
            response["has_downloads"],
            response["pushed_at"],
            response["created_at"],
            response["updated_at"],
        ]

        self.__write_to_csv_file(fields=fields, row=row, filename=response["name"])

    def log_repo_path_contents(self, content: dict, repo_name: str):
        fields = self.__attribute.path_attributes()[0]
        fields.insert(0, "Filename")

        row = [
            content["name"],
            content["size"],
            content["type"],
            content["path"],
            content["sha"],
            content["html_url"],
        ]

        self.__write_to_csv_file(
            fields=fields,
            row=row,
            filename=f"{content['name']}_content_from_{repo_name}",
        )

    def log_repo_stargazers(self, stargazer: dict, repo_name: str):
        fields = self.__attribute.user_summary_attributes()[0]
        fields.insert(1, "Username")

        row = [
            stargazer["login"],
            stargazer["avatar_url"],
            stargazer["login"],
            stargazer["id"],
            stargazer["node_id"],
            stargazer["gravatar_id"],
            stargazer["type"],
            stargazer["site_admin"],
            stargazer["html_url"],
        ]

        self.__write_to_csv_file(
            fields=fields,
            row=row,
            filename=f"{stargazer['login']}_stargazer_of_{repo_name}",
        )

    def log_repo_forks(self, fork: dict, count: int):
        fields = self.__attribute.repository_profile_attributes()[0]
        fields.insert(0, "Repository")

        row = [
            fork["full_name"],
            fork["name"],
            fork["id"],
            fork["description"],
            fork["forks"],
            fork["stargazers_count"],
            fork["watchers"],
            fork["license"],
            fork["default_branch"],
            fork["visibility"],
            fork["language"],
            fork["open_issues"],
            fork["topics"],
            fork["homepage"],
            fork["clone_url"],
            fork["ssh_url"],
            fork["fork"],
            fork["allow_forking"],
            fork["private"],
            fork["archived"],
            fork["is_template"],
            fork["has_wiki"],
            fork["has_pages"],
            fork["has_projects"],
            fork["has_issues"],
            fork["has_downloads"],
            fork["pushed_at"],
            fork["created_at"],
            fork["updated_at"],
        ]

        self.__write_to_csv_file(
            fields=fields, row=row, filename=f"{fork['name']}_fork_{count}"
        )

    def log_repo_issues(self, issue: dict, repo_name: str):
        fields = self.__attribute.issue_information_attributes()[0]
        fields.insert(0, "Title")

        row = [
            issue["title"],
            issue["id"],
            issue["node_id"],
            issue["number"],
            issue["state"],
            issue["reactions"],
            issue["comments"],
            issue["milestone"],
            issue["assignee"],
            issue["assignees"],
            issue["author_association"],
            issue["labels"],
            issue["locked"],
            issue["active_lock_reason"],
            issue["closed_at"],
            issue["created_at"],
            issue["updated_at"],
        ]

        self.__write_to_csv_file(
            fields=fields, row=row, filename=f"{repo_name}_issue_{issue['id']}"
        )

    def log_repo_releases(self, release: dict, repo_name: str):
        fields = self.__attribute.repo_releases_attributes()[0]
        fields.insert(0, "Release")

        row = [
            release["name"],
            release["id"],
            release["node_id"],
            release["tag_name"],
            release["target_commitish"],
            release["assets"],
            release["draft"],
            release["prerelease"],
            release["created_at"],
            release["published_at"],
        ]

        self.__write_to_csv_file(
            fields=fields, row=row, filename=f"{repo_name}_release_{release['name']}"
        )

    def log_repo_contributors(self, contributor: dict, repo_name: str):
        fields = self.__attribute.user_summary_attributes()[0]
        fields.insert(1, "Username")

        row = [
            contributor["login"],
            contributor["avatar_url"],
            contributor["login"],
            contributor["id"],
            contributor["node_id"],
            contributor["gravatar_id"],
            contributor["type"],
            contributor["site_admin"],
            contributor["html_url"],
        ]

        self.__write_to_csv_file(
            fields=fields,
            row=row,
            filename=f"{contributor['login']}_contributor_of_{repo_name}",
        )

    def log_repo_events(self, event: dict, organisation: str):
        fields = ["ID", "Type", "Created at", "Payload"]
        row = [event["id"], event["type"], event["created_at"], event["payload"]]

        self.__write_to_csv_file(
            fields=fields, row=row, filename=f"{organisation}_event_{event['id']}"
        )

    def log_organisation_repos(self, repository: dict, organisation: str):
        fields = self.__attribute.repository_profile_attributes()[0].insert(
            0, "Repository"
        )

        row = [
            repository["full_name"],
            repository["name"],
            repository["id"],
            repository["description"],
            repository["forks"],
            repository["stargazers_count"],
            repository["watchers"],
            repository["license"],
            repository["default_branch"],
            repository["visibility"],
            repository["language"],
            repository["open_issues"],
            repository["topics"],
            repository["homepage"],
            repository["clone_url"],
            repository["ssh_url"],
            repository["fork"],
            repository["allow_forking"],
            repository["private"],
            repository["archived"],
            repository["is_template"],
            repository["has_wiki"],
            repository["has_pages"],
            repository["has_projects"],
            repository["has_issues"],
            repository["has_downloads"],
            repository["pushed_at"],
            repository["created_at"],
            repository["updated_at"],
        ]

        self.__write_to_csv_file(
            fields=fields,
            row=row,
            filename=f"{repository['name']}_repository_of_{organisation}",
        )

    def log_organisation_events(self, event: dict, organisation: str):
        fields = ["ID", "Type", "Created at", "Data"]
        row = [event["id"], event["type"], event["created_at"], event["payload"]]

        self.__write_to_csv_file(
            fields=fields, row=row, filename=f"{event['id']}_{organisation}"
        )

    def log_user_repositories(self, repository: dict, username: str):
        fields = self.__attribute.repository_profile_attributes()[0]
        fields.insert(0, "Repository")

        row = [
            repository["full_name"],
            repository["name"],
            repository["id"],
            repository["description"],
            repository["forks"],
            repository["stargazers_count"],
            repository["watchers"],
            repository["license"],
            repository["default_branch"],
            repository["visibility"],
            repository["language"],
            repository["open_issues"],
            repository["topics"],
            repository["homepage"],
            repository["clone_url"],
            repository["ssh_url"],
            repository["fork"],
            repository["allow_forking"],
            repository["private"],
            repository["archived"],
            repository["is_template"],
            repository["has_wiki"],
            repository["has_pages"],
            repository["has_projects"],
            repository["has_issues"],
            repository["has_downloads"],
            repository["pushed_at"],
            repository["created_at"],
            repository["updated_at"],
        ]

        self.__write_to_csv_file(
            fields=fields, row=row, filename=f"{repository['name']}_{username}"
        )

    def log_user_events(self, event: dict):
        fields = ["Actor", "Type", "Repository", "Created at", "Payload"]
        row = [
            event["actor"]["login"],
            event["type"],
            event["repo"]["name"],
            event["created_at"],
            event["payload"],
        ]

        self.__write_to_csv_file(
            fields=fields,
            row=row,
            filename=f"{event['actor']['login']}_event_{event['id']}",
        )

    def log_user_gists(self, gist: dict):
        fields = [
            "ID",
            "Node ID",
            "About",
            "Comments",
            "Files",
            "Git Push URL",
            "Is public?",
            "Is truncated?",
            "Updated at",
        ]
        row = [
            gist["id"],
            gist["node_id"],
            gist["description"],
            gist["comments"],
            gist["files"],
            gist["git_push_url"],
            gist["public"],
            gist["truncated"],
            gist["updated_at"],
        ]

        self.__write_to_csv_file(
            fields=fields,
            row=row,
            filename=f"{gist['id']}_gists_{gist['owner']['login']}",
        )

    def log_user_followers(self, follower: dict, username: str):
        fields = self.__attribute.user_summary_attributes()[0]
        fields.insert(1, "Username")

        row = [
            follower["login"],
            follower["avatar_url"],
            follower["login"],
            follower["id"],
            follower["node_id"],
            follower["gravatar_id"],
            follower["type"],
            follower["site_admin"],
            follower["html_url"],
        ]

        self.__write_to_csv_file(
            fields=fields,
            row=row,
            filename=f"{follower['login']}_follower_of_{username}",
        )

    def log_user_following(self, user: dict, username: str):
        fields = self.__attribute.user_summary_attributes()[0]
        fields.insert(1, "Username")

        row = [
            user["login"],
            user["avatar_url"],
            user["login"],
            user["id"],
            user["node_id"],
            user["gravatar_id"],
            user["type"],
            user["site_admin"],
            user["html_url"],
        ]

        self.__write_to_csv_file(
            fields=fields, row=row, filename=f"{user['login']}_followed_by_{username}"
        )

    def log_user_subscriptions(self, repository: dict, username: str):
        fields = self.__attribute.repository_profile_attributes()[0]
        fields.insert(0, "Repository")

        row = [
            repository["full_name"],
            repository["name"],
            repository["id"],
            repository["description"],
            repository["forks"],
            repository["stargazers_count"],
            repository["watchers"],
            repository["license"],
            repository["default_branch"],
            repository["visibility"],
            repository["language"],
            repository["open_issues"],
            repository["topics"],
            repository["homepage"],
            repository["clone_url"],
            repository["ssh_url"],
            repository["fork"],
            repository["allow_forking"],
            repository["private"],
            repository["archived"],
            repository["is_template"],
            repository["has_wiki"],
            repository["has_pages"],
            repository["has_projects"],
            repository["has_issues"],
            repository["has_downloads"],
            repository["pushed_at"],
            repository["created_at"],
            repository["updated_at"],
        ]

        self.__write_to_csv_file(
            fields=fields,
            row=row,
            filename=f"{username}_subscriptions_{repository['name']}",
        )

    def log_user_organisations(self, organisation: dict, username: str):
        fields = ["Profile photo", "Name", "ID", "Node ID", "URL", "About"]
        row = [
            organisation["avatar_url"],
            organisation["login"],
            organisation["id"],
            organisation["node_id"],
            organisation["url"],
            organisation["description"],
        ]

        self.__write_to_csv_file(
            fields=fields, row=row, filename=f"{organisation['login']}_{username}"
        )

    def log_users_search(self, user: dict, query: str):
        fields = self.__attribute.user_summary_attributes()[0].insert(1, "Username")

        row = [
            user["login"],
            user["avatar_url"],
            user["login"],
            user["id"],
            user["node_id"],
            user["gravatar_id"],
            user["type"],
            user["site_admin"],
            user["html_url"],
        ]

        self.__write_to_csv_file(
            fields=fields,
            row=row,
            filename=f"{user['login']}_user_search_result_for_{query}",
        )

    def log_repos_search(self, repository: dict, query: str):
        fields = self.__attribute.repository_profile_attributes()[0]
        fields.insert(0, "Repository")

        row = [
            repository["full_name"],
            repository["name"],
            repository["id"],
            repository["description"],
            repository["forks"],
            repository["stargazers_count"],
            repository["watchers"],
            repository["license"],
            repository["default_branch"],
            repository["visibility"],
            repository["language"],
            repository["open_issues"],
            repository["topics"],
            repository["homepage"],
            repository["clone_url"],
            repository["ssh_url"],
            repository["fork"],
            repository["allow_forking"],
            repository["private"],
            repository["archived"],
            repository["is_template"],
            repository["has_wiki"],
            repository["has_pages"],
            repository["has_projects"],
            repository["has_issues"],
            repository["has_downloads"],
            repository["pushed_at"],
            repository["created_at"],
            repository["updated_at"],
        ]

        self.__write_to_csv_file(
            fields=fields,
            row=row,
            filename=f"{repository['name']}_repository_" f"search_result_for_{query}",
        )

    def log_topics_search(self, topic: dict, query: str):
        fields = [
            "Name",
            "Score",
            "Curated",
            "Featured",
            "Display name",
            "Created by",
            "Created at",
            "Updated at",
        ]

        row = [
            topic["name"],
            topic["score"],
            topic["curated"],
            topic["featured"],
            topic["display_name"],
            topic["created_by"],
            topic["created_at"],
            topic["updated_at"],
        ]

        self.__write_to_csv_file(
            fields=fields,
            row=row,
            filename=f"{topic['name']}_topic_search_result_for_{query}",
        )

    def log_issues_search(self, issue: dict, query: str):
        fields = self.__attribute.issue_information_attributes()[0].insert(0, "Title")
        row = [
            issue["title"],
            issue["id"],
            issue["node_id"],
            issue["number"],
            issue["state"],
            issue["reactions"],
            issue["comments"],
            issue["milestone"],
            issue["assignee"],
            issue["assignees"],
            issue["author_association"],
            issue["labels"],
            issue["locked"],
            issue["active_lock_reason"],
            issue["closed_at"],
            issue["created_at"],
            issue["updated_at"],
        ]

        self.__write_to_csv_file(
            fields=fields,
            row=row,
            filename=f"{issue['id']}_issue_search_result_for_{query}",
        )

    def log_commits_search(self, commit, query):
        fields = [
            "SHA",
            "Author",
            "Username",
            "Email",
            "Committer",
            "Repository",
            "URL",
            "Description",
        ]
        row = [
            commit["commit"]["tree"]["sha"],
            commit["commit"]["author"]["name"],
            commit["author"]["login"],
            commit["commit"]["author"]["email"],
            commit["commit"]["committer"]["name"],
            commit["repository"]["full_name"],
            commit["html_url"],
            commit["commit"]["message"],
        ]

        self.__write_to_csv_file(
            fields=fields,
            row=row,
            filename=f"{commit['commit']['tree']['sha']}"
            f"_commit_search_result_for_{query}",
        )
