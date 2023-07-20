import os
import functools
from octosuite.helpers import Helper
from octosuite.messages import Message
from octosuite.managers import FileManager
from octosuite.octosuite import Octosuite, Prompt, xprint
from octosuite.miscellaneous import (
    about,
    check_updates,
    clear_screen,
    list_files_and_directories,
)


class Command:
    def __init__(self, args):
        """
        Command class constructor. Initialises command-line arguments, command_map, argument_map,
        and Helper, Octosuite and FileManager classes.
        """
        self.__args = args

        # Initialise the Helper instance.
        __helper = Helper()

        # Initialise the Octosuite instance.
        __octosuite = Octosuite()

        # Initialise the FileManager instance.
        __file_management = FileManager()

        # Mapping commands to their corresponding methods.
        # And using functools.partial to map methods that require an argument (args).
        self.command_map = {
            "exit": __octosuite.exit_session,
            "clear": clear_screen,
            "about": about,
            "help": __helper.help_command,
            "update": check_updates,
            "help:search": __helper.search_help_command_table,
            "help:user": __helper.user_help_command_table,
            "help:repo": __helper.repo_help_command_table,
            "help:logs": __helper.logs_help_command_table,
            "help:csv": __helper.csv_help_command_table,
            "help:org": __helper.org_help_command_table,
            "org:events": functools.partial(__octosuite.get_organisation_events, args),
            "org:profile": functools.partial(
                __octosuite.get_organisation_profile, args
            ),
            "org:repos": functools.partial(
                __octosuite.get_organisation_repositories, args
            ),
            "org:member": functools.partial(__octosuite.is_organisation_member, args),
            "repo:path_contents": functools.partial(
                __octosuite.get_repository_path_contents, args
            ),
            "repo:profile": functools.partial(__octosuite.get_repository_profile, args),
            "repo:contributors": functools.partial(
                __octosuite.get_repository_contributors, args
            ),
            "repo:stargazers": functools.partial(
                __octosuite.get_repository_stargazers, args
            ),
            "repo:forks": functools.partial(__octosuite.get_repository_forks, args),
            "repo:issues": functools.partial(__octosuite.get_repository_issues, args),
            "repo:releases": functools.partial(
                __octosuite.get_repository_releases, args
            ),
            "user:email": functools.partial(__octosuite.get_user_email, args),
            "user:repos": functools.partial(__octosuite.get_user_repositories, args),
            "user:gists": functools.partial(__octosuite.get_user_gists, args),
            "user:orgs": functools.partial(__octosuite.get_user_organisations, args),
            "user:profile": functools.partial(__octosuite.get_user_profile, args),
            "user:events": functools.partial(__octosuite.get_user_events, args),
            "user:followers": functools.partial(__octosuite.get_user_followers, args),
            "user:follows": functools.partial(__octosuite.check_if_user_follows, args),
            "user:following": functools.partial(__octosuite.get_user_following, args),
            "user:subscriptions": functools.partial(
                __octosuite.get_user_subscriptions, args
            ),
            "search:users": functools.partial(__octosuite.search_users, args),
            "search:repos": functools.partial(__octosuite.search_repositories, args),
            "search:topics": functools.partial(__octosuite.search_topics, args),
            "search:issues": functools.partial(__octosuite.search_issues, args),
            "search:commits": functools.partial(__octosuite.search_commits, args),
            "logs:view": __file_management.view_log_files,
            "logs:read": functools.partial(__file_management.read_log_file, args),
            "logs:delete": functools.partial(__file_management.delete_log_file, args),
            "logs:clear": __file_management.clear_log_files,
            "csv:view": __file_management.view_csv_files,
            "csv:read": functools.partial(__file_management.read_csv_file, args),
            "csv:delete": functools.partial(__file_management.delete_csv_file, args),
            "csv:clear": __file_management.clear_csv_files,
        }

        # Mapping command-line arguments to their corresponding methods.
        self.argument_map = {
            "user-profile": functools.partial(__octosuite.get_user_profile, args),
            "user-email": functools.partial(__octosuite.get_user_email, args),
            "user-repos": functools.partial(__octosuite.get_user_repositories, args),
            "user-gists": functools.partial(__octosuite.get_user_gists, args),
            "user-orgs": functools.partial(__octosuite.get_user_organisations, args),
            "user-events": functools.partial(__octosuite.get_user_events, args),
            "user-subscriptions": functools.partial(
                __octosuite.get_user_subscriptions, args
            ),
            "user-following": functools.partial(__octosuite.get_user_following, args),
            "user-followers": functools.partial(__octosuite.get_user_followers, args),
            "user-follows": functools.partial(__octosuite.check_if_user_follows, args),
            "users-search": functools.partial(__octosuite.search_users, args),
            "issues-search": functools.partial(__octosuite.search_issues, args),
            "commits-search": functools.partial(__octosuite.search_commits, args),
            "topics-search": functools.partial(__octosuite.search_topics, args),
            "repos-search": functools.partial(__octosuite.search_repositories, args),
            "org-profile": functools.partial(
                __octosuite.get_organisation_profile, args
            ),
            "org-repos": functools.partial(
                __octosuite.get_organisation_repositories, args
            ),
            "org-events": functools.partial(__octosuite.get_organisation_events, args),
            "is-org-member": functools.partial(
                __octosuite.is_organisation_member, args
            ),
            "repo-profile": functools.partial(__octosuite.get_repository_profile, args),
            "repo-contributors": functools.partial(
                __octosuite.get_repository_contributors, args
            ),
            "repo-stargazers": functools.partial(
                __octosuite.get_repository_stargazers, args
            ),
            "repo-forks": functools.partial(__octosuite.get_repository_forks, args),
            "repo-issues": functools.partial(__octosuite.get_repository_issues, args),
            "repo-releases": functools.partial(
                __octosuite.get_repository_releases, args
            ),
            "repo-path-contents": functools.partial(
                __octosuite.get_repository_path_contents, args
            ),
            "view-logs": __file_management.view_log_files,
            "read-log": functools.partial(__file_management.read_log_file, args),
            "delete-log": functools.partial(__file_management.delete_log_file, args),
            "clear-logs": __file_management.clear_log_files,
            "view-csv": __file_management.view_csv_files,
            "read-csv": functools.partial(__file_management.read_csv_file, args),
            "delete-csv": functools.partial(__file_management.delete_csv_file, args),
            "clear-csv": __file_management.clear_csv_files,
            "about": about,
        }

    def execute_commands(self):
        """
        Executes the given command and calls its corresponding method.
        """
        # Initialise the Message instance.
        message = Message()

        while True:
            # Prompt user to enter a command.
            command = Prompt.ask(message.command_prompt())

            # Move to the specified directory if the `cd` command is entered.
            if command[:2] == "cd":
                os.chdir(command[3:])

            # List files and directories in the specified or current directory.
            elif command[:2] == "ls":
                list_files_and_directories(command[3:])

            # Check if the user-specified command is present in the command map and call its corresponding method.
            elif command in self.command_map:
                self.command_map.get(command)()
            else:
                # Print an `Unknown command` message if an invalid command is entered.
                xprint(message.unknown_command(command=command))

    def execute_command_line_args(self):
        """
        Executes the given command-line argument and calls its corresponding method.
        If none is passed, print the usage.
        """
        from octosuite.config import usage

        if self.__args.initialise:
            # Call the corresponding method for the given command-line argument.
            self.argument_map.get(self.__args.initialise)()
        else:
            # Print the usage if an invalid command-line argument/option is passed.
            xprint(usage())
