import os
import functools
from octosuite.helpers import Helper
from octosuite.messages import Message
from octosuite.managers import FileManager
from octosuite.octosuite import Octosuite, Prompt, xprint
from octosuite.miscellaneous import about, check_updates, clear_screen, list_files_and_directories


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
            "org:profile": functools.partial(__octosuite.get_organisation_profile, args),
            "org:repos": functools.partial(__octosuite.get_organisation_repositories, args),
            "org:member": functools.partial(__octosuite.is_organisation_member, args),
            "repo:path_contents": functools.partial(__octosuite.get_repository_path_contents, args),
            "repo:profile": functools.partial(__octosuite.get_repository_profile, args),
            "repo:contributors": functools.partial(__octosuite.get_repository_contributors, args),
            "repo:stargazers": functools.partial(__octosuite.get_repository_stargazers, args),
            "repo:forks": functools.partial(__octosuite.get_repository_forks, args),
            "repo:issues": functools.partial(__octosuite.get_repository_issues, args),
            "repo:releases": functools.partial(__octosuite.get_repository_releases, args),
            "user:email": functools.partial(__octosuite.get_user_email, args),
            "user:repos": functools.partial(__octosuite.get_user_repositories, args),
            "user:gists": functools.partial(__octosuite.get_user_gists, args),
            "user:orgs": functools.partial(__octosuite.get_user_organisations, args),
            "user:profile": functools.partial(__octosuite.get_user_profile, args),
            "user:events": functools.partial(__octosuite.get_user_events, args),
            "user:followers": functools.partial(__octosuite.get_user_followers, args),
            "user:follows": functools.partial(__octosuite.check_if_user_follows, args),
            "user:following": functools.partial(__octosuite.get_user_following, args),
            "user:subscriptions": functools.partial(__octosuite.get_user_subscriptions, args),
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
            "csv:clear": __file_management.clear_csv_files
        }

        # Mapping command-line arguments to their corresponding methods.
        self.argument_map = {
            "user_profile": functools.partial(__octosuite.get_user_profile, args),
            "user_email": functools.partial(__octosuite.get_user_email, args),
            "user_repos": functools.partial(__octosuite.get_user_repositories, args),
            "user_gists": functools.partial(__octosuite.get_user_gists, args),
            "user_orgs": functools.partial(__octosuite.get_user_organisations, args),
            "user_events": functools.partial(__octosuite.get_user_events, args),
            "user_subscriptions": functools.partial(__octosuite.get_user_subscriptions, args),
            "user_following": functools.partial(__octosuite.get_user_following, args),
            "user_followers": functools.partial(__octosuite.get_user_followers, args),
            "user_follows": functools.partial(__octosuite.check_if_user_follows, args),
            "users_search": functools.partial(__octosuite.search_users, args),
            "issues_search": functools.partial(__octosuite.search_issues, args),
            "commits_search": functools.partial(__octosuite.search_commits, args),
            "topics_search": functools.partial(__octosuite.search_topics, args),
            "repos_search": functools.partial(__octosuite.search_repositories, args),
            "org_profile": functools.partial(__octosuite.get_organisation_profile, args),
            "org_repos": functools.partial(__octosuite.get_organisation_repositories, args),
            "org_events": functools.partial(__octosuite.get_organisation_events, args),
            "is_org_member": functools.partial(__octosuite.is_organisation_member, args),
            "repo_profile": functools.partial(__octosuite.get_repository_profile, args),
            "repo_contributors": functools.partial(__octosuite.get_repository_contributors, args),
            "repo_stargazers": functools.partial(__octosuite.get_repository_stargazers, args),
            "repo_forks": functools.partial(__octosuite.get_repository_forks, args),
            "repo_issues": functools.partial(__octosuite.get_repository_issues, args),
            "repo_releases": functools.partial(__octosuite.get_repository_releases, args),
            "repo_path_contents": functools.partial(__octosuite.get_repository_path_contents, args),
            "view_logs": __file_management.view_log_files,
            "read_log": functools.partial(__file_management.read_log_file, args),
            "delete_log": functools.partial(__file_management.delete_log_file, args),
            "clear_logs": __file_management.clear_log_files,
            "view_csv": __file_management.view_csv_files,
            "read_csv": functools.partial(__file_management.read_csv_file, args),
            "delete_csv": functools.partial(__file_management.delete_csv_file, args),
            "clear_csv": __file_management.clear_csv_files,
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
            if command[:2] == 'cd':
                os.chdir(command[3:])

            # List files and directories in the specified or current directory.
            elif command[:2] == 'ls':
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

        if self.__args.method:
            # Call the corresponding method for the given command-line argument.
            self.argument_map.get(self.__args.method)()
        else:
            # Print the usage if an invalid command-line argument/option is passed.
            xprint(usage())
