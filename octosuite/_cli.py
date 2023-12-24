# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

import argparse
import asyncio
from datetime import datetime

import aiohttp
from rich.pretty import pprint

from ._utils import create_parser, log, version


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


async def stage(args: argparse.Namespace):
    # ---------------------------------------------------------------------------------- #

    from .base import OctoUser, OctoOrg, OctoRepo

    # ---------------------------------------------------------------------------------- #

    limit: int = args.limit

    user = OctoUser(username=args.username if hasattr(args, "username") else None)
    org = OctoOrg(
        organisation=args.organisation if hasattr(args, "organisation") else None
    )

    repo = OctoRepo(
        repo_name=args.repo_name if hasattr(args, "repo_name") else None,
        repo_owner=args.repo_owner if hasattr(args, "repo_owner") else None,
    )

    # ---------------------------------------------------------------------------------- #

    func_mapping: dict = {
        "user": [
            ("orgs", lambda session: user.orgs(limit=limit, session=session)),
            ("emails", lambda session: user.emails(session=session)),
            ("profile", lambda session: user.profile(session=session)),
            ("repos", lambda session: user.repos(limit=limit, session=session)),
            ("starred", lambda session: user.starred(limit=limit, session=session)),
            (
                "follows",
                lambda session: user.follows(
                    user=args.follows if hasattr(args, "follows") else None,
                    session=session,
                ),
            ),
            ("followers", lambda session: user.followers(limit=limit, session=session)),
            ("following", lambda session: user.following(limit=limit, session=session)),
        ],
        "repo": [
            (
                "contributors",
                lambda session: repo.contributors(limit=limit, session=session),
            ),
            (
                "contents",
                lambda session: repo.contents(
                    path=args.contents if hasattr(args, "contents") else None,
                    session=session,
                ),
            ),
            ("forks", lambda session: repo.forks(limit=limit, session=session)),
            ("profile", lambda session: repo.profile(session=session)),
            (
                "stargazers",
                lambda session: repo.stargazers(limit=limit, session=session),
            ),
        ],
        "org": [
            ("profile", lambda session: org.profile(session=session)),
            ("repos", lambda session: org.repos(limit=limit, session=session)),
            (
                "is_member",
                lambda session: org.is_member(
                    user=args.is_member if hasattr(args, "is_member") else None,
                    session=session,
                ),
            ),
            ("members", lambda session: org.members(limit=limit, session=session)),
        ],
    }

    # ---------------------------------------------------------------------------------- #

    if args.entity in func_mapping:
        async with aiohttp.ClientSession() as request_session:
            mode_action = func_mapping.get(args.entity)
            is_executed: bool = False

            for action, function in mode_action:
                if getattr(args, action, False):
                    call_function = await function(session=request_session)

                    if call_function:
                        pprint(call_function, expand_all=True)
                    is_executed = True

            if not is_executed:
                log.warning(
                    f"octosuite {args.entity}: missing one or more expected argument(s)."
                )


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def run():
    parser = create_parser()
    args = parser.parse_args()

    start_time = datetime.now()
    print(
        """
┏┓    ┏┓  •   
┃┃┏╋┏┓┗┓┓┏┓╋┏┓
┗┛┗┗┗┛┗┛┗┻┗┗┗ """
    )
    if args.entity:
        log.info(
            f"OctoSuite {version} started at {start_time.strftime('%a %b %d %Y, %I:%M:%S%p')}..."
        )
        try:
            asyncio.run(stage(args=args))
        except KeyboardInterrupt:
            log.warning("User interruption detected (Ctrl+C)")
        finally:
            log.info(f"Stopped in {datetime.now() - start_time} seconds.")
    else:
        parser.print_usage()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
