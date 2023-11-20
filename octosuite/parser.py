import argparse

from rich.markdown import Markdown
from rich_argparse import RichHelpFormatter


def create_parser() -> argparse.ArgumentParser:
    """
    Creates and configures an argument parser for the command line arguments.

    :return: A configured argparse.ArgumentParser object ready to parse the command line arguments.
    """
    from . import (
        __description__,
        __epilog__,
        __user_examples__,
        __organisation_examples__,
        __repository_examples__,
    )

    parser = argparse.ArgumentParser(
        description=Markdown(__description__, style="argparse.text"),
        epilog=Markdown(__epilog__, style="argparse.text"),
        formatter_class=RichHelpFormatter,
    )
    parser.add_argument("-d", "--debug", help="Enable debug mode", action="store_true")
    parser.add_argument(
        "-l", "--limit", help="Bulk data output limit", default=10, type=int
    )
    subparsers = parser.add_subparsers(dest="target", help="Target entity")

    # User mode
    user_parser = subparsers.add_parser(
        "user",
        help="User operations",
        description=Markdown("# User Investigation"),
        epilog=Markdown(__user_examples__),
        formatter_class=RichHelpFormatter,
    )
    user_parser.add_argument("username", help="Username to query")
    user_parser.add_argument(
        "-p", "--profile", help="Get a user's profile.", action="store_true"
    )
    user_parser.add_argument(
        "-r",
        "--repos",
        action="store_true",
        help="Get user's repositories",
    )
    user_parser.add_argument(
        "-e",
        "--emails",
        action="store_true",
        help="Get emails from user's PushEvents",
    )
    user_parser.add_argument(
        "-o",
        "--orgs",
        action="store_true",
        help="Get user's organisations (owned/belonging to)",
    )
    user_parser.add_argument(
        "-ee",
        "--events",
        action="store_true",
        help="Get user's events",
    )
    user_parser.add_argument(
        "-g",
        "--gists",
        action="store_true",
        help="Get user's gists",
    )
    user_parser.add_argument(
        "-s",
        "--starred",
        action="store_true",
        help="Get user's starred repositories",
    )
    user_parser.add_argument(
        "-f",
        "--followers",
        action="store_true",
        help="Get user's followers",
    )
    user_parser.add_argument(
        "-ff",
        "--following",
        action="store_true",
        help="Get accounts followed by user",
    )
    user_parser.add_argument(
        "-fff",
        "--follows",
        action="store_true",
        help="Check if user follows a second specified user",
    )
    user_parser.add_argument(
        "-su",
        "--secondary-username",
        dest="secondary_username",
        help="Secondary user (used with the -fff/--follows flag)",
    )

    # Org mode
    org_parser = subparsers.add_parser(
        "org",
        help="Organisation operations",
        description=Markdown("# Organisation Investigation"),
        epilog=Markdown(__organisation_examples__),
        formatter_class=RichHelpFormatter,
    )
    org_parser.add_argument("organisation", help="Organisation username to query")
    org_parser.add_argument(
        "-u",
        "--username",
        help="Username (used with -m/--member)",
    )
    org_parser.add_argument(
        "-p",
        "--profile",
        action="store_true",
        help="Get an organisation's profile",
    )
    org_parser.add_argument(
        "-r",
        "--repos",
        action="store_true",
        help="Get an organisation's repositories",
    )
    org_parser.add_argument(
        "-e",
        "--events",
        action="store_true",
        help="Get an organisation's events",
    )
    org_parser.add_argument(
        "-m",
        "--is-member",
        dest="is_member",
        action="store_true",
        help="Check if a specified user is a member of the organisation",
    )

    # Repo mode
    repo_parser = subparsers.add_parser(
        "repo",
        help="Repository operations",
        description=Markdown("# Repository Investigation"),
        epilog=Markdown(__repository_examples__),
        formatter_class=RichHelpFormatter,
    )
    repo_parser.add_argument("repo_name", help="Repository name to query")
    repo_parser.add_argument("repo_owner", help="Repository owner username")
    repo_parser.add_argument(
        "-p",
        "--profile",
        action="store_true",
        help="Get a repository's data (similar to profile data)",
    )
    repo_parser.add_argument(
        "-c",
        "--contributors",
        action="store_true",
        help="Get a repository's contributors",
    )
    repo_parser.add_argument(
        "-s", "--stargazers", action="store_true", help="Get a repository's stargazers"
    )
    repo_parser.add_argument(
        "-f", "--forks", action="store_true", help="Get a repository's forks"
    )
    repo_parser.add_argument(
        "-i", "--issues", action="store_true", help="Get a repository's issues"
    )
    repo_parser.add_argument(
        "-r", "--releases", action="store_true", help="Get a repository's releases"
    )
    return parser
