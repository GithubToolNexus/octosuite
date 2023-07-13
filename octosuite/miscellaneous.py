import os
import psutil
import platform
import requests
import subprocess
from rich import print as xprint
from rich.markdown import Markdown
from octosuite.config import Version
from octosuite.messages import Message

__message = Message()
__version = Version()


def path_finder(directories: list):
    """
    Checks if the specified directories exist.
    If not, it creates them.

    :param directories: List of directories to check and create
    :return: None
    """

    for directory in directories:
        # Construct and create each directory from the directories list if it doesn't already exist
        os.makedirs(directory, exist_ok=True)


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


def send_request(endpoint: str, authentication=None) -> tuple:
    """
    Sends a GET request to the specified endpoint and returns the status code and JSON response.

    :param endpoint: URL endpoint to send the request to
    :param authentication: Authentication information for the request.
    :return: Tuple containing the status code (int) and response data (dict)
    """
    from octosuite.config import setup_activity_logging

    log = setup_activity_logging()
    try:
        with requests.get(endpoint, auth=authentication,
                          headers={"Accept": "application/vnd.github.v3+json"}) as response:
            if authentication:
                response_data = response.text
            else:
                response_data = response.json()
            status_code = response.status_code

        return status_code, response_data
    except Exception as e:
        log.error(__message.error_occurred(exception=str(e)))
        xprint(__message.error_occurred(exception=str(e)))


def list_files_and_directories(directory: str = None):
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


def check_updates():
    """
    Check for updates to Octosuite.

    This function queries the GitHub API to check for the latest release of Octosuite.
    If an update is available, it retrieves the release notes and returns them as markdown.

    :return: None
    """

    response = send_request("https://api.github.com/repos/bellingcat/octosuite/releases/latest")
    if response[1]['tag_name'] == __version.full_version():
        pass
    else:
        raw_release_notes = response[1]['body']
        markdown_release_notes = Markdown(raw_release_notes)
        xprint(__message.update_found(version_tag=response[1]['tag_name']))
        xprint(markdown_release_notes)
        xprint(f"\nRun `{__message.colour.GREEN}pip install --upgrade "
               f"octosuite{__message.colour.RESET}` to install the updates.")


def clear_screen():
    """
    Clears the screen with `cls` command if system is Windows.
    Otherwise, uses the `clear` command.

    :return: None
    """
    subprocess.call('cmd.exe /c cls' if os.name == "nt" else 'clear')


def about():
    """
    Prints the program's about information.

    :return: None
    """
    about_text = """
    OCTOSUITE/OCTOSUITE-CLI © 2022-2023 Richard Mwewa
    
    An all-in-one framework for gathering open-source intelligence on GitHub users and organisations.
    
    GNU General Public License v3 (GPLv3)
    Read the wiki: https://github.com/bellingcat/octosuite/wiki
    GitHub REST API documentation: https://docs.github.com/rest
    """
    xprint(about_text)
