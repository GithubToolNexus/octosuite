class Messages:
    @staticmethod
    def ctrl_c() -> str:
        """
        Returns the message for session termination with Ctrl+C.
        
        :return: Message string
        """
        return "Session terminated with Ctrl+C."

    @staticmethod
    def error(exception: str) -> str:
        """
        Returns the error message with the provided exception.

        :param exception: Raised exception
        :return: Message string
        """
        return f"An error occurred: {exception}"

    @staticmethod
    def session_opened(host: str, username: str) -> str:
        """
        Returns the message for opening a new session with the given host and username.

        :param host: System hostname
        :param username: Current user's login name
        :return: Message string
        """
        return f"Opened new session on {host}:{username}"

    @staticmethod
    def session_closed(timestamp: str) -> str:
        """
        Returns the message for session closure at the provided timestamp.

        :param timestamp: Current date and time
        :return: Message string
        """
        return f"Session closed at {timestamp}."

    @staticmethod
    def viewing_logs() -> str:
        """
        Returns the message for viewing logs.
        
        :return: Message string
        """
        return "Viewing logs..."

    @staticmethod
    def viewing_csv() -> str:
        """
        Returns the message for viewing CSV files.
        
        :return: Message string
        """
        return "Viewing CSV files..."

    @staticmethod
    def deleted(filename: str) -> str:
        """
        Returns the message for file deletion with the given filename.

        :param filename: File to delete
        :return: Message string
        """
        return f"Deleted: {filename}"

    @staticmethod
    def reading(filename: str) -> str:
        """
        Returns the message for reading a file with the given filename.

        :param filename: File to read
        :return: Message string
        """
        return f"Reading: {filename}"

    @staticmethod
    def information_not_found(param1: str, param2: str, param3: str) -> str:
        """
        Returns the message for information not found with the provided parameters.

        :param param1: First parameter
        :param param2: Second parameter
        :param param3: Third parameter
        :return: Message string
        """
        return f"Information Not Found: {param1}, {param2}, {param3}"

    @staticmethod
    def user_not_found(username: str) -> str:
        """
        Returns the message for user not found with the given username.

        :param username: Username
        :return: Message string
        """
        return f"User Not Found: @{username}"

    @staticmethod
    def org_not_found(org_name: str) -> str:
        """
        Returns the message for organisation not found with the given organisation name.

        :param org_name: Organisation name
        :return: Message string
        """
        return f"Organization Not Found: @{org_name}"

    @staticmethod
    def repo_or_user_not_found(repository: str, username: str) -> str:
        """
        Returns the message for repository or user not found with the provided parameters.

        :param repository: Repository name
        :param username: Username
        :return: Message string
        """
        return f"Repository/User Not Found: ({repository}, @{username})"

    @staticmethod
    def repo_does_not_have_stargazers(repository: str, username: str) -> str:
        """
        Returns the message for 'repository does not have stargazers' with the provided parameters.

        :param repository: Repository name
        :param username: Username
        :return: Message string
        """
        return f"Repository/User Not Found: ({repository}, @{username})"

    @staticmethod
    def prompt_log_csv() -> str:
        """Returns the message for prompting whether to log output to a CSV file."""
        return "Would you like to log this output to a .csv file?"

    @staticmethod
    def logged_to_csv(filename: str) -> str:
        """
        Returns the message confirming that output has been logged to a CSV file with the given filename.

        :param filename: File to save the output to
        :return: Message string
        """
        return f"Output logged: {filename}"

    @staticmethod
    def limit_output(title: str) -> str:
        """
        Returns the message for limiting output based on a user-defined value.

        :param title: A title of the information that is requested to be returned
        """
        return f"Limit '{title}' output to how many? (1-100)"
