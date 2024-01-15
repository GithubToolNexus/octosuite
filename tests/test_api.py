# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

import aiohttp
import pytest

from conftest import (
    TEST_USERNAME,
    TEST_USER_TYPE,
    TEST_USER_ID,
    TEST_USER_NODE_ID,
    TEST_USER_CREATION_DATE,
    TEST_ORGANISATION,
    TEST_ORGANISATION_ID,
    TEST_ORGANISATION_NODE_ID,
    TEST_ORGANISATION_CREATION_DATE,
    TEST_REPOSITORY,
    TEST_REPOSITORY_ID,
    TEST_REPOSITORY_NODE_ID,
    TEST_REPOSITORY_CREATION_DATE,
    TEST_ORGANISATION_TYPE,
)
from octosuite._api import get_profile, get_accounts


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


@pytest.mark.asyncio
async def test_get_profile():
    async with aiohttp.ClientSession() as session:
        # ---------------------------------------------------------------- #

        user: dict = await get_profile(
            profile_type="user", profile_source=TEST_USERNAME, session=session
        )

        assert user.get("id") == TEST_USER_ID
        assert user.get("node_id") == TEST_USER_NODE_ID
        assert user.get("type") == TEST_USER_TYPE
        assert user.get("created_at") == TEST_USER_CREATION_DATE

        # ---------------------------------------------------------------- #

        organisation: dict = await get_profile(
            profile_type="org",
            profile_source=TEST_ORGANISATION,
            session=session,
        )

        assert organisation.get("id") == TEST_ORGANISATION_ID
        assert organisation.get("node_id") == TEST_ORGANISATION_NODE_ID
        assert organisation.get("type") == TEST_ORGANISATION_TYPE
        assert organisation.get("created_at") == TEST_ORGANISATION_CREATION_DATE

        # ---------------------------------------------------------------- #

        repository: dict = await get_profile(
            profile_source=TEST_USERNAME,
            additional_source=TEST_REPOSITORY,
            profile_type="repo",
            session=session,
        )

        assert repository.get("id") == TEST_REPOSITORY_ID
        assert repository.get("node_id") == TEST_REPOSITORY_NODE_ID
        assert repository.get("created_at") == TEST_REPOSITORY_CREATION_DATE


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


@pytest.mark.asyncio
async def test_get_accounts():
    async with aiohttp.ClientSession() as session:
        # ---------------------------------------------------------------- #

        user_followers: list = await get_accounts(
            accounts_type="user_followers",
            accounts_source=TEST_USERNAME,
            limit=50,
            session=session,
        )

        assert isinstance(user_followers, list)
        assert len(user_followers) == 50
        assert isinstance(user_followers[0], dict)
        assert user_followers[0].get("type") == "User"

        # ---------------------------------------------------------------- #

        repo_stargazers: list = await get_accounts(
            accounts_type="repo_stargazers",
            accounts_source=TEST_USERNAME,
            additional_source=TEST_REPOSITORY,
            limit=32,
            session=session,
        )

        assert len(repo_stargazers) == 32
        assert isinstance(repo_stargazers[0], dict)
        assert repo_stargazers[0].get("type") == "User"
