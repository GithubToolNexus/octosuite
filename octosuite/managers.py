import os
import shutil
from rich.text import Text
from rich.table import Table
from rich import print as xprint
from octosuite.octosuite import Prompt


class FileManager:
    def __init__(self):
        from octosuite.messages import Message
        from octosuite.config import setup_activity_logging, OUTPUT_DIRECTORY, LOGS_DIRECTORY
        
        self.__message = Message()
        self.__colour = self.__message.colour
        self.__OUTPUT_DIRECTORY = OUTPUT_DIRECTORY
        self.__LOGS_DIRECTORY = LOGS_DIRECTORY
        self.__log = setup_activity_logging()

    def delete_csv_file(self, args):
        csv_file = args.csv_file or Prompt.ask("-> .csv (filename)")

        file_path = os.path.join(self.__OUTPUT_DIRECTORY, csv_file)
        try:
            os.remove(file_path)
            self.__log.info(self.__message.file_deleted(filename=file_path))
            xprint(self.__message.file_deleted(filename=file_path))
        except OSError as e:
            xprint(f"{self.__message.unable_to_delete_file(filename=file_path)} -> "
                   f"{self.__colour.RED}{e}{self.__colour.RESET}")

    def clear_csv_files(self, args):
        csv_files_directory = self.__OUTPUT_DIRECTORY
        csv_files_count = len(os.listdir(csv_files_directory))
        clear_csv_prompt = args.clear_csv or Prompt.ask(self.__message.prompt_clear_files(csv_files_count))

        if clear_csv_prompt:
            try:
                shutil.rmtree(csv_files_directory)  # ignore_errors=True)
                self.__log.info(self.__message.files_cleared(csv_files_directory))
                xprint(self.__message.files_cleared(files_directory=csv_files_directory))
            except OSError as e:
                self.__log.error(f"{self.__message.unable_to_clear_files(files_directory=csv_files_directory)} -> {e}")
                xprint(f"{self.__message.unable_to_clear_files(files_directory=csv_files_directory)} -> "
                       f"{self.__colour.RED}{e}{self.__colour.RESET}")

    def view_csv_files(self):
        csv_files = os.listdir(self.__OUTPUT_DIRECTORY)

        csv_table = Table(show_header=True, header_style="bold white")
        csv_table.add_column("File", style="dim")
        csv_table.add_column("Size (bytes)")

        for csv_file in csv_files:
            csv_file_path = os.path.join(self.__OUTPUT_DIRECTORY, csv_file)
            csv_table.add_row(str(csv_file), str(os.path.getsize(csv_file_path)))
        xprint(csv_table)

    def read_csv_file(self, args):
        csv_file = args.csv_file or Prompt.ask("-> .csv (filename)")
        file_path = os.path.join(self.__OUTPUT_DIRECTORY, csv_file)

        try:
            with open(file_path, "r") as file:
                text = Text(file.read())
                xprint(text)
        except OSError as e:
            self.__log.error(f"{self.__message.unable_to_read_file(filename=file_path)} -> {e}")
            xprint(f"{self.__message.unable_to_read_file(filename=file_path)} -> "
                   f"{self.__colour.RED}{e}{self.__colour.RESET}")

    def read_log_file(self, args):
        log_file = args.csv_file or Prompt.ask("-> .log (filename)")
        file_path = os.path.join(self.__OUTPUT_DIRECTORY, log_file)

        try:
            with open(os.path.join(self.__LOGS_DIRECTORY, log_file), "r") as file:
                text = Text(file.read())
                xprint(text)
        except OSError as e:
            self.__log.error(f"{self.__message.unable_to_read_file(filename=file_path)} -> {e}")
            xprint(f"{self.__message.unable_to_read_file(filename=file_path)} -> "
                   f"{self.__colour.RED}{e}{self.__colour.RESET}")

    def delete_log_file(self, args):
        log_file = args.log_file or Prompt.ask("-> .log (filename)")
        file_path = os.path.join(self.__LOGS_DIRECTORY, log_file)

        try:
            os.remove(file_path)
            xprint(self.__message.file_deleted(filename=file_path))
            self.__log.info(self.__message.file_deleted(filename=file_path))
        except OSError as e:
            self.__log.error(f"{self.__message.unable_to_delete_file(filename=file_path)} -> {e}")
            xprint(f"{self.__message.unable_to_delete_file(filename=file_path)} -> "
                   f"{self.__colour.RED}{e}{self.__colour.RESET}")

    def clear_log_files(self, args):
        log_files_count = len(os.listdir(self.__LOGS_DIRECTORY))
        clear_logs_prompt = args.clear_log or Prompt.ask(self.__message.prompt_clear_files(files_count=log_files_count))

        if clear_logs_prompt:
            try:
                shutil.rmtree(self.__LOGS_DIRECTORY)  # ignore_errors=True)
                self.__log.info(self.__message.files_cleared(self.__LOGS_DIRECTORY))
                xprint(self.__message.files_cleared(files_directory=self.__LOGS_DIRECTORY))
            except OSError as e:
                self.__log.error(f"{self.__message.unable_to_clear_files(files_directory=self.__LOGS_DIRECTORY)} "
                                 f"-> {e}")
                xprint(f"{self.__message.unable_to_clear_files(files_directory=self.__LOGS_DIRECTORY)} -> "
                       f"{self.__colour.RED}{e}{self.__colour.RESET}")

    def view_log_files(self):
        log_files = os.listdir(self.__LOGS_DIRECTORY)

        logs_table = Table(show_header=True, header_style="bold white")
        logs_table.add_column("File", style="dim")
        logs_table.add_column("Size (bytes)")

        for log_file in log_files:
            log_file_path = os.path.join(self.__LOGS_DIRECTORY, log_file)
            logs_table.add_row(str(log_file), str(os.path.getsize(log_file_path)))
        xprint(logs_table)
