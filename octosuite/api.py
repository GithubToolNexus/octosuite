from typing import Optional, Union, Literal

import requests

from .coreutils import log
from .messages import message


class Api:
    def __init__(self, base_api_endpoint: str):
        self.user_data_endpoint = f"{base_api_endpoint}/users"
        self.orgs_data_endpoint = f"{base_api_endpoint}/orgs"
        self.repos_data_endpoint = f"{base_api_endpoint}/repos"
        self.updates_endpoint = (
            f"{base_api_endpoint}/repos/bellingcat/octosuite/releases/latest"
        )

    @staticmethod
    def get_data(
        endpoint: str, get_status_codes: bool = False
    ) -> Optional[Union[dict, list, int]]:
        """
        Fetches JSON data from a given API endpoint.

        :param endpoint: The API endpoint to fetch data from.
        :param get_status_codes: A boolean value indicating whether
            the response should only return status codes and not a dict or list.
        :return: Returns JSON data as a dictionary or list.
        """
        try:
            with requests.get(url=endpoint) as response:
                if get_status_codes:
                    return response.status_code
                else:
                    if response.status_code == 200:
                        return response.json()

                    else:
                        log.error(
                            message(
                                message_type="error",
                                message_key="api_error",
                                error_message=response.json(),
                            )
                        )
                        return {}
        except requests.exceptions.RequestException as e:
            log.error(
                message(
                    message_type="error",
                    message_key="http_error",
                    error_message=str(e),
                )
            )
            return {}
        except Exception as e:
            log.critical(
                message(
                    message_type="error",
                    message_key="unexpected_error",
                    error_message=str(e),
                )
            )
            return {}

    @staticmethod
    def validate_data(
        data: Union[dict, list], valid_key: str = None
    ) -> Union[dict, list, set]:
        """
        Validates the input data. If it's a dictionary and a valid_key is provided,
        checks for the presence of the key in the dictionary. If it's a list, it
        ensures the list is not empty.

        :param data: The data to validate, which should be a dictionary, list or set.
        :param valid_key: The key to check for in the data if it's a dictionary.
        :return: The original data if valid, or an empty dictionary/list/set if invalid.
        """
        if isinstance(data, dict):
            if valid_key:
                return data if valid_key in data else {}
            else:
                return data  # Explicitly return the dictionary if valid_key is not provided
        elif isinstance(data, list):
            return data if data else []
        else:
            log.critical(
                message(
                    message_type="critical",
                    message_key="unknown_critical",
                    critical_message=f"Unknown data type ({type(data).__name__}), expected a list or dict.",
                )
            )

    def get_updates(self):
        """
        This function checks if there's a new release of a project on GitHub.
        If there is, it shows a notification to the user about the release.
        """
        from . import __version__

        # Make a GET request to the GitHub API to get the latest release of the project.
        response = self.get_data(endpoint=self.updates_endpoint)

        if response:
            remote_version = response.get("tag_name")

            # Check if the remote version tag matches the current version tag.
            if remote_version != __version__:
                log.info(
                    message(
                        message_type="info",
                        message_key="update_found",
                        program_name="OctoSuite",
                        program_call_name="octosuite",
                        release_version=remote_version,
                    )
                )

    def get_profile(
        self,
        profile_type: str,
        profile_source: str = Union[
            Literal["user_profile"], Literal["org_profile"], Literal["repo_profile"]
        ],
        additional_profile_source: str = None,
    ) -> dict:
        """
        Get profile data based on the specified profile type.

        :param profile_source: A string representing the source of the profile data
                              (e.g., username, organization name).
        :param profile_type: Type of profile to retrieve data for
                            (e.g., "user_profile" or "org_profile").
        :param additional_profile_source: An optional string representing an additional source
                                         for data retrieval (used with "repo_profile" type).
        :return: A dictionary containing the profile data.
        """
        # Map profile types to their API endpoints
        profile_map = [
            ("user_profile", f"{self.user_data_endpoint}/{profile_source}"),
            ("org_profile", f"{self.orgs_data_endpoint}/{profile_source}"),
            (
                "repo_profile",
                f"{self.repos_data_endpoint}/{profile_source}/{additional_profile_source}",
            ),
        ]
        profile_endpoint = None
        for element, endpoint in profile_map:
            if element == profile_type:
                profile_endpoint = endpoint

        profile = self.get_data(endpoint=profile_endpoint)
        return self.validate_data(data=profile, valid_key="id")

    def get_user_emails(self, username: str) -> list:
        """
        Get the list of unique email addresses from a user's PushEvents.

        :param username: The username of the user whose emails are to be retrieved.
        :return: A list of unique email addresses.
        """
        events = self.get_data(endpoint=f"{self.user_data_endpoint}/{username}/events")
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

        return self.validate_data(data=list(emails))

    def get_repos(
        self,
        repos_limit: int,
        repos_source: str,
        repos_type: str = Union[
            Literal["user_repos"],
            Literal["user_starred"],
            Literal["org_repos"],
            Literal["repo_forks"],
        ],
        additional_repos_source: str = None,
    ) -> list:
        """
        Get a list of public repositories based on the specified repositories type.

        :param repos_type: Type of repositories to retrieve
                          (e.g., "user_repos" or "org_repos").
        :param repos_limit: The maximum number of repositories to retrieve.
        :param repos_source: The source of the repositories data
                            (e.g., username or organization name).
        :param additional_repos_source: An optional string representing an additional source
                                       for data retrieval (used with "repo_forks" type).
        :return: A list of repositories.
        """
        repos_map = [
            (
                "user_repos",
                f"{self.user_data_endpoint}/{repos_source}/repos?per_page={repos_limit}",
            ),
            (
                "user_starred",
                f"{self.user_data_endpoint}/{repos_source}/subscriptions?per_page={repos_limit}",
            ),
            (
                "org_repos",
                f"{self.orgs_data_endpoint}/{repos_source}/repos?per_page={repos_limit}",
            ),
            (
                "repo_forks",
                f"{self.repos_data_endpoint}/{repos_source}/{additional_repos_source}"
                f"/forks?per_page={repos_limit}",
            ),
        ]
        repos_endpoint = None
        for type_name, type_endpoint in repos_map:
            if type_name == repos_type:
                repos_endpoint = type_endpoint

        repos = self.get_data(endpoint=repos_endpoint)
        return self.validate_data(data=repos)

    def get_users(
        self,
        users_limit: int,
        users_source: str,
        users_type: str = Union[
            Literal["user_followers"],
            Literal["user_followings"],
            Literal["repo_contributors"],
            Literal["repo_stargazers"],
        ],
        additional_users_source: str = None,
    ) -> list:
        """
        Get a list of users based on the specified users type.

        :param users_type: Type of users to retrieve (e.g., "user_followers" or "repo_contributors").
        :param users_limit: The maximum number of users to retrieve.
        :param users_source: The source of the users data (e.g., username or repository name).
        :param additional_users_source: An optional string representing an additional source
                                       for data retrieval (used with "repo_contributors" or "repo_stargazers" type).
        :return: A list of users.
        """
        users_map = [
            (
                "user_followers",
                f"{self.user_data_endpoint}/{users_source}/followers?per_page={users_limit}",
            ),
            (
                "user_followings",
                f"{self.user_data_endpoint}/{users_source}/following?per_page={users_limit}",
            ),
            (
                "repo_contributors",
                f"{self.repos_data_endpoint}/{users_source}/{additional_users_source}"
                f"/contributors?per_page={users_limit}",
            ),
            (
                "repo_stargazers",
                f"{self.repos_data_endpoint}/{users_source}/{additional_users_source}"
                f"/stargazers?per_page={users_limit}",
            ),
        ]
        users_endpoint = None
        for type_name, type_endpoint in users_map:
            if type_name == users_type:
                users_endpoint = type_endpoint

        repos = self.get_data(endpoint=users_endpoint)
        return self.validate_data(data=repos)

    def get_user_gists(self, username: str, limit: int) -> list:
        """
        Get a list of public gists associated with a user.

        :param username: The username of the user whose gists are to be retrieved.
        :param limit: The maximum number of gists to retrieve.
        :return: A list of gists.
        """
        user_gists = self.get_data(
            endpoint=f"{self.user_data_endpoint}/{username}/gists?per_page={limit}"
        )
        return self.validate_data(data=user_gists)

    def get_user_orgs(self, username: str, limit: int) -> list:
        """
        Get a list of organizations that a user publicly belongs to.

        :param username: The username of the user whose organizations are to be retrieved.
        :param limit: The maximum number of organizations to retrieve.
        :return: A list of organizations.
        """
        user_orgs = self.get_data(
            endpoint=f"{self.user_data_endpoint}/{username}/orgs?per_page={limit}"
        )
        return self.validate_data(data=user_orgs)

    def get_events(
        self,
        events_source: str,
        events_limit: int,
        events_type: str = Union[Literal["user_events"], Literal["org_events"]],
    ):
        events_type_map = [
            (
                "user_events",
                f"{self.user_data_endpoint}/{events_source}/events/public?per_page={events_limit}",
            ),
            (
                "org_events",
                f"{self.orgs_data_endpoint}/{events_source}/events/public?per_page={events_limit}",
            ),
        ]

        events_endpoint = None
        for type_name, type_endpoint in events_type_map:
            if type_name == events_type:
                events_endpoint = type_endpoint

        events = self.get_data(endpoint=events_endpoint)
        return self.validate_data(data=events)

    def get_org_repos(self, organisation_name: str, limit: int) -> list:
        """
        Get a list of public repositories associated with an organisation.

        :param organisation_name: The name of the organisation whose repositories are to be retrieved.
        :param limit: The maximum number of repositories to retrieve.
        :return: A list of repositories.
        """
        org_repos = self.get_data(
            endpoint=f"{self.orgs_data_endpoint}/{organisation_name}/repos?per_page={limit}"
        )
        return self.validate_data(data=org_repos)

    def get_repo_issues(self, repo_name: str, repo_owner: str, limit: int) -> list:
        """
        Get a list of issues associated with a repository.

        :param repo_name: The name of the repository whose issues are to be retrieved.
        :param repo_owner: The owner or username of the repository.
        :param limit: The maximum number of issues to retrieve.
        :return: A list of issues.
        """
        repo_issues = self.get_data(
            endpoint=f"{self.repos_data_endpoint}/{repo_owner}/{repo_name}/issues?per_page={limit}"
        )

        return self.validate_data(data=repo_issues)

    def get_repo_releases(self, repo_name: str, repo_owner: str, limit: int) -> list:
        """
        Get a list of releases associated with a repository.

        :param repo_name: The name of the repository whose releases are to be retrieved.
        :param repo_owner: The owner or username of the repository.
        :param limit: The maximum number of releases to retrieve.
        :return: A list of releases.
        """
        repo_releases = self.get_data(
            endpoint=f"{self.repos_data_endpoint}/{repo_owner}/{repo_name}/releases?per_page={limit}"
        )

        return self.validate_data(data=repo_releases)
