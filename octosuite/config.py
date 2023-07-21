import os
import json
import getpass
import argparse
import subprocess
from typing import Any
from rich.table import Table
from rich.prompt import Confirm


class Emojis:
    def __init__(self):
        """
        Emoji class constructor. Initialises emoji code names
        """
        self.BUST_IN_SILHOUETTE = self.__get_emoji("BUST_IN_SILHOUETTE")
        self.BUSTS_IN_SILHOUETTE = self.__get_emoji("BUSTS_IN_SILHOUETTE")
        self.MAGNIFYING_GLASS_LEFT = self.__get_emoji("MAGNIFYING_GLASS_LEFT")
        self.FILE_CABINET = self.__get_emoji("FILE_CABINET")
        self.OFFICE_BUILDING = self.__get_emoji("OFFICE_BUILDING")
        self.WHITE_QUESTION_MARK = self.__get_emoji("WHITE_QUESTION_MARK")
        self.RED_QUESTION_MARK = self.__get_emoji("RED_QUESTION_MARK")
        self.INFORMATION = self.__get_emoji("INFORMATION")
        self.EXCLAMATION_MARK = self.__get_emoji("EXCLAMATION_MARK")
        self.EXCLAMATION_QUESTION_MARK = self.__get_emoji("EXCLAMATION_QUESTION_MARK")
        self.LETTER_A = self.__get_emoji("LETTER_A")
        self.LETTER_B = self.__get_emoji("LETTER_B")
        self.FILE_FOLDER = self.__get_emoji("FILE_FOLDER")
        self.OPEN_FILE_FOLDER = self.__get_emoji("OPEN_FILE_FOLDER")
        self.CARD_FILE_BOX = self.__get_emoji("CARD_FILE_BOX")
        self.LITTER_IN_BIN = self.__get_emoji("LITTER_IN_BIN")
        self.WASTEBASKET = self.__get_emoji("WASTEBASKET")
        self.NO_ENTRY = self.__get_emoji("NO_ENTRY")
        self.STOP_SIGN = self.__get_emoji("STOP_SIGN")
        self.GREEN_CHECK_MARK = self.__get_emoji("GREEN_CHECK_MARK")
        self.GREEN_CROSS_MARK = self.__get_emoji("GREEN_CROSS_MARK")
        self.SPIRAL_NOTEPAD = self.__get_emoji("SPIRAL_NOTEPAD")
        self.NOTEBOOK = self.__get_emoji("NOTEBOOK")
        self.OPEN_BOOK = self.__get_emoji("OPEN_BOOK")
        self.EYES = self.__get_emoji("EYES")
        self.RIGHT_ARROW = self.__get_emoji("RIGHT_ARROW")
        self.PAGE_FACING_UP = self.__get_emoji("PAGE_FACING_UP")
        self.FORK_AND_KNIFE = self.__get_emoji("FORK_AND_KNIFE")
        self.PACKAGE = self.__get_emoji("PACKAGE")
        self.GLOWING_STAR = self.__get_emoji("GLOWING_STAR")
        self.CHART_INCREASING = self.__get_emoji("CHART_INCREASING")
        self.EMAIL = self.__get_emoji("EMAIL")
        self.NAME_BADGE = self.__get_emoji("NAME_BADGE")
        self.RIGHT_ARROW_CURVING_LEFT = self.__get_emoji("RIGHT_ARROW_CURVING_LEFT")
        self.COMPUTER = self.__get_emoji("COMPUTER")
        self.COMPUTER_DISK = self.__get_emoji("COMPUTER_DISK")
        self.UP_BUTTON = self.__get_emoji("UP_BUTTON")
        self.IDENTIFICATION_CARD = self.__get_emoji("IDENTIFICATION_CARD")

    @staticmethod
    def __get_emoji(emoji_code: str) -> str:
        """
        Retrieves the value of the specified emoji from the settings.

        :param: emoji_code (str): Code of the emoji to retrieve.
        :return: Value of the specified emoji code.
        """
        return settings()["emojis"][emoji_code]


