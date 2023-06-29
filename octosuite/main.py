from octosuite.octosuite import *
from octosuite.miscellaneous import path_finder, check_updates
from octosuite.config import setup_cli_completion, configure_logging, create_parser

setup_cli_completion()

parser = create_parser()
args = parser.parse_args()


def run() -> None:
    """
    Run the Octosuite application.

    This function initializes the Octosuite instance, sets up necessary paths, configures logging,
    checks for updates, and handles command line arguments and user input.

    :return: None
    """
    try:
        octosuite = Octosuite()
        path_finder([".logs", "output", "downloads"])
        configure_logging()
        check_updates()
        if args.method:
            """
            Iterate over the argument_map and check if the passed command line argument matches any argument in it
            [argument_map].
            If there's a match, execute its associated method.
            If no match is found, do nothing (which will return the usage).
            """
            for argument, method in octosuite.argument_map:
                if args.method == argument:
                    method(args)
                    print("\n")
                else:
                    pass
        else:
            """
            Main loop to keep Octosuite running. The loop will break if Octosuite detects a KeyboardInterrupt (Ctrl+C)
            or if the 'exit' command is entered.
            """
            while True:
                command_input = Prompt.ask(f"{getpass.getuser()}@:octopus: [blue]{os.getcwd()}[/]")
                """
                Iterate over the command_map and check if the user input matches any command in it [command_map].
                If there's a match, execute its associated method. If no match is found, ignore it.
                """
                if command_input[:2] == 'cd':
                    os.chdir(command_input[3:])
                elif command_input[:2] == 'ls':
                    list_files_and_directories(command_input[3:])
                else:
                    """
                    Execute the specified method based on the user input.
                    If no match is found, ignore it.
                    """
                    for command, method in octosuite.command_map:
                        if command_input == command:
                            method(args)
                        else:
                            pass

    except KeyboardInterrupt:
        logging.warning(message.ctrl_c())
        xprint(message.ctrl_c())

    except Exception as e:
        logging.error(message.error(e))
        xprint(message.error(e))
