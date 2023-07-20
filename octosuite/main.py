import time
from octosuite.octosuite import xprint
from octosuite.commands import Command
from octosuite.messages import Message
from octosuite.miscellaneous import clear_screen, path_finder, check_updates, systeminfo
from octosuite.config import (
    setup_cli_completion,
    setup_activity_logging,
    create_parser,
    LOGS_DIRECTORY,
    OUTPUT_DIRECTORY,
    CURRENT_USERNAME,
)


class Run:
    def __init__(self, cli_mode: bool):
        """
        Run class constructor. Initializes parser, command and sets up directories.

        :param cli_mode: Boolean flag to indicate whether the program is running in CLI mode.
        """
        self.cli_mode = cli_mode
        self.parser = create_parser()
        args = self.parser.parse_args()
        self.command = Command(args=args)

        # Set up the logs and output directories.
        path_finder(directories=[LOGS_DIRECTORY, OUTPUT_DIRECTORY])

        # Clear screen
        clear_screen()

    def __call__(self):
        """
        Makes the Run instance callable. Sets up command completion, initialises system information and handles
        session logging and command execution based on the mode.
        """
        # Initialise the Message instance
        message = Message()
        system_info = systeminfo()

        # Set-up command completion
        setup_cli_completion()

        # Set-up logging
        log = setup_activity_logging()

        # Log the start of a new session.
        log.info(
            message.session_opened(
                host=system_info["node"],
                username=CURRENT_USERNAME,
                timestamp=time.asctime(),
            )
        )

        # Log system information.
        log.info(message.system_os(os=system_info["os"]))
        log.info(message.system_ram(ram=system_info["ram"]))
        log.info(message.system_node(node=system_info["node"]))
        log.info(message.system_release(release=system_info["release"]))
        log.info(message.system_processor(processor=system_info["processor"]))
        log.info(message.system_architecture(architecture=system_info["architecture"]))

        # Print the start of a session.
        xprint(
            message.session_opened(
                host=system_info["node"],
                username=CURRENT_USERNAME,
                timestamp=time.asctime(),
            )
        )

        # Print system information
        xprint(message.system_os(os=system_info["os"]))
        xprint(message.system_ram(ram=system_info["ram"]))
        xprint(message.system_node(node=system_info["node"]))
        xprint(message.system_release(release=system_info["release"]))
        xprint(message.system_processor(processor=system_info["processor"]))
        xprint(message.system_architecture(architecture=system_info["architecture"]))

        try:
            if self.cli_mode:
                # Check for updates
                check_updates()

                # If in CLI mode, execute command line args
                self.command.execute_command_line_args()
            else:
                # If not in CLI mode, execute commands
                self.command.execute_commands()

        except KeyboardInterrupt:
            # Log/print warning if program is interrupted
            log.warning(message.ctrl_c())
            xprint(message.ctrl_c())
        except Exception as error:
            # Log/print any other exceptions that occur
            log.error(message.error_occurred(exception=str(error)))
            xprint(message.error_occurred(exception=str(error)))


def octosuite_cli():
    """
    Function for running the program in CLI mode. Creates an instance of Run
    in CLI mode and runs it.
    """
    Run(cli_mode=True)()


def octosuite_non_cli():
    """
    Function for running the program in non-CLI mode. Creates an instance of Run
    in non-CLI mode and runs it.
    """
    Run(cli_mode=False)()
