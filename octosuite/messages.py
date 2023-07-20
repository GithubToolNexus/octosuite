import os
import getpass


class Message:
    from octosuite.config import Colours, Emojis, create_parser

    colour = Colours(enable_colours=create_parser().parse_args().colours)

    def __init__(self):
        """
        Message class constructor. Initialises emojis.
        """
        self.__emoji = Message.Emojis()

    def ctrl_c(self) -> str:
        return f"{self.__emoji.STOP_SIGN} {Message.colour.YELLOW}Session terminated with Ctrl+C.{Message.colour.RESET}"

    def checking_updates(self) -> str:
        return (
            f"{self.__emoji.INFORMATION} {self.colour.WHITE}Checking for "
            f"latest releases/updates{self.colour.RESET} ..."
        )

    def update_found(self, version_tag: str) -> str:
        return (
            f"{self.__emoji.INFORMATION} {Message.colour.WHITE}Octosuite "
            f"{Message.colour.GREEN}v{version_tag}{Message.colour.WHITE}"
            f" is available.{Message.colour.RESET}"
        )

    def update_not_found(self, version_tag: str) -> str:
        return (
            f"{self.__emoji.GREEN_CHECK_MARK} {self.colour.WHITE}You're running the "
            f"latest release of Octosuite{self.colour.RESET} ({version_tag})."
        )

    def error_occurred(self, exception: str) -> str:
        return (
            f"{self.__emoji.NO_ENTRY} {Message.colour.WHITE}An error occurred:{Message.colour.RESET} "
            f"{Message.colour.RED}{exception}{Message.colour.RESET}"
        )

    def prompt_close_session(self) -> str:
        return (
            f"{self.__emoji.RED_QUESTION_MARK} {Message.colour.WHITE}"
            f"This will closed the current session. Continue?{Message.colour.RESET}"
        )

    def prompt_clear_files(self, files_count: int) -> str:
        return (
            f"{self.__emoji.RED_QUESTION_MARK} "
            f"{Message.colour.WHITE}This will clear all "
            f"{Message.colour.CYAN}{files_count}{Message.colour.WHITE} files. "
            f"Continue?{Message.colour.RESET}"
        )

    @staticmethod
    def command_prompt() -> str:
        import random

        prompt_emojis = [
            ":hamster:",
            ":wolf:",
            ":bear:",
            ":worm:",
            ":mammoth:",
            ":bison:",
            ":elephant:",
            ":rhinoceros:",
            ":two-hump_camel:",
            ":dromedary_camel:",
            ":leopard:",
            ":horse_face:",
            ":deer:",
            ":boar:",
            ":sheep:",
            ":shrimp:",
            ":ram:",
            ":goat:",
            ":camel:",
            ":kangaroo:",
            ":badger:",
            ":turkey:",
            ":peacock:",
            ":parrot:",
            ":swan:",
            ":owl:",
            ":troll:",
            ":flamingo:",
            ":crocodile:",
            ":tropical_fish:",
            ":blowfish:",
            ":lobster:",
            ":mosquito:",
            ":microbe:",
            ":bat:",
            ":bear_face:",
            ":fox_face:",
            ":hedgehog:",
            ":giraffe:",
            ":llama:",
            ":hippopotamus:",
            ":raccoon:",
            ":donkey:",
            ":jellyfish:",
            ":whale:",
            ":skunk:",
            ":kangaroo:",
            ":water_buffalo:",
            ":ox:",
            ":cow_face:",
            ":mouse:",
            ":rabbit:",
            ":turtle:",
            ":chipmunk:",
            ":beaver:",
            ":otter:",
            ":sloth:",
            ":oyster:",
        ]

        return f"{random.choice(prompt_emojis)} [bold]{getpass.getuser()}[/] {Message.colour.BLUE}~{os.getcwd()}{Message.colour.RESET}"

    def unknown_command(self, command: str) -> str:
        return (
            f"{self.__emoji.GREEN_CROSS_MARK} {Message.colour.WHITE}Unknown command{Message.colour.RESET}: "
            f"{Message.colour.GREEN}{command}{Message.colour.WHITE}."
            f" Enter {Message.colour.GREEN}help{Message.colour.WHITE} "
            f"for a list of available commands.{Message.colour.RESET}"
        )

    def session_opened(self, host: str, username: str, timestamp: str) -> str:
        return (
            f"{self.__emoji.GREEN_CHECK_MARK} "
            f"{Message.colour.WHITE}Opened new session on {username}@{host} at {Message.colour.RESET}{timestamp}"
        )

    def session_closed(self, timestamp: str) -> str:
        return (
            f"{self.__emoji.GREEN_CHECK_MARK} "
            f"{Message.colour.WHITE}Session closed at{Message.colour.RESET} {timestamp}."
        )

    def file_deleted(self, filename: str) -> str:
        return f"{self.__emoji.GREEN_CHECK_MARK} File deleted: {filename}"

    def files_cleared(self, files_directory: str) -> str:
        files = os.listdir(files_directory)
        return f"{self.__emoji.GREEN_CHECK_MARK} Files cleared successfully: {files}"

    def unable_to_clear_files(self, files_directory: str) -> str:
        files = os.listdir(files_directory)
        return f"{self.__emoji.GREEN_CROSS_MARK} Unable to clear files: {files}"

    def unable_to_delete_file(self, filename: str) -> str:
        return f"{self.__emoji.GREEN_CROSS_MARK} Unable to delete file: {filename}"

    def unable_to_read_file(self, filename: str) -> str:
        return f"{self.__emoji.GREEN_CROSS_MARK} Unable to delete file: {filename}"

    def information_not_found(self, param1: str, param2: str, param3: str) -> str:
        return (
            f"{self.__emoji.GREEN_CROSS_MARK} {Message.colour.GREEN}{param1}{Message.colour.WHITE} -> "
            f"{Message.colour.GREEN}{param2}{Message.colour.WHITE} -> "
            f"{Message.colour.GREEN}{param3}{Message.colour.WHITE}"
            f" (information) {Message.colour.RED}Not Found{Message.colour.RESET}"
        )

    def user_not_found(self, username: str) -> str:
        return (
            f"{self.__emoji.NO_ENTRY} @{Message.colour.GREEN}{username}{Message.colour.WHITE} (user) "
            f"{Message.colour.RED}Not Found{Message.colour.RESET}."
        )

    def org_not_found(self, organisation: str) -> str:
        return (
            f"{self.__emoji.NO_ENTRY} @{Message.colour.GREEN}{organisation}{Message.colour.WHITE} "
            f"(organisation) {Message.colour.RED}Not Found{Message.colour.RESET}."
        )

    def repo_or_user_not_found(self, repository: str, username: str) -> str:
        return (
            f"{self.__emoji.NO_ENTRY} {Message.colour.GREEN}{repository}{Message.colour.WHITE} -> "
            f"@{Message.colour.GREEN}{username}{Message.colour.WHITE} (repository/user) "
            f"{Message.colour.RED}Not Found{Message.colour.RESET}."
        )

    def repo_does_not_have(self, title: str, repository: str, username: str) -> str:
        return (
            f"{self.__emoji.NO_ENTRY} {Message.colour.GREEN}{repository}{Message.colour.WHITE} -> "
            f"@{Message.colour.GREEN}{username} {Message.colour.WHITE}Repository does not have "
            f"{title}.{Message.colour.RESET}"
        )

    def prompt_log_csv(self) -> str:
        return (
            f"{self.__emoji.WHITE_QUESTION_MARK} "
            f"{Message.colour.WHITE}Would you like to log this output to a .csv file?{Message.colour.RESET}"
        )

    def logged_to_csv(self, filename: str) -> str:
        return (
            f"{self.__emoji.GREEN_CHECK_MARK} {Message.colour.WHITE}Output logged:{Message.colour.RESET} "
            f"{Message.colour.GREEN}{filename}{Message.colour.RESET}"
        )

    def limit_output(self, title: str) -> str:
        return (
            f"{self.__emoji.WHITE_QUESTION_MARK} {Message.colour.WHITE}Limit{Message.colour.RESET} '{title}' "
            f"{Message.colour.WHITE}output to how many?{Message.colour.RESET} (1-100)"
        )

    def system_os(self, os: str) -> str:
        return f"{self.__emoji.COMPUTER_DISK} OS: {os}"

    def system_ram(self, ram: str) -> str:
        return f"{self.__emoji.COMPUTER} RAM: {ram}"

    def system_node(self, node: str) -> str:
        return f"{self.__emoji.COMPUTER} Node: {node}"

    def system_release(self, release: str) -> str:
        return f"{self.__emoji.COMPUTER_DISK} Release: {release}"

    def system_processor(self, processor: str) -> str:
        return f"{self.__emoji.COMPUTER} Processor: {processor}"

    def system_architecture(self, architecture: str) -> str:
        return f"{self.__emoji.COMPUTER} Architecture: {architecture}"
