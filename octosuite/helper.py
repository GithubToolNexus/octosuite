from rich import print as xprint
from octosuite.config import create_table


def search_help_command_table() -> None:
    """
    Display a table with search subcommands.
    The table includes the available commands and their descriptions.

    :return: None
    """
    table = create_table(table_title=":magnifying_glass_tilted_left:Target Discovery" 
                                     "\ncommand syntax: `search:<subcommand>`",
                         column_headers=["Command", "Description"],
                         table_data=[("commits", "Search commits"),
                                     ("issues", "Search issues"),
                                     ("repos", "Search repositories"),
                                     ("topics", "Search topics"),
                                     ("users", "Search users")
                                     ])
    xprint(table)


def user_help_command_table() -> None:
    """
    Display a table with user subcommands.
    The table includes the available commands and their descriptions.

    :return: None
    """
    table = create_table(table_title=":bust_in_silhouette:User Investigation\ncommand syntax: `user:<subcommand>`",
                         column_headers=["Command", "Description"],
                         table_data=[("email", "Get a user's email"),
                                     ("events", "Get a user's events"),
                                     ("followers", "Get a user's followers"),
                                     ("following", "Get a list of users the target user is following"),
                                     ("follows", "Check if target user follows the specified user"),
                                     ("gists", "Get a user's gists (shared code snippets)"),
                                     ("orgs", "Get organisations that the target user follows/owns"),
                                     ("profile", "Get a user's profile information"),
                                     ("repos", "Get a user's repositories"),
                                     ("subscriptions", "Get a user's subscriptions (starred repositories)")
                                     ])
    xprint(table)


def org_help_command_table() -> None:
    """
    Display a table with org subcommands.
    The table includes the available commands and their descriptions.

    :return: None
    """
    table = create_table(table_title=":office_building:Organisation Investigation\n" 
                                     "command syntax: `org:<subcommand>`",
                         column_headers=["Command", "Description"],
                         table_data=[("events", "Get an organisation;s events"),
                                     ("member", "Check if a specified user is a "
                                                "public member of the target organisation"),
                                     ("profile", "Get an organisation's profile information"),
                                     ("repos", "Get an organisation's repositories"),
                                     ])
    xprint(table)


def repo_help_command_table() -> None:
    """
    Display a table with repo subcommands.
    The table includes the available commands and their descriptions.

    :return: None
    """
    table = create_table(table_title=":file_cabinet:Repository Investigation\n"
                                     "command syntax: `repo:<subcommand>`",
                         column_headers=["Command", "Description"],
                         table_data=[("contributors", "Get a repository's contributors"),
                                     ("forks", "Get a repository's forks"),
                                     ("issues", "Get a repository's issues"),
                                     ("path_contents", "Get contents of a specified path from the target repository"),
                                     ("profile", "Get a repository's profile information"),
                                     ("releases", "Get a repository's releases"),
                                     ("stargazers", "Get a repository's stargazers "
                                                    "(users that have starred the target repository)")])
    xprint(table)


def logs_help_command_table() -> None:
    """
    Display a table with logs subcommands.
    The table includes the available commands and their descriptions.

    :return: None
    """
    table = create_table(table_title=":spiral_note_pad:Logs Management\n"
                                     "command syntax: `logs:<subcommand>`",
                         column_headers=["Command", "Description"],
                         table_data=[("clear", "Clear/Delete all logs"),
                                     ("delete", "Delete a specified log file"),
                                     ("read", "Read a specified log file"),
                                     ("view", "View all generated log files")
                                     ])
    xprint(table)


def csv_help_command_table() -> None:
    """
    Display a table with logs subcommands.
    The table includes the available commands and their descriptions.

    :return: None
    """
    table = create_table(table_title=":page_facing_up:CSV File Management\n"
                                     "command syntax: `csv:<subcommand>`",
                         column_headers=["Command", "Description"],
                         table_data=[("clear", "Clear/Delete all csv files"),
                                     ("delete", "Delete a specified csvfile"),
                                     ("read", "Read a specified csv file"),
                                     ("view", "View all generated csv files")
                                     ])
    xprint(table)


def help_command() -> None:
    """
    Display a table with basic commands and help subcommands.
    The table includes the available commands and their descriptions.

    :return: None
    """
    basic_commands_table = create_table(table_title=":information:Basic Commands",
                                        column_headers=["Command", "Description"],
                                        table_data=[("about", "About Octosuite"),
                                                    ("author", "Show developer's information"),
                                                    ("cd", "Move to the specified directory"),
                                                    ("clear", "Clear screen"),
                                                    ("exit", "Exit/Close session"),
                                                    ("help", "Show this help menu"),
                                                    ("ls", "List contents of the specified directory "
                                                           "(shows contents of the current directory "
                                                           "if directory name is  not specified)")])
    help_sub_commands = create_table(table_title=":white_question_mark:Investigation & Management Commands\n"
                                                 "command syntax: help:<subcommand>",
                                     column_headers=["Command", "Description"],
                                     table_data=[("csv", "List all csv management commands"),
                                                 ("logs", "List all logs management commands"),
                                                 ("org", "List all organisation investigation commands"),
                                                 ("repo", "List all repository investigation commands"),
                                                 ("search", "List all target discovery commands"),
                                                 ("user", "List all user investigation commands")])
    xprint(basic_commands_table)
    xprint(help_sub_commands)
