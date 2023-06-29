import os
import json
import psutil
import platform
import subprocess
from rich import print as xprint
from rich.markdown import Markdown
from urllib.request import urlopen
from octosuite.config import Colours
from octosuite.config import Version
from octosuite.messages import Messages

from urllib.error import HTTPError, URLError


colour = Colours()
message = Messages()
version = Version()


def path_finder(directories: list) -> None:
    """
    Checks if the specified directories exist.
    If not, it creates them.

    :param directories: List of directories to check and create
    :return: None
    """
    # Construct path to the user's home directory
    home_directory = os.path.expanduser("~")

    for directory in directories:
        # Construct and create each directory from the directories list if it doesn't already exist
        os.makedirs(os.path.join(home_directory, directory), exist_ok=True)


def systeminfo() -> dict:
    """
    Gets current system information.

    :return: Dictionary containing the following system information:
        - os: Operating system name
        - ram: Total RAM in GB
        - node: Hostname of the system
        - release: Operating system release
        - processor: Processor information
        - architecture: System architecture
    """
    ram_gb = f"{round(psutil.virtual_memory().total / (1024.0 ** 3))}GB"
    node = platform.node()
    system = platform.system()
    release = platform.release()
    sys_version = platform.version()
    os_name = f"{system} {sys_version}"
    processor = platform.processor()
    architecture = platform.architecture()[0]

    return {
        "os": os_name,
        "ram": ram_gb,
        "node": node,
        "release": release,
        "processor": processor,
        "architecture": architecture
    }


def send_request(endpoint: str) -> tuple:
    """
    Sends a GET request to the specified endpoint and returns the status code and JSON response.

    :param endpoint: URL endpoint to send the request to
    :return: Tuple containing the status code (int) and response data (dict)
    """
    try:
        with urlopen(endpoint) as response:
            response_data = json.loads(response.read().decode())
            status_code = response.status
        return status_code, response_data
    except (URLError, HTTPError) as exception:
        xprint(f": {colour.RED}{message.error(exception)}{colour.RESET}")
        return None, None


def list_files_and_directories(directory: str = None) -> None:
    """
    List contents of the specified directory or the current directory.

    :param directory: Directory path (optional)
    :return: None
    """
    if directory:
        command = ['cmd.exe', '/c', 'dir', directory] if os.name == "nt" else ['ls', directory]
    else:
        command = ['cmd.exe', '/c', 'dir'] if os.name == "nt" else ['ls']

    subprocess.run(command)


def check_updates() -> None:
    """
    Check for updates to Octosuite.

    This function queries the GitHub API to check for the latest release of Octosuite.
    If an update is available, it retrieves the release notes and returns them as markdown.

    :return: None
    """

    response = send_request("https://api.github.com/repos/bellingcat/octosuite/releases/latest")
    if response[1]['tag_name'] == version.full_version():
        pass
    else:
        raw_release_notes = response[1]['body']
        markdown_release_notes = Markdown(raw_release_notes)
        xprint(f"[{colour.GREEN}UPDATE{colour.RESET}] Octosuite v{response[1]['tag_name']} is available.")
        xprint(markdown_release_notes)
        xprint("\nRun `pip install --upgrade octosuite` to install the updates.")


def clear_screen() -> None:
    """
    Clears the screen with `cls` command if system is Windows.
    Otherwise, uses the `clear` command.

    :return: None
    """
    subprocess.call('cmd.exe /c cls' if os.name == "nt" else 'clear')


def about() -> None:
    """
    Prints the program's about information.

    :return: None
    """
    about_text = """
    OCTOSUITE © 2023 Richard Mwewa
    
    An advanced and lightning fast framework for gathering open-source intelligence on GitHub users and organisations.
    
    Read the wiki: https://github.com/bellingcat/octosuite/wiki
    GitHub REST API documentation: https://docs.github.com/rest
    """
    xprint(about_text)
