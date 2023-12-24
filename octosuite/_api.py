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
    Fetches JSON data from a given API endpoint.

    :param session: aiohttp session to use for the request.
    :param endpoint: The API endpoint to fetch data from.
    :return: Returns JSON data as a dictionary or list. Returns an empty dict if fetching fails.
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

    If it's a dictionary and a valid_key is provided,
    checks for the presence of the key in the response dictionary.

    If it's a list, it ensures the list is not empty.

    :param response_data: The API response data to validate, which should be a dictionary or list.
    :param valid_key: The key to check for in the data if it's a dictionary.
    :return: The original data if valid, or an empty dictionary or list if invalid.
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
    source: str,
    source_type: Literal["user", "org", "repo"],
    session: aiohttp.ClientSession,
    additional_source: str = None,
) -> dict:
    """
    Gets profile data from the specified profile_type and profile_source.

    :param source: Source to get profile data from.
    :param additional_source:
    :param session: aiohttp session to use for the request.
    :param source_type: The type of profile that is to be fetched.
    """
    # Use a dictionary for direct mapping
    source_mapping: dict = {
        "user": f"{GITHUB_API_ENDPOINT}/users/{source}",
        "org": f"{GITHUB_API_ENDPOINT}/orgs/{source}",
        "repo": f"{REPOS_DATA_ENDPOINT}/{source}/{additional_source}",
    }

    # Get the endpoint directly from the dictionary
    endpoint: str = source_mapping.get(source_type, "")

    if not endpoint:
        raise ValueError(f"Invalid profile type in {source_mapping}: {source_type}")

    profile_data: dict = await get_data(endpoint=endpoint, session=session)
    return process_response(response_data=profile_data, valid_key="created_at")


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


async def get_repositories(
    limit: int,
    source: str,
    session: aiohttp.ClientSession,
    repos_type: Literal["user_repos", "user_starred", "org_repos", "repo_forks"],
    additional_source: str = None,
) -> list[dict]:
    source_mapping: dict = {
        "user_repos": f"{GITHUB_API_ENDPOINT}/users/{source}/repos",
        "user_starred": f"{GITHUB_API_ENDPOINT}/users/{source}/subscriptions",
        "org_repos": f"{ORGS_DATA_ENDPOINT}/{source}/repos",
        "repo_forks": f"{REPOS_DATA_ENDPOINT}/{source}/{additional_source}" f"/forks",
    }
    # Get the endpoint directly from the dictionary
    endpoint: str = source_mapping.get(repos_type, "")

    if not endpoint:
        raise ValueError(f"Invalid posts type in {source_mapping}: {repos_type}")

    repositories: list = await get_data(
        endpoint=endpoint + f"?per_page={limit}", session=session
    )
    return process_response(response_data=repositories)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


async def get_users(
    limit: int,
    users_source: str,
    session: aiohttp.ClientSession,
    source_type: Literal[
        "user_followers",
        "user_followings",
        "repo_contributors",
        "repo_stargazers",
        "org_members",
    ],
    additional_source: str = None,
) -> list[dict]:
    source_mapping: dict = {
        "user_followers": f"{USER_DATA_ENDPOINT}/{users_source}/followers",
        "user_followings": f"{USER_DATA_ENDPOINT}/{users_source}/following",
        "repo_contributors": f"{REPOS_DATA_ENDPOINT}/{users_source}/{additional_source}"
        f"/contributors",
        "repo_stargazers": f"{REPOS_DATA_ENDPOINT}/{users_source}/{additional_source}/stargazers",
        "org_members": f"{ORGS_DATA_ENDPOINT}/{users_source}/members",
    }
    # Get the endpoint directly from the dictionary
    endpoint: str = source_mapping.get(source_type, "")

    if not endpoint:
        raise ValueError(f"Invalid posts type in {source_mapping}: {source_type}")

    users: list = await get_data(
        endpoint=endpoint + f"?per_page={limit}", session=session
    )
    return process_response(response_data=users)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
