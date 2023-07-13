import platform
from octosuite.octosuite import xprint
from octosuite.commands import Command
from octosuite.messages import Message
from octosuite.miscellaneous import path_finder, check_updates
from octosuite.config import setup_cli_completion, setup_activity_logging, create_parser, \
    LOGS_DIRECTORY, OUTPUT_DIRECTORY, CURRENT_USERNAME


class Run:
    def __init__(self, cli_mode: bool):
        """
        Run class constructor. Initializes parser, command, sets up directories and checks for updates.
        
        :param cli_mode: Boolean flag to indicate whether the program is running in CLI mode.
        """
        self.cli_mode = cli_mode
        self.parser = create_parser()
        args = self.parser.parse_args()
        self.command = Command(args=args)
        
        # Set up the logs and output directories.
        path_finder(directories=[LOGS_DIRECTORY, OUTPUT_DIRECTORY])
        
        # Check for latest program updates.
        check_updates()
        
    def __call__(self):
        """
        Makes the Run instance callable. Sets up command completion and handles
        session logging and command execution based on the mode.
        """
        # Initialise the Message instance
        message = Message()

        # Set-up command completion
        setup_cli_completion()

        log = setup_activity_logging()
        # Log the start of a new session.
        log.info(message.session_opened(platform.node(), CURRENT_USERNAME))
        try:
            if self.cli_mode:
                # If in CLI mode, execute command line args
                self.command.execute_command_line_args()
            else:
                # If not in CLI mode, execute commands
                self.command.execute_commands()

        except KeyboardInterrupt:
            # Log warning if program is interrupted
            log.warning(message.ctrl_c())
            xprint(message.ctrl_c())
        except Exception as e:
            # Log any other exceptions that occur
            log.error(message.error_occurred(exception=str(e)))
            xprint(message.error_occurred(exception=str(e)))


def run_octosuite_cli():
    """
    Function for running the program in CLI mode. Creates an instance of Run
    in CLI mode and runs it.
    """
    Run(cli_mode=True)()


def run_octosuite_no_cli():
    """
    Function for running the program in non-CLI mode. Creates an instance of Run
    in non-CLI mode and runs it.
    """
    Run(cli_mode=False)()
