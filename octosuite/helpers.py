from rich import print as xprint


class Helper:
    def __init__(self):
        from octosuite.config import create_table, Emojis
        """
        Helper class constructor. Imports and initialises emojis and table (create_table).
        """
        self.__emoji = Emojis()
        self.__create_table = create_table

    def search_help_command_table(self):
        """
        Display a table with search subcommands.
        The table includes the available commands and their descriptions.

        :return: None
        """
        table = self.__create_table(table_title="Target Discovery"
                                                "\ncommand syntax: `search:<subcommand>`",
                                    column_headers=["#", "Command", "Description"],
                                    table_data=[(self.__emoji.RIGHT_ARROW, "commits", "Search commits"),
                                                (self.__emoji.EXCLAMATION_QUESTION_MARK, "issues", "Search issues"),
                                                (self.__emoji.FILE_CABINET, "repos", "Search repositories"),
                                                (self.__emoji.CHART_INCREASING, "topics", "Search topics"),
                                                (self.__emoji.BUSTS_IN_SILHOUETTE, "users", "Search users")
                                                ])
        xprint(table)

    def user_help_command_table(self):
        """
        Display a table with user subcommands.
        The table includes the available commands and their descriptions.
        """
        table = self.__create_table(
            table_title="User Investigation\ncommand syntax: `user:<subcommand>`",
            column_headers=["#", "Command", "Description"],
            table_data=[(self.__emoji.EMAIL, "email", "Get a user's email"),
                        (self.__emoji.WHITE_QUESTION_MARK, "events", "Get a user's events"),
                        (self.__emoji.BUSTS_IN_SILHOUETTE, "followers", "Get a user's followers"),
                        (self.__emoji.RIGHT_ARROW, "following", "Get a list of users the target user is following"),
                        (self.__emoji.RIGHT_ARROW_CURVING_LEFT,
                         "follows", "Check if target user follows the specified user"),
                        (self.__emoji.CARD_FILE_BOX, "gists", "Get a user's gists (shared code snippets)"),
                        (self.__emoji.OFFICE_BUILDING, "orgs", "Get organisations that the target user follows/owns"),
                        (self.__emoji.EXCLAMATION_MARK, "profile", "Get a user's profile information"),
                        (self.__emoji.FILE_CABINET, "repos", "Get a user's repositories"),
                        (
                            self.__emoji.GLOWING_STAR, "subscriptions",
                            "Get a user's subscriptions (starred repositories)")
                        ])
        xprint(table)

    def org_help_command_table(self):
        """
        Display a table with org subcommands.
        The table includes the available commands and their descriptions.
        """
        table = self.__create_table(table_title="Organisation Investigation\n"
                                                "command syntax: `org:<subcommand>`",
                                    column_headers=["#", "Command", "Description"],
                                    table_data=[(self.__emoji.WHITE_QUESTION_MARK, "events",
                                                 "Get an organisation;s events"),
                                                (self.__emoji.WHITE_QUESTION_MARK, "is_org_member",
                                                 "Check if a specified user is a "
                                                 "public member of the target organisation"),
                                                (self.__emoji.BUST_IN_SILHOUETTE, "profile",
                                                 "Get an organisation's profile information"),
                                                (self.__emoji.FILE_CABINET, "repos",
                                                 "Get an organisation's repositories"),
                                                ])
        xprint(table)

    def repo_help_command_table(self):
        """
        Display a table with repo subcommands.
        The table includes the available commands and their descriptions.
        """
        table = self.__create_table(table_title="Repository Investigation\n"
                                                "command syntax: `repo:<subcommand>`",
                                    column_headers=["#", "Command", "Description"],
                                    table_data=[(self.__emoji.BUSTS_IN_SILHOUETTE,
                                                 "contributors", "Get a repository's contributors"),
                                                (self.__emoji.FORK_AND_KNIFE, "forks", "Get a repository's forks"),
                                                (self.__emoji.EXCLAMATION_QUESTION_MARK, "issues",
                                                 "Get a repository's issues"),
                                                (self.__emoji.FILE_FOLDER, "path_contents",
                                                 "Get contents of a specified path from the target repository"),
                                                (self.__emoji.EXCLAMATION_MARK,
                                                 "profile", "Get a repository's profile information"),
                                                (self.__emoji.PACKAGE, "releases", "Get a repository's releases"),
                                                (self.__emoji.GLOWING_STAR, "stargazers",
                                                 "Get a repository's stargazers "
                                                 "(users that have starred the target repository)")])
        xprint(table)

    def logs_help_command_table(self):
        """
        Display a table with logs subcommands.
        The table includes the available commands and their descriptions.
        """
        table = self.__create_table(table_title="Logs Management\n"
                                                "command syntax: `logs:<subcommand>`",
                                    column_headers=["#", "Command", "Description"],
                                    table_data=[(self.__emoji.LITTER_IN_BIN, "clear", "Clear/Delete all logs"),
                                                (self.__emoji.WASTEBASKET, "delete", "Delete a specified log file"),
                                                (self.__emoji.OPEN_BOOK, "read", "Read a specified log file"),
                                                (self.__emoji.EYES, "view", "View all generated log files")
                                                ])
        xprint(table)

    def csv_help_command_table(self):
        """
        Display a table with logs subcommands.
        The table includes the available commands and their descriptions.
        """
        table = self.__create_table(table_title="CSV File Management\n"
                                                "command syntax: `csv:<subcommand>`",
                                    column_headers=["#", "Command", "Description"],
                                    table_data=[(self.__emoji.LITTER_IN_BIN, "clear", "Clear/Delete all csv files"),
                                                (self.__emoji.WASTEBASKET, "delete", "Delete a specified csvfile"),
                                                (self.__emoji.OPEN_BOOK, "read", "Read a specified csv file"),
                                                (self.__emoji.EYES, "view", "View all generated csv files")
                                                ])
        xprint(table)

    def help_command(self):
        """
        Display a table with basic commands and help subcommands.
        The table includes the available commands and their descriptions.
        """
        basic_commands_table = self.__create_table(table_title="Basic Commands",
                                                   column_headers=["#", "Command", "Description"],
                                                   table_data=[
                                                       (self.__emoji.WHITE_QUESTION_MARK, "about", "About Octosuite"),
                                                       (self.__emoji.FILE_FOLDER, "cd",
                                                        "Move to the specified directory"),
                                                       (self.__emoji.LITTER_IN_BIN, "clear", "Clear screen"),
                                                       (self.__emoji.NO_ENTRY, "exit", "Exit/Close session"),
                                                       (self.__emoji.WHITE_QUESTION_MARK, "help",
                                                        "Show this help menu"),
                                                       (self.__emoji.OPEN_FILE_FOLDER, "ls",
                                                        "List contents of the current/specified directory"),
                                                       (self.__emoji.UP_BUTTON, "update",
                                                        "Check for latest program releases/updates")])
        help_sub_commands = self.__create_table(table_title="Investigation & Management Commands\n"
                                                            "command syntax: help:<subcommand>",
                                                column_headers=["#", "Command", "Description"],
                                                table_data=[(self.__emoji.SPIRAL_NOTEPAD, "csv",
                                                             "List all csv management commands"),
                                                            (self.__emoji.NOTEBOOK, "logs",
                                                             "List all logs management commands"),
                                                            (self.__emoji.OFFICE_BUILDING, "org",
                                                             "List all organisation investigation commands"),
                                                            (self.__emoji.FILE_CABINET, "repo",
                                                             "List all repository investigation commands"),
                                                            (self.__emoji.MAGNIFYING_GLASS_LEFT, "search",
                                                             "List all target discovery commands"),
                                                            (self.__emoji.BUST_IN_SILHOUETTE, "user",
                                                             "List all user investigation commands")])
        xprint(basic_commands_table)
        xprint(help_sub_commands)
