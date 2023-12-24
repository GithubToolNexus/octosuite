# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

from typing import Union, Literal

import aiohttp

from ._utils import log

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

GITHUB_API_ENDPOINT: str = "https://api.github.com"
ORGS_DATA_ENDPOINT: str = f"{GITHUB_API_ENDPOINT}/orgs"
REPOS_DATA_ENDPOINT: str = f"{GITHUB_API_ENDPOINT}/repos"
USER_DATA_ENDPOINT: str = f"{GITHUB_API_ENDPOINT}/users"

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


async def get_data(session: aiohttp.ClientSession, endpoint: str) -> Union[dict, list]:
    """
    Asynchronously fetches JSON data from a given API endpoint.

    :param session: Aiohttp session to use for the request.
    :type session: aiohttp.ClientSession
    :param endpoint: API endpoint to fetch data from.
    :type endpoint: str
    :return: API response data as a dictionary or list. Returns an empty dict if fetching fails.
    :rtype: Union[dict, list]
    """
    try:
        async with session.get(
            endpoint,
        ) as response:
            if response.status in [200, 204]:
                return await response.json()
            else:
                error_message = await response.json()
                log.error(f"An API error occurred: {error_message}")
                return {}

    except aiohttp.ClientConnectionError as error:
        log.error(f"An HTTP error occurred: [red]{error}[/]")
        return {}
    except Exception as error:
        log.critical(f"An unknown error occurred: [red]{error}[/]")
        return {}


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def process_response(
    response_data: Union[dict, list], valid_key: str = None
) -> Union[dict, list]:
    """
    Processes and validates the API response data.

    f it's a dictionary and a valid_key is provided,
    checks for the presence of the key in the response dictionary.

    If it's a list, it ensures the list is not empty.

    :param response_data: API response data to validate, which should be a dictionary or list.
    :type response_data: Union[dict, list]
    :param valid_key: Key to check for in the dict data.
    :type valid_key: str
    :return: Original data if valid, or an empty dictionary or list if invalid.
    :rtype: Union[dict, list]
    """

    if isinstance(response_data, dict):
        if valid_key:
            return response_data if valid_key in response_data else {}
        else:
            return response_data  # Explicitly return the dictionary if valid_key is not provided
    elif isinstance(response_data, list):
        return response_data if response_data else []
    else:
        log.critical(
            f"Unknown data type ({response_data}: {type(response_data)}), expected a list or dict."
        )


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


async def get_profile(
    profile_source: str,
    profile_type: Literal["user", "organisation", "repository"],
    session: aiohttp.ClientSession,
    additional_source: str = None,
) -> dict:
    """
    Asynchronously fetches a profile from the specified source.

    :param profile_source: Profile source.
    :type profile_source: str
    :param profile_type: Type of profile to fetch.
    :type profile_type: str
    :param session: Aiohttp session to use for the request.
    :type session: aiohttp.ClientSession
    :param additional_source: Additional profile source (optional, used with repository profile)
    :type additional_source: str
    :return: A dictionary object containing profile data.
    :rtype: dict
    """
    # Use a dictionary for direct mapping
    source_mapping: dict = {
        "user": f"{GITHUB_API_ENDPOINT}/users/{profile_source}",
        "organisation": f"{GITHUB_API_ENDPOINT}/orgs/{profile_source}",
        "repository": f"{REPOS_DATA_ENDPOINT}/{profile_source}/{additional_source}",
    }

    # Get the endpoint directly from the dictionary
    endpoint: str = source_mapping.get(profile_type, "")

    if not endpoint:
        raise ValueError(f"Invalid profile type in {source_mapping}: {profile_type}")

    profile_data: dict = await get_data(endpoint=endpoint, session=session)
    return process_response(response_data=profile_data, valid_key="created_at")


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


async def get_repositories(
    limit: int,
    repos_source: str,
    session: aiohttp.ClientSession,
    repos_type: Literal["user_repos", "user_starred", "org_repos", "repo_forks"],
    additional_source: str = None,
) -> list[dict]:
    """
    Asynchronously fetches repositories from the specified source.

    :param limit: Maximum number of repositories to fetch.
    :type limit:  int
    :param repos_source: Repositories source.
    :type repos_source: str
    :param session: Aiohttp session to use for the request.
    :type session: aiohttp.ClientSession
    :param repos_type: Type of repositories to be fetched.
    :type repos_type: str
    :param additional_source: Additional repositories' source
        (optional, mostly used when fetching a repository's forks).
    :type additional_source: str
    :return: A list of dictionaries, each containing a repository's data.
    :rtype: list[dict]
    """
    source_mapping: dict = {
        "user_repos": f"{GITHUB_API_ENDPOINT}/users/{repos_source}/repos",
        "user_starred": f"{GITHUB_API_ENDPOINT}/users/{repos_source}/subscriptions",
        "org_repos": f"{ORGS_DATA_ENDPOINT}/{repos_source}/repos",
        "repo_forks": f"{REPOS_DATA_ENDPOINT}/{repos_source}/{additional_source}/forks",
    }
    # Get the endpoint directly from the dictionary
    endpoint: str = source_mapping.get(repos_type, "")
    endpoint += f"?per_page={limit}"

    if not endpoint:
        raise ValueError(f"Invalid posts type in {source_mapping}: {repos_type}")

    repositories: list = await get_data(endpoint=endpoint, session=session)
    return process_response(response_data=repositories)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


async def get_accounts(
    limit: int,
    accounts_source: str,
    session: aiohttp.ClientSession,
    accounts_type: Literal[
        "user_followers",
        "user_followings",
        "repo_contributors",
        "repo_stargazers",
        "org_members",
    ],
    additional_source: str = None,
) -> list[dict]:
    """
    Asynchronously fetches accounts from the specified source.

    :param limit: Maximum number of accounts to fetch.
    :type limit: int
    :param accounts_source: Accounts source.
    :type accounts_source: str
    :param session: Aiohttp session to use for the request.
    :type session: aiohttp.ClientSession
    :param accounts_type: Type of accounts to fetch.
    :type accounts_type: str
    :param additional_source: Additional accounts' source (optional, used with repository contributors and stargazers)
    :type additional_source: str
    :return: A list of dictionary objects, each containing an account's data.
    :rtype: list[dict]
    """
    source_mapping: dict = {
        "user_followers": f"{USER_DATA_ENDPOINT}/{accounts_source}/followers",
        "user_followings": f"{USER_DATA_ENDPOINT}/{accounts_source}/following",
        "repo_contributors": f"{REPOS_DATA_ENDPOINT}/{accounts_source}/{additional_source}"
        f"/contributors",
        "repo_stargazers": f"{REPOS_DATA_ENDPOINT}/{accounts_source}/{additional_source}/stargazers",
        "org_members": f"{ORGS_DATA_ENDPOINT}/{accounts_source}/members",
    }
    # Get the endpoint directly from the dictionary
    endpoint: str = source_mapping.get(accounts_type, "")
    endpoint += f"?per_page={limit}"

    if not endpoint:
        raise ValueError(f"Invalid posts type in {source_mapping}: {accounts_type}")

    accounts: list = await get_data(endpoint=endpoint, session=session)
    return process_response(response_data=accounts)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
