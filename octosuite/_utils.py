# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

import argparse
import logging

from rich.logging import RichHandler
from rich.markdown import Markdown
from rich_argparse import RichHelpFormatter

from ._meta import (
    description,
    epilog,
    user_examples,
    organisation_examples,
    repository_examples,
    version,
)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def create_parser() -> argparse.ArgumentParser:
    """
    Creates and configures an argument parser for the command line arguments.

    :return: A configured argparse.ArgumentParser object ready to parse the command line arguments.
    """
    # --------------------------------------------------------------- #

    parser = argparse.ArgumentParser(
        description=Markdown(description, style="argparse.text"),
        epilog=Markdown(epilog, style="argparse.text"),
        formatter_class=RichHelpFormatter,
    )
    parser.add_argument("-d", "--debug", help="enable debug mode", action="store_true")
    parser.add_argument(
        "-l", "--limit", help="output data limit", default=100, type=int
    )
    parser.add_argument("-v", "--version", action="version", version=version)
    subparsers = parser.add_subparsers(dest="entity", help="target entity")

    # --------------------------------------------------------------- #

    # User mode
    user_parser = subparsers.add_parser(
        "user",
        help="user operations",
        description=Markdown("# User Investigation"),
        epilog=Markdown(user_examples),
        formatter_class=RichHelpFormatter,
    )
    user_parser.add_argument("username", help="username to query")
    user_parser.add_argument(
        "-p", "--profile", help="get a user's profile.", action="store_true"
    )
    user_parser.add_argument(
        "-r",
        "--repos",
        action="store_true",
        help="get user's public repositories",
    )
    user_parser.add_argument(
        "-e",
        "--emails",
        action="store_true",
        help="get emails from user's public PushEvents",
    )
    user_parser.add_argument(
        "-o",
        "--orgs",
        action="store_true",
        help="get user's public organisations (owned/belonging to)",
    )
    user_parser.add_argument(
        "-ee",
        "--events",
        action="store_true",
        help="get user's public events",
    )
    user_parser.add_argument(
        "-g",
        "--gists",
        action="store_true",
        help="get user's public gists",
    )
    user_parser.add_argument(
        "-s",
        "--starred",
        action="store_true",
        help="get user's starred repositories",
    )
    user_parser.add_argument(
        "-f",
        "--followers",
        action="store_true",
        help="get user's followers",
    )
    user_parser.add_argument(
        "-ff",
        "--following",
        action="store_true",
        help="get accounts followed by user",
    )
    user_parser.add_argument(
        "-fff",
        "--follows",
        action="store_true",
        help="check if user follows a second specified user",
    )
    user_parser.add_argument(
        "-su",
        "--secondary-username",
        dest="secondary_username",
        help="secondary user (used with the -fff/--follows flag)",
    )

    # --------------------------------------------------------------- #

    # Org mode
    org_parser = subparsers.add_parser(
        "org",
        help="organisation operations",
        description=Markdown("# Organisation Investigation"),
        epilog=Markdown(organisation_examples),
        formatter_class=RichHelpFormatter,
    )
    org_parser.add_argument("organisation", help="organisation to query")

    org_parser.add_argument(
        "-p",
        "--profile",
        action="store_true",
        help="get an organisation's profile",
    )
    org_parser.add_argument(
        "-r",
        "--repos",
        action="store_true",
        help="get an organisation's public repositories",
    )
    org_parser.add_argument(
        "-e",
        "--events",
        action="store_true",
        help="get an organisation's events",
    )
    org_parser.add_argument(
        "-m",
        "--members",
        action="store_true",
        help="get an organisation's public members",
    )

    # --------------------------------------------------------------- #

    # Repo mode
    repo_parser = subparsers.add_parser(
        "repo",
        help="repository operations",
        description=Markdown("# Repository Investigation"),
        epilog=Markdown(repository_examples),
        formatter_class=RichHelpFormatter,
    )
    repo_parser.add_argument("repo_name", help="repository name to query")
    repo_parser.add_argument("repo_owner", help="repository owner username")
    repo_parser.add_argument(
        "-p",
        "--profile",
        action="store_true",
        help="get a repository's data (similar to profile data)",
    )
    repo_parser.add_argument(
        "-c",
        "--contributors",
        action="store_true",
        help="get a repository's contributors",
    )
    repo_parser.add_argument(
        "-cc",
        "--contents",
        nargs="?",
        const="/",
        help="get a repository's files from a specified path (const: %(const)s)",
    )
    repo_parser.add_argument(
        "-s", "--stargazers", action="store_true", help="get a repository's stargazers"
    )
    repo_parser.add_argument(
        "-f", "--forks", action="store_true", help="get a repository's forks"
    )
    repo_parser.add_argument(
        "-i", "--issues", action="store_true", help="get a repository's open issues"
    )
    repo_parser.add_argument(
        "-r", "--releases", action="store_true", help="get a repository's releases"
    )
    return parser


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def setup_logging(enable_debug: bool) -> logging.getLogger:
    """
    Configure and return a logging object with the specified log level.

    :param enable_debug: A boolean value indicating whether debug mode should be enabled or not.
    :return: A logging object configured with the specified log level.
    """
    logging.basicConfig(
        level="NOTSET" if enable_debug else "INFO",
        format="%(message)s",
        handlers=[
            RichHandler(
                markup=True,
                log_time_format="%I:%M:%S%p",
                show_level=enable_debug,
                rich_tracebacks=True,
            )
        ],
    )
    return logging.getLogger(f"OctoSuite")


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

log = setup_logging(enable_debug=create_parser().parse_args().debug)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
