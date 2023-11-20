import json
import logging
import os

from rich.logging import RichHandler

from .parser import create_parser


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
                markup=True, log_time_format="%H:%M:%S", show_level=enable_debug
            )
        ],
    )
    return logging.getLogger(f"OctoSuite")


def data_broker(raw_data: dict, data_file: str) -> dict:
    """
    Formats API data based on a key mapping from a JSON file.

    :param raw_data: Dictionary containing raw data from the API.
    :param data_file: Path to the JSON file that contains the key mapping.

    :returns: A Formatted JSON object with human-readable keys.
    """

    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct path to the mapping data file
    mapping_data_file = os.path.join(current_dir, "data", data_file)

    # Load the mapping from the specified file
    with open(mapping_data_file, "r", encoding="utf-8") as file:
        mapping_data = json.load(file)

    # Initialize an empty dictionary to hold the formatted data
    formatted_data = {}

    # Map API data to human-readable format using the mapping
    for api_data_key, mapping_data_key in mapping_data.items():
        formatted_data[mapping_data_key] = raw_data.get(api_data_key, "N/A")

    return formatted_data


args = create_parser().parse_args()
log = setup_logging(enable_debug=args.debug)
