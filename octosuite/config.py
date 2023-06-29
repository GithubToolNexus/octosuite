import os
import json
import getpass
import logging
import argparse
import platform
import subprocess
from rich.table import Table
from datetime import datetime
from messages import Messages

message = Messages()


class Version:
    def __init__(self):
        self.major = settings()["program"]["version"]["major"]
        self.minor = settings()["program"]["version"]["minor"]
        self.patch = settings()["program"]["version"]["patch"]
        self.suffix = settings()["program"]["version"]["suffix"]

    def full_version(self) -> str:
        """
        Returns the full version string composed of the version components.
        :return: The complete version string in the format 'major.minor.patchsuffix'.
        """
        return f"{self.major}.{self.minor}.{self.patch}{self.suffix}"


class Colours:
    def __init__(self):
        self.RED = self.get_colour("RED")
        self.WHITE = self.get_colour("WHITE")
        self.GREEN = self.get_colour("GREEN")
        self.YELLOW = self.get_colour("YELLOW")
        self.RESET = self.get_colour("RESET")

    @staticmethod
    def get_colour(colour_name: str) -> str:
        """
        Retrieves the value of the specified colour from the settings.

        :param: colour_name (str): The name of the colour to retrieve.
        :return: The value of the specified colour.
        """
        return settings()["colours"][colour_name]


def settings() -> dict:
    """
    Loads the program's settings from /data/settings.json
    :return: Dictionary (JSON) containing program settings
    """
    # Get the absolute path of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the settings.json file
    settings_path = os.path.join(current_dir, "data", "settings.json")

    # Load the settings from the file
    with open(settings_path) as file:
        data = json.load(file)

    return data


def create_table(table_title: str, table_data: list, column_headers: list) -> Table:
    """
    Create a table with the given title, data, and column headers.

    :param table_title: The title of the table.
    :param table_data: The data to populate the table rows. Each inner list represents a row.
    :param column_headers: The column headers for the table.

    :return: The created table.
    """

    table = Table(title=table_title)

    for header_index, header in enumerate(column_headers):
        # Dim the first column header
        if header_index == 0:
            table.add_column(header, style="dim")
        else:
            table.add_column(header)

    for row in table_data:
        table.add_row(*row)

    return table


def create_parser():
    parser = argparse.ArgumentParser(
        description=f"{settings()['program']['name']}: {settings()['program']['about']}  — "
                    f"by {settings()['program']['developer']['name']} ({settings()['program']['developer']['about']})",
        usage=usage())
    parser.add_argument("method", help="method",
                        choices=["user_email", "user_profile", "user_repos", "user_gists", "user_orgs", "user_events",
                                 "user_subscriptions", "user_following", "user_followers", "user_follows",
                                 "org_profile", "org_repos", "org_events", "org_member",
                                 "repo_profile", "repo_contributors", "repo_stargazers", "repo_forks",
                                 "repo_issues", "repo_releases", "repo_path_contents", "users_search", "issues_search",
                                 "commits_search", "topics_search", "repos_search", "view_logs", "read_log",
                                 "delete_log",
                                 "clear_logs", "view_csv", "read_csv", "delete_csv", "clear_csv", "about", "author"])
    parser.add_argument("-a", "--about", help="show program's about information", action="store_true")
    parser.add_argument("-c", "--colors", "--colours", help="run octosuite cli with colours enabled",
                        action="store_true")
    parser.add_argument("-csv", "--log-to-csv", help="log output to a csv file", action="store_true", dest="log_to_csv")
    parser.add_argument("-f", "--file", help="filename (used with logs/csv management arguments)", dest="csv_file")
    parser.add_argument("-l", "--limit",
                        help="output limit (used with methods that return results in bulk) (default: %(default)s)",
                        default=10)
    parser.add_argument("-o", "--organisation", "--organization", help="organisation name")
    parser.add_argument("-pn", "--path-name", help="path name (used with repo_path_contents)", dest="path_name")
    parser.add_argument("-q", "--query", help="query (used with search arguments)")
    parser.add_argument("-r", "--repository", help="repository name")
    parser.add_argument("-u", "--username", help="username")
    parser.add_argument("-ub", "--username_b", help="username_b (used with user_follows)", dest="username_b")
    parser.add_argument("-v", "--version", action="version", version=Version().full_version())
    
    return parser


def usage():
    return """
    Basic Usage
    ===========

        Get User Profile Info
        ---------------------
        octosuite user_profile --username <username>


        Get User Repos
        --------------
        octosuite user_repos --username <username>


        Get Organisation Profile Info
        -----------------------------
        octosuite org_profile --organisation <organisation_name>


        Get Organisation Repos
        -----------------------------
        octosuite org_repos --organisation <organisation_name>

        
        Get Repository Profile Info
        ---------------------------
        octosuite repo_profile --username <username> --repository <repo_name>


        Get Repository Forks
        --------------------
        octosuite repo_forks --username <username> --repository <repo_name>
        
    
    
    Searching
    =========

        Search Users
        ------------
        octosuite users_search --query <query>

        
        Search Issues
        -------------
        octosuite issues_search --query <query>

        
        Search Commits
        --------------
        octosuite commits_search --query <query>
        

        Search Topics
        -------------
        octosuite topics_search --query <query>
        

        Search Repositories
        -------------------
        octosuite repos_search --query <query>



    Log Management
    ==============

        View logs
        ---------
        octosuite view_logs


        Read log
        --------
        octosuite read_log --log-file <log_file>


        Delete log
        ----------
        octosuite delete_log --log-file <log_file>


        Clear logs
        ----------
        octosuite clear_logs



    CSV Management
    ==============

        View CSV
        ---------
        octosuite view_csv


        Read A Specified CSV File
        -------------------------
        octosuite read_csv --file <csv_file>


        Delete CSV
        ----------
        octosuite delete_csv --file <csv_file>


        Clear All CSV Files
        -------------------
        octosuite clear_csv
        """


def setup_cli_completion() -> None:
    """
    Set up the readline module for command line completion.

    This function checks the operating system and imports the appropriate readline module.
    On Windows, it tries to import `pyreadline3` and installs it if not found.
    On other platforms, it imports the default `readline` module.

    If `readline` is imported successfully, it sets up command line completion using a custom completer function.

    :return: None
    """
    if os.name == "nt":
        try:
            from pyreadline3 import Readline
        except ImportError:
            subprocess.run(["pip", "install", "pyreadline3"], shell=False)
        readline = Readline()
    else:
        import readline

        def completer(text, state):
            options = [i for i in commands if i.startswith(text)]
            if state < len(options):
                return options[state]
            else:
                return None

        readline.parse_and_bind("tab: complete")
        readline.set_completer(completer)


def configure_logging():
    """
    Configure logging settings.

    :return: None
    """
    now = datetime.now()
    now_formatted = now.strftime("%Y-%m-%d %H-%M-%S%p")
    logging.basicConfig(
        filename=f".logs/{now_formatted}.log",
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %I:%M:%S%p",
        level=logging.DEBUG
    )

    # Log the start of a session
    logging.info(message.session_opened(platform.node(), getpass.getuser()))
