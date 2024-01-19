# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

import os
from datetime import datetime
from typing import Union, Literal

import pandas as pd
from rich.console import Console

from .data import Account, User, Organisation, Repository, Event, Org, Gist


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def pathfinder(directories: list[str]):
    """
    Creates directories in knewkarma-data directory of the user's home folder.

    :param directories: A list of file directories to create.
    :type directories: list[str]
    """
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def filename_timestamp() -> str:
    """
    Generates a timestamp string suitable for file naming, based on the current date and time.
    The format of the timestamp is adapted based on the operating system.

    :return: The formatted timestamp as a string. The format is "%d-%B-%Y-%I-%M-%S%p" for Windows
             and "%d-%B-%Y-%I:%M:%S%p" for non-Windows systems.
    :rtype: str

    Example
    -------
    - Windows: "20-July-1969-08-17-45PM"
    - Non-Windows: "20-July-1969-08:17:45PM" (format may vary based on the current date and time)
    """
    now = datetime.now()
    return (
        now.strftime("%d-%B-%Y-%I-%M-%S%p")
        if os.name == "nt"
        else now.strftime("%d-%B-%Y-%I:%M:%S%p")
    )


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def create_dataframe(
    data: Union[
        str,
        dict,
        list,
        list[Union[Account, Org, Repository, Event, Gist]],
        User,
        Repository,
        Organisation,
    ],
):
    """
    Converts and prints provided data into a pandas DataFrame and optionally saves it as JSON or CSV file.

    :param data: Data to be converted. Can be a single object (Community, User, WikiPage),
                 a dictionary, or a list of objects (Comment, Community, Post, PreviewCommunity, User).
    :type data: Union[Community, Dict, User, WikiPage, List[Union[Comment, Community, Post, PreviewCommunity, User]]]
    :return: A pandas DataFrame constructed from the provided data. Excludes any 'raw_data'
             column from the dataframe.
    :rtype: pd.DataFrame

    Note
    ----
        This function internally converts User, Community, and WikiPage objects into a
        list of dictionaries before DataFrame creation.
        For lists containing Comment, Community, Post, PreviewCommunity and User objects,
        each object is converted to its dictionary representation.
    """

    # ---------------------------------------------------------------------------------- #

    if isinstance(data, (User, Repository, Organisation)):
        # Transform each attribute of the object into a dictionary entry
        data = [{"key": key, "value": value} for key, value in data.__dict__.items()]

    elif isinstance(data, list) and all(
        isinstance(item, (Account, Event, Gist, Repository, Org)) for item in data
    ):
        # Each object in the list is converted to its dictionary representation
        data = [item.__dict__ for item in data]

    # If data is already a dictionary or a list, use it directly for DataFrame creation
    elif isinstance(data, (dict, list)):
        # No transformation needed; the data is ready for DataFrame creation
        pass

    # If data is a string, print it
    elif isinstance(data, str):
        console.log(data)
        return

    # Set pandas display option to show all rows
    pd.set_option("display.max_rows", None)

    # Create a DataFrame from the processed data
    dataframe = pd.DataFrame(data)

    return dataframe


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def export_dataframe(
    dataframe: pd.DataFrame,
    filename: str,
    directory: str,
    formats: list[Literal["csv", "html", "json", "xml"]],
):
    """
    Exports a pandas dataframe to the specified file types.

    :param dataframe: Pandas dataframe to export.
    :type dataframe: pandas.DataFrame
    :param filename: A name for the exported files.
    :type filename: str
    :param directory: Directory to which exported files will be saved.
    :type directory: str
    :param formats: List of file formats in which the dataframe will be exported.
    :type formats: list[Literal]
    """
    file_mapping: dict = {
        "csv": lambda: dataframe.to_csv(
            os.path.join(directory, "csv", f"{filename}.csv"), encoding="utf-8"
        ),
        "html": lambda: dataframe.to_html(
            os.path.join(directory, "html", f"{filename}.html"),
            escape=False,
            encoding="utf-8",
        ),
        "json": lambda: dataframe.to_json(
            os.path.join(directory, "json", f"{filename}.json"),
            encoding="utf-8",
            orient="records",
            lines=True,
            force_ascii=False,
            indent=4,
        ),
        "xml": lambda: dataframe.to_xml(
            os.path.join(directory, "xml", f"{filename}.xml"), parser="etree"
        ),
    }

    for file_format in formats:
        if file_format in file_mapping:
            filepath: str = os.path.join(
                directory, file_format, f"{filename}.{file_format}"
            )
            file_mapping.get(file_format)()
            console.log(
                f"{os.path.getsize(filepath)} bytes written to [link file://{filepath}]{filepath}"
            )
        else:
            console.log(f"Unsupported file format: {file_format}")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

console = Console(color_system="auto", log_time_format="[%I:%M:%S%p]")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
