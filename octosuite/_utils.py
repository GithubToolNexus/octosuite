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
    search_examples,
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
    parser.add_argument(
        "-v",
        "--version",
        version=f"OctoSuite CLI/Library {version}",
        action="version",
    )
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
        help="get user's public repositories",
        action="store_true",
    )
    user_parser.add_argument(
        "-e",
        "--emails",
        help="get emails from user's public PushEvents",
        action="store_true",
    )
    user_parser.add_argument(
        "-o",
        "--orgs",
        help="get user's public organisations (owned/belonging to)",
        action="store_true",
    )
    user_parser.add_argument(
        "-ee",
        "--events",
        help="get user's public events",
        action="store_true",
    )
    user_parser.add_argument(
        "-g",
        "--gists",
        help="get user's public gists",
        action="store_true",
    )
    user_parser.add_argument(
        "-s",
        "--starred",
        help="get user's starred repositories",
        action="store_true",
    )
    user_parser.add_argument(
        "-f",
        "--followers",
        help="get user's followers",
        action="store_true",
    )
    user_parser.add_argument(
        "-ff",
        "--following",
        help="get accounts followed by user",
        action="store_true",
    )
    user_parser.add_argument(
        "-fff",
        "--follows",
        help="check if target follows the second specified user",
        type=str,
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
        help="get an organisation's profile",
        action="store_true",
    )
    org_parser.add_argument(
        "-r",
        "--repos",
        help="get an organisation's public repositories",
        action="store_true",
    )
    org_parser.add_argument(
        "-e",
        "--events",
        help="get an organisation's events",
        action="store_true",
    )
    org_parser.add_argument(
        "-m",
        "--is-member",
        dest="is_member",
        help="check if the specified user is a public member of the target organisation",
        type=str,
    )
    org_parser.add_argument(
        "-mm",
        "--members",
        help="get an organisation's public members",
        action="store_true",
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
        help="get a repository's data (similar to profile data)",
        action="store_true",
    )
    repo_parser.add_argument(
        "-c",
        "--contributors",
        help="get a repository's contributors",
        action="store_true",
    )
    repo_parser.add_argument(
        "-cc",
        "--contents",
        nargs="?",
        const="/",
        help="get a repository's files from a specified path (const: %(const)s)",
    )
    repo_parser.add_argument(
        "-s", "--stargazers", help="get a repository's stargazers", action="store_true"
    )
    repo_parser.add_argument(
        "-f", "--forks", help="get a repository's forks", action="store_true"
    )
    repo_parser.add_argument(
        "-i", "--issues", help="get a repository's open issues", action="store_true"
    )
    repo_parser.add_argument(
        "-r", "--releases", help="get a repository's releases", action="store_true"
    )

    # --------------------------------------------------------------- #

    # Search mode
    search_parser = subparsers.add_parser(
        "search",
        help="search operations",
        description=Markdown("# Entity/Target Discovery"),
        epilog=Markdown(search_examples),
        formatter_class=RichHelpFormatter,
    )

    search_parser.add_argument("query", help="search query")
    search_parser.add_argument(
        "-u", "--users", help="search users", action="store_true"
    )
    search_parser.add_argument(
        "-i", "--issues", help="search issues", action="store_true"
    )
    search_parser.add_argument(
        "-t", "--topics", help="search topics", action="store_true"
    )
    search_parser.add_argument(
        "-c", "--commits", help="search commits", action="store_true"
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
