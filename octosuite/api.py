# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

from typing import Union, Literal

import aiohttp
import rich
from rich.markdown import Markdown

from ._utils import console
from .help import Version

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

GITHUB_API_ENDPOINT: str = "https://api.github.com"
ORGS_DATA_ENDPOINT: str = f"{GITHUB_API_ENDPOINT}/orgs"
REPOS_DATA_ENDPOINT: str = f"{GITHUB_API_ENDPOINT}/repos"
USER_DATA_ENDPOINT: str = f"{GITHUB_API_ENDPOINT}/users"
SEARCH_DATA_ENDPOINT: str = f"{GITHUB_API_ENDPOINT}/search"
RELEASE_ENDPOINT: str = f"{REPOS_DATA_ENDPOINT}/bellingcat/octosuite/releases/latest"


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


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
                console.log(f"[yellow]✘[/] An API error occurred: {error_message}")
                return {}

    except aiohttp.ClientConnectionError as error:
        console.log(f"[yellow]✘[/] An HTTP error occurred: [red]{error}[/]")
        return {}
    except Exception as error:
        console.log(f"[yellow]✘[/] An unknown error occurred: [red]{error}[/]")
        return {}


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


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
        console.log(
            f"Unknown data type ({response_data}: {type(response_data)}), expected a list or dict."
        )


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


async def get_updates(session: aiohttp.ClientSession):
    """
    Asynchronously gets and compares the current program version with the remote version.

    Assumes version format: major.minor.patch.prefix

    :param session: aiohttp session to use for the request.
    :type session: aiohttp.ClientSession
    """
    # Make a GET request to PyPI to get the project's latest release.
    response: dict = await get_data(endpoint=RELEASE_ENDPOINT, session=session)
    release: dict = process_response(response_data=response, valid_key="tag_name")

    if release:
        remote_version: str = release.get("tag_name")
        markup_release_notes: str = release.get("body")
        markdown_release_notes = Markdown(markup=markup_release_notes)

        # Splitting the version strings into components
        remote_parts: list = remote_version.split(".")

        update_message: str = f"%s update ({remote_version}) available"

        # ------------------------------------------------------------------------- #

        # Check for differences in version parts
        if remote_parts[0] != Version.major:
            update_message = update_message % "MAJOR"

        # ------------------------------------------------------------------------- #

        elif remote_parts[1] != Version.minor:
            update_message = update_message % "MINOR"

        # ------------------------------------------------------------------------- #

        elif remote_parts[2] != Version.patch:
            update_message = update_message % "PATCH"

        # ------------------------------------------------------------------------- #

        if update_message:
            console.log(update_message)
            rich.print(markdown_release_notes)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


async def get_profile(
    profile_source: str,
    profile_type: Literal["user", "org", "repo"],
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
    :param additional_source: Additional profile source (optional, used with repo profile)
    :type additional_source: str
    :return: A dictionary object containing profile data.
    :rtype: dict
    """
    # Use a dictionary for direct mapping
    source_mapping: dict = {
        "user": f"{GITHUB_API_ENDPOINT}/users/{profile_source}",
        "org": f"{GITHUB_API_ENDPOINT}/orgs/{profile_source}",
        "repo": f"{REPOS_DATA_ENDPOINT}/{profile_source}/{additional_source}",
    }

    # Get the endpoint directly from the dictionary
    endpoint: str = source_mapping.get(profile_type, "")

    if not endpoint:
        raise ValueError(f"Invalid profile type in {source_mapping}: {profile_type}")

    profile_data: dict = await get_data(endpoint=endpoint, session=session)
    return process_response(response_data=profile_data, valid_key="created_at")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


async def get_repos(
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


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


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


async def get_events(
    limit: int,
    events_type: Literal["user", "org"],
    events_source: str,
    session: aiohttp.ClientSession,
) -> list[dict]:
    events_mapping: dict = {
        "user": f"{USER_DATA_ENDPOINT}/{events_source}/events",
        "org": f"{ORGS_DATA_ENDPOINT}/{events_source}/events",
    }

    events_endpoint: str = events_mapping.get(events_type)
    events_endpoint += f"?per_page={limit}"

    if not events_endpoint:
        raise ValueError(f"Invalid events type in {events_mapping}: {events_type}")

    events: list = await get_data(endpoint=events_endpoint, session=session)
    return process_response(response_data=events)


async def get_search(
    search_type: Literal["users", "repos", "issues", "commits", "topics"],
    query: str,
    limit: int,
    session: aiohttp.ClientSession,
) -> list[dict]:
    search_mapping: dict = {
        "users": f"{SEARCH_DATA_ENDPOINT}/users?q={query}",
        "repos": f"{SEARCH_DATA_ENDPOINT}/repositories?q={query}",
        "issues": f"{SEARCH_DATA_ENDPOINT}/issues?q={query}",
        "commits": f"{SEARCH_DATA_ENDPOINT}/commits?q={query}",
        "topics": f"{SEARCH_DATA_ENDPOINT}/topics?q={query}",
    }

    search_endpoint: str = search_mapping.get(search_type)
    search_endpoint += f"&per_page={limit}"

    if not search_endpoint:
        raise ValueError(f"Invalid search type in {search_mapping}: {search_type}")

    results: dict = await get_data(endpoint=search_endpoint, session=session)
    return process_response(response_data=results.get("items"))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