class Version:
    def __init__(self):
        """
        Version class constructor. Initialises the major, minor, patch and suffix parts of the version tag
        """
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
    def __init__(self, enable_colours=None):
        """
        Colours class constructor. Initialises colours if both the enable_colours parameter or input prompt are True.

        :param enable_colours: Command-line argument to enable colours (Default is None).
        """
        if enable_colours or Confirm.ask(
            ":white_question_mark: Would you like to enable colours for this session?"
        ):
            self.BLUE = self.__get_colour("BLUE")
            self.CYAN = self.__get_colour("CYAN")
            self.RED = self.__get_colour("RED")
            self.WHITE = self.__get_colour("WHITE")
            self.GREEN = self.__get_colour("GREEN")
            self.YELLOW = self.__get_colour("YELLOW")
            self.RESET = self.__get_colour("RESET")
        else:
            self.BLUE = (
                self.CYAN
            ) = self.RED = self.WHITE = self.GREEN = self.YELLOW = self.RESET = ""

    @staticmethod
    def __get_colour(colour_name: str) -> str:
        """
        Retrieves the value of the specified colour from the settings.

        :param: colour_name (str): Name of the colour to retrieve.
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


def create_parser() -> argparse.ArgumentParser:
    """
    Creates a command-line argument parser with the program's positional arguments and options.

    :returns: Object for passing command-line strings.
    """
    parser = argparse.ArgumentParser(
        description=f"{settings()['program']['name']}: {settings()['program']['about']}  — "
        f"by {settings()['program']['developer']['name']} ({settings()['program']['developer']['about']})",
        usage=usage(),
    )
    parser.add_argument(
        "-i",
        "--initialise",
        "--initialize",
        help="init method",
        choices=[
            "user-email",
            "user-profile",
            "user-repos",
            "user-gists",
            "user-orgs",
            "user-events",
            "user-subscriptions",
            "user-following",
            "user-followers",
            "user-follows",
            "org-profile",
            "org-repos",
            "org-events",
            "is-org-member",
            "repo-profile",
            "repo-contributors",
            "repo-stargazers",
            "repo-forks",
            "repo-issues",
            "repo-releases",
            "repo-path-contents",
            "users-search",
            "issues-search",
            "commits-search",
            "topics-search",
            "repos-search",
            "view-logs",
            "read-log",
            "delete-log",
            "clear-logs",
            "view-csv",
            "read-csv",
            "delete-csv",
            "clear-csv",
            "about",
        ],
    )
    parser.add_argument(
        "-a", "--about", help="show program's about information", action="store_true"
    )
    parser.add_argument(
        "-c",
        "--colours",
        "--colors",
        help="pass to run octosuite-cli with colours enabled",
        action="store_true",
    )
    parser.add_argument(
        "-csv",
        "--log-to-csv",
        help="log output to a csv file",
        action="store_true",
        dest="log_to_csv",
    )
    parser.add_argument(
        "-f", "--file", help="filename (used with logs/csv management arguments)"
    )
    parser.add_argument(
        "-l",
        "--limit",
        help="output limit (used with methods that return results in bulk) (default: %(default)s)",
        default=10,
    )
    parser.add_argument(
        "-o", "--organisation", "--organization", help="organisation name"
    )
    parser.add_argument(
        "-pn",
        "--path-name",
        help="path name (used with repo-path-contents)",
        dest="path_name",
    )
    parser.add_argument("-q", "--query", help="query (used with search arguments)")
    parser.add_argument("-r", "--repository", help="repository name")
    parser.add_argument("-u", "--username", help="username")
    parser.add_argument(
        "-ub",
        "--username-b",
        help="username-b (used with user-follows)",
        dest="username_b",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=Version().full_version()
    )

    return parser


def usage():
    return """
    Basic Usage
    ===========

        Get User Profile Info
        ---------------------
        octosuite-cli --initialise user-profile --username <username>


        Get User Repos
        --------------
        octosuite-cli --initialise user-repos --username <username>


        Get Organisation Profile Info
        -----------------------------
        octosuite-cli --initialise org-profile --organisation <organisation name>


        Get Organisation Repos
        -----------------------------
        octosuite-cli --initialise org-repos --organisation <organisation name>

        
        Get Repository Profile Info
        ---------------------------
        octosuite-cli --initialise repo-profile --username <username> --repository <repository name>


        Get Repository Forks
        --------------------
        octosuite-cli --initialise repo-forks --username <username> --repository <repository name>
        
    
    
    Searching
    =========

        Search Users
        ------------
        octosuite-cli --initialise users-search --query <query>

        
        Search Issues
        -------------
        octosuite-cli --initialise issues-search --query <query>

        
        Search Commits
        --------------
        octosuite-cli --initialise commits-search --query <query>
        

        Search Topics
        -------------
        octosuite-cli --initialise topics-search --query <query>
        

        Search Repositories
        -------------------
        octosuite-cli --initialise repos-search --query <query>



    Log Management
    ==============

        View logs
        ---------
        octosuite-cli --initialise view-logs


        Read log
        --------
        octosuite-cli --initialise read-log --file <log filename>


        Delete log
        ----------
        octosuite-cli --initialise delete-log --file <log filename>


        Clear logs
        ----------
        octosuite-cli --initialise clear-logs



    CSV Management
    ==============

        View CSV
        ---------
        octosuite-cli --initialise view-csv


        Read A Specified CSV File
        -------------------------
        octosuite-cli --initialise read-csv --file <csv filename>


        Delete CSV
        ----------
        octosuite-cli --initialise delete-csv --file <csv filename>


        Clear All CSV Files
        -------------------
        octosuite-cli --initialise clear-csv
        """


def setup_cli_completion():
    """
    Set up the readline module for command line completion.

    This function checks the operating system and imports the appropriate readline module.
    On Windows, it tries to import `pyreadline3` and installs it if not found.
    On other platforms, it imports the default `readline` module.

    If `readline` is imported successfully, it sets up command line completion using a custom completer function.
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


def setup_activity_logging() -> Any:
    """
    Setup logging program activity to a file.

    :returns: Any
    """
    import logging
    from datetime import datetime

    # Avoid using the ':' symbol in the log filename if the current system is Windows,
    # as files and directory names cannot be created with a colon.
    if os.name == "nt":
        now = datetime.now().strftime("octosuite-%d-%m-%Y %H-%M-%S%p")
    else:
        now = datetime.now().strftime("octosuite-%d-%m-%Y %H:%M:%S%p")

    # Construct the path to the log file
    log_file_path = os.path.join(LOGS_DIRECTORY, now)
    logging.basicConfig(
        filename=f"{log_file_path}.log",
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S%p",
        level=logging.DEBUG,
    )

    return logging


CURRENT_USERNAME = getpass.getuser()
USER_HOME_DIRECTORY = os.path.expanduser("~")
LOGS_DIRECTORY = os.path.join(USER_HOME_DIRECTORY, ".octosuite-logs")
OUTPUT_DIRECTORY = os.path.join(USER_HOME_DIRECTORY, "octosuite-output")
log = setup_activity_logging()
