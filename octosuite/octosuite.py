#!usr/bin/python
import argparse
import re
import os
import sys
import shutil
import logging
import getpass
import requests
import platform
import subprocess
from rich.tree import Tree
from datetime import datetime
from rich.prompt import Prompt, Confirm
from rich import print as xprint
from requests.auth import HTTPBasicAuth
from octosuite.attributes import Attributes
from octosuite.miscellaneous import send_request, clear_screen, list_files_and_directories, about
from octosuite.config import setup_cli_completion, Colours, Messages, Version
from octosuite.helper import help_command, search_help_command_table, user_help_command_table, repo_help_command_table, \
    org_help_command_table, logs_help_command_table, csv_help_command_table
from octosuite.csv_loggers import log_organisation_profile, log_user_profile, log_repo_profile, log_repo_path_contents, \
    log_repo_contributors, log_repo_stargazers, log_repo_forks, log_repo_issues, log_repo_releases, log_org_repos, \
    log_user_repos, log_user_gists, log_user_orgs, log_user_events, log_user_subscriptions, \
    log_user_following, log_user_followers, log_repos_search, log_users_search, log_topics_search, log_issues_search, \
    log_commits_search

attribute = Attributes()
colour = Colours()
message = Messages()



# Delete a specified csv file
def delete_csv():
    if args.csv_file:
        csv_file = args.csv_file
    else:
        csv_file = Prompt.ask(f"{green}.csv {white}(filename){reset}")
    os.remove(os.path.join("output", csv_file))
    logging.info(deleted.format(csv_file))
    xprint(f"{POSITIVE} {deleted.format(csv_file)}")


# Clear csv files
def clear_csv():
    clear_csv_prompt = Confirm.ask(f"{PROMPT} This will clear all {len(os.listdir('output'))} csv files, continue?")
    if clear_csv_prompt:
        shutil.rmtree('output', ignore_errors=True)
        xprint(f"{INFO} csv files cleared successfully!")
    else:
        pass


# View csv files
def view_csv():
    logging.info(viewing_csv)
    csv_files = os.listdir("output")
    csv_table = Table(show_header=True, header_style=header_title)
    csv_table.add_column("CSV", style="dim")
    csv_table.add_column("Size (bytes)")
    for csv_file in csv_files:
        csv_table.add_row(str(csv_file), str(os.path.getsize("output/" + csv_file)))
    xprint(csv_table)


# Read csv
def read_csv():
    if args.csv_file:
        csv_file = args.csv_file
    else:
        csv_file = Prompt.ask(f"{green}.csv {white}(filename){reset}")
    with open(os.path.join("output", csv_file), "r") as file:
        logging.info(reading.format(csv_file))
        text = Text(file.read())
        xprint(text)


# View logs
def view_logs():
    logging.info(viewing_logs)
    logs = os.listdir(".logs")
    logs_table = Table(show_header=True, header_style=header_title)
    logs_table.add_column("Log", style="dim")
    logs_table.add_column("Size (bytes)")
    for log in logs:
        logs_table.add_row(str(log), str(os.path.getsize(".logs/" + log)))
    xprint(logs_table)


# Read log
def read_log():
    if args.log_file:
        log_file = args.log_file
    else:
        log_file = Prompt.ask(f"{green}.log date{white} (eg. 2022-04-27 10:09:36AM){reset}")
    with open(os.path.join(".logs", log_file + ".log"), "r") as log:
        logging.info(reading.format(log_file))
        xprint("\n" + log.read())


# Delete log
def delete_log():
    if args.log_file:
        log_file = args.log_file
    else:
        log_file = Prompt.ask(f"{green}.log date{white} (eg. 2022-04-27 10:09:36AM){reset}")
    os.remove(os.path.join(".logs", log_file))
    logging.info(deleted.format(log_file))
    xprint(f"{POSITIVE} {deleted.format(log_file)}")


# Clear logs
def clear_logs():
    clear_logs_prompt = Confirm.ask(f"{PROMPT} This will clear all {len(os.listdir('output'))} log files and close the current session, continue?")
    if clear_logs_prompt:
        shutil.rmtree('.logs', ignore_errors=True)
        xprint(f"{INFO} .log files cleared successfully!")
        exit()
    else:
        pass


# Exit session
def exit_session():
    exit_prompt = Confirm.ask(f"{PROMPT} This will close the current session, continue?")
    if exit_prompt:
        logging.info(session_closed.format(datetime.now()))
        xprint(f"{INFO} {session_closed.format(datetime.now())}")
        exit()
    else:
        pass


def get_email_from_contributor(username: str, repository: str, contributor: str) -> str:
    """
    Get the email address of a contributor in a GitHub repository.

    :param username: GitHub username
    :param repository: GitHub repository name
    :param contributor: Contributor's username
    :return: Email address of the contributor (None if not found)

    https://github.com/s0md3v/Zen/blob/master/zen.py#L84-L105
    """
    commits_url = f"https://github.com/{username}/{repository}/commits?author={contributor}"
    response = requests.get(commits_url, auth=HTTPBasicAuth(username, '')).text
    latest_commit_match = re.search(rf'href="/{username}/{repository}/commit/(.*?)"', response)
    latest_commit = latest_commit_match.group(1) if latest_commit_match else 'dummy'
    commit_details_url = f"https://github.com/{username}/{repository}/commit/{latest_commit}.patch"
    commit_details = requests.get(commit_details_url, auth=HTTPBasicAuth(username, '')).text
    email_match = re.search(r'<(.*)>', commit_details)
    email = email_match.group(1) if email_match else None
    return email


def get_unforked_repositories(username: str) -> list:
    """
    Get a list of unforked repositories for a GitHub user.

    :param username: GitHub username
    :return: List of unforked repository names
    """
    repos_url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=pushed"
    response = requests.get(repos_url, auth=HTTPBasicAuth(username, '')).json()
    unforked_repositories = [repo['name'] for repo in response if not repo['fork']]
    return unforked_repositories


def get_user_email() -> None:
    """
    Prompt the user for a GitHub username and retrieve the email address for the user's latest commit.

    :return: None

    https://github.com/s0md3v/Zen/blob/master/zen.py#L107-L113
    """
    username = input("Username: ")
    repos = get_unforked_repositories(username)
    for repo in repos:
        email = get_email_from_contributor(username, repo, username)
        if email:
            xprint(f"{username}: {email}")
            break


class Octosuite:
    def __init__(self):
        # API endpoint
        self.endpoint = 'https://api.github.com'

        # A list of tuples mapping commands to their methods
        self.command_map = [("exit", exit_session),
                            ("clear", clear_screen),
                            ("about", about),
                            ("author", self.author),
                            ("help", help_command),
                            ("help:search", search_help_command_table),
                            ("help:user", user_help_command_table),
                            ("help:repo", repo_help_command_table),
                            ("help:logs", logs_help_command_table),
                            ("help:csv", csv_help_command_table),
                            ("help:org", org_help_command_table),
                            ("org:events", self.org_events),
                            ("org:profile", self.organisation_profile),
                            ("org:repos", self.org_repos),
                            ("org:member", self.org_member),
                            ("repo:path_contents", self.path_contents),
                            ("repo:profile", self.repository_profile),
                            ("repo:contributors", self.repository_contributors),
                            ("repo:stargazers", self.repo_stargazers),
                            ("repo:forks", self.repo_forks),
                            ("repo:issues", self.repo_issues),
                            ("repo:releases", self.repo_releases),
                            ("user:email", get_user_email),
                            ("user:repos", self.user_repos),
                            ("user:gists", self.user_gists),
                            ("user:orgs", self.user_orgs),
                            ("user:profile", self.user_profile),
                            ("user:events", self.user_events),
                            ("user:followers", self.user_followers),
                            ("user:follows", self.user_follows),
                            ("user:following", self.user_following),
                            ("user:subscriptions", self.user_subscriptions),
                            ("search:users", self.users_search),
                            ("search:repos", self.repos_search),
                            ("search:topics", self.topics_search),
                            ("search:issues", self.issues_search),
                            ("search:commits", self.commits_search),
                            ("logs:view", view_logs),
                            ("logs:read", read_log),
                            ("logs:delete", delete_log),
                            ("logs:clear", clear_logs),
                            ("csv:view", view_csv),
                            ("csv:read", read_csv),
                            ("csv:delete", delete_csv),
                            ("csv:clear", clear_csv)]

        # Arguments map will be used to run Octosuite with command-line arguments/options
        self.argument_map = [("user_profile", self.user_profile),
                             ("user_email", get_user_email),
                             ("user_repos", self.user_repos),
                             ("user_gists", self.user_gists),
                             ("user_orgs", self.user_orgs),
                             ("user_events", self.user_events),
                             ("user_subscriptions", self.user_subscriptions),
                             ("user_following", self.user_following),
                             ("user_followers", self.user_followers),
                             ("user_follows", self.user_follows),
                             ("users_search", self.users_search),
                             ("issues_search", self.issues_search),
                             ("commits_search", self.commits_search),
                             ("topics_search", self.topics_search),
                             ("repos_search", self.repos_search),
                             ("org_profile", self.organisation_profile),
                             ("org_repos", self.org_repos),
                             ("org_events", self.org_events),
                             ("org_member", self.org_member),
                             ("repo_profile", self.repository_profile),
                             ("repo_contributors", self.repository_contributors),
                             ("repo_stargazers", self.repo_stargazers),
                             ("repo_forks", self.repo_forks),
                             ("repo_issues", self.repo_issues),
                             ("repo_releases", self.repo_releases),
                             ("repo_path_contents", self.path_contents),
                             ("view_logs", view_logs),
                             ("read_log", read_log),
                             ("delete_log", delete_log),
                             ("clear_logs", clear_logs),
                             ("view_csv", view_csv),
                             ("read_csv", read_csv),
                             ("delete_csv", delete_csv),
                             ("clear_csv", clear_csv),
                             ("about", about),
                             ("author", self.author)]

    def organisation_profile(self, args) -> None:
        """
        Query the organisation profile endpoint and process the response.

        If the status code is 404, assume the specified organisation was not found.
        If the status code is 200, display the organisation's profile information in a tree view.
        Otherwise, print the raw JSON response.

        :param args: Command-line arguments or options.
        :return: None
        """
        organisation = args.organisation or Prompt.ask("@Organisation")
        response = send_request(f"{self.endpoint}/orgs/{organisation}")

        if response[0] == 404:
            xprint(f"{colour.YELLOW}{message.org_not_found(organisation)}{colour.RESET}")
        elif response[0] == 200:
            organisation_profile_tree = Tree(f"\n{response[1]['name']}")
            for attr in attribute.organisation_profile_attributes()[0]:
                organisation_profile_tree.add(f"{attribute.organisation_profile_attributes()[1][attr]}: {response[1][attr]}")
            xprint(organisation_profile_tree)

            if args.log_to_csv or Confirm.ask(message.prompt_log_csv()):
                log_organisation_profile(response)
        else:
            xprint(response[1])

    def user_profile(self, args) -> None:
        """
        Query the user profile endpoint and process the response.

        If the status code is 404, assume the specified user was not found.
        If the status code is 200, display the user's profile information in a tree view.
        Otherwise, print the raw JSON response.

        :param args: Command-line arguments or options.
        :return: None
        """
        username = args.username or Prompt.ask("@Username")
        response = send_request(f"{self.endpoint}/users/{username}")

        if response[1] == 404:
            xprint(message.user_not_found(username))
        elif response[1] == 200:
            user_profile_tree = Tree(f"\n{response[0]['name']}")
            for attr in attribute.user_profile_attributes()[0]:
                user_profile_tree.add(f"{attribute.user_profile_attributes()[1][attr]}: {response[1][attr]}")
            xprint(user_profile_tree)

            if args.log_to_csv or Confirm.ask(message.prompt_log_csv()):
                log_user_profile(response)
        else:
            xprint(response[1])

    def repository_profile(self, args) -> None:
        """
        Query the repository profile endpoint and process the response.

        If the status code is 404, assume the specified repository was not found.
        If the status code is 200, display the repository's profile information in a tree view.
        Otherwise, print the raw JSON response.

        :param args: Command-line arguments or options.
        :return: None
        """
        username = args.username or Prompt.ask("@Username")
        repository = args.repository or Prompt.ask("%Repository")

        response = send_request(f"{self.endpoint}/repos/{username}/{repository}")
        if response[0] == 404:
            xprint(message.repo_or_user_not_found(repository, username))
        elif response[0] == 200:
            repository_profile_tree = Tree(f"\n{response[1]['full_name']}")
            for attr in attribute.repository_profile_attributes()[0]:
                repository_profile_tree.add(
                    f"{attribute.repository_profile_attributes()[1][attr]}: {response[1][attr]}")
            xprint(repository_profile_tree)

            if args.log_to_csv or Confirm.ask(message.prompt_log_csv()):
                log_repo_profile(response)
        else:
            xprint(response[1])

    def path_contents(self, args) -> None:
        """
        Query the path contents endpoint and process the response.

        If the status code is 404, assume the specified repository, user or path name was not found.
        If the status code is 200, display the repository path contents' information in a tree view.
        Otherwise, print the raw JSON response.

        :param args: Command-line arguments or options.
        :return: None
        """
        repository = args.repository or Prompt.ask(f"%Repository")
        repository_owner = args.username or Prompt.ask("@Owner (username)")
        path_name = args.path_name or Prompt.ask("~/path/name")
        response = send_request(f"{self.endpoint}/repos/{repository_owner}/{repository}/contents/{path_name}")
        if response[0] == 404:
            xprint(message.information_not_found(repository, path_name, repository_owner))
        elif response[0] == 200:
            for content_count, content in enumerate(response[1], start=1):
                path_contents_tree = Tree(f"\n{content['name']}")
                for attr in attribute.path_attributes()[0]:
                    path_contents_tree.add(f"{attribute.path_attributes()[1][attr]}: {content[attr]}")
                xprint(path_contents_tree)
                log_repo_path_contents(content, repository)
                xprint(f"Found {content_count} file(s) in {repository}/{path_name}.")
        else:
            xprint(response[1])

    def repository_contributors(self, args) -> None:
        """
        Query the repository contributors endpoint and process the response.

        If the status code is 404, assume the specified repository or user was not found.
        If the status code is 200, display the repository's contributors information in a tree view.
        Otherwise, print the raw JSON response.

        :param args: Command-line arguments or options.
        :return: None
        """
        repository = args.repository or Prompt.ask("%Repository")
        repository_owner = args.repository or Prompt.ask("@Owner (username)")
        limit = args.limit or Prompt.ask(message.limit_output("Contributors"))

        response = send_request(f"{self.endpoint}/repos/{repository_owner}/{repository}/contributors?per_page={limit}")
        if response[0] == 404:
            xprint(message.repo_or_user_not_found(repository, repository_owner))
        elif response[0] == 200:
            for contributor in response[1]:
                contributor_tree = Tree(f"\n{contributor['login']}")
                for attr in attribute.user_information_attributes()[0]:
                    contributor_tree.add(f"{attribute.user_information_attributes()[1][attr]}: {contributor[attr]}")
                xprint(contributor_tree)

                if args.log_to_csv or Confirm.ask(message.prompt_log_csv()):
                    log_repo_contributors(contributor, repository_owner)
            else:
                xprint(response[1])

    # repo stargazers
    def repository_stargazers(self, args) -> None:
        """
        Query the repository stargazers endpoint and process the response.

        If the status code is 404, assume the specified repository or user was not found.
        If the status code is 200, display the repository's stargazers information in a tree view.
        Otherwise, print the raw JSON response.

        :param args: Command-line arguments or options.
        :return: None
        """
        repository = args.repository or Prompt.ask("%Repository")
        repository_owner = args.username or Prompt.ask("@Owner (username)")
        limit = args.limit or Prompt.ask(message.limit_output("Stargazers"))
        response = send_request(f"{self.endpoint}/repos/{repository_owner}/{repository}/stargazers?per_page={limit}")
        if response[0] == 404:
            xprint(message.repo_or_user_not_found(repository, repository_owner))
        elif response[0] == {}:
            xprint(message.repo_does_not_have_stargazers(repository, repository_owner))
        elif response[0] == 200:
            for stargazer in response[1]:
                stargazer_tree = Tree(f"\n{stargazer['login']}")
                for attr in attribute.user_information_attributes()[0]:
                    stargazer_tree.add(f"{attribute.user_information_attributes()[1][attr]}: {stargazer[attr]}")
                xprint(stargazer_tree)
                
                if args.log_csv or Confirm.ask(message.prompt_log_csv()):
                    log_repo_stargazers(stargazer, repository)
        else:
            xprint(response[1])

    # repo forks
    def repo_forks(self):
        if args.repository and args.username and args.limit:
            repo_name = args.repository
            username = args.username
            limit = args.limit
        else:
            repo_name = Prompt.ask(f"{white}%{green}Repository{reset}")
            username = Prompt.ask(f"{white}@{green}Username{reset}")
            limit = Prompt.ask(limit_output.format("forks"))
        response = requests.get(f"{self.endpoint}/repos/{username}/{repo_name}/forks?per_page={limit}")
        if response.status_code == 404:
            xprint(f"{NEGATIVE} {repo_or_user_not_found.format(repo_name, username)}")
        elif response.json() == {}:
            xprint(f"{NEGATIVE} Repository does not have forks -> ({repo_name})")
        elif response.status_code == 200:
            for count, fork in enumerate(response.json()):
                fork_tree = Tree("\n" + fork['full_name'])
                for attr in self.repo_attrs:
                    fork_tree.add(f"{self.repo_attr_dict[attr]}: {fork[attr]}")
                xprint(fork_tree)

                if args.log_csv or Confirm.ask(f"\n{PROMPT} {prompt_log_csv}"):
                    log_repo_forks(fork, count)
        else:
            xprint(response.json())

    # Repo issues
    def repo_issues(self):
        if args.repository and args.username and args.limit:
            repo_name = args.repository
            username = args.username
            limit = args.limit
        else:
            repo_name = Prompt.ask(f"{white}%{green}Repository{reset}")
            username = Prompt.ask(f"{white}@{green}Username{reset}")
            limit = Prompt.ask(limit_output.format("issues"))
        response = requests.get(f"{self.endpoint}/repos/{username}/{repo_name}/issues?per_page={limit}")
        if response.status_code == 404:
            xprint(f"{NEGATIVE} {repo_or_user_not_found.format(repo_name, username)}")
        elif not response.json():
            xprint(f"{NEGATIVE} Repository does not have open issues -> ({repo_name})")
        elif response.status_code == 200:
            for issue in response.json():
                issues_tree = Tree("\n" + issue['title'])
                for attr in self.repo_issues_attrs:
                    issues_tree.add(f"{self.repo_issues_attr_dict[attr]}: {issue[attr]}")
                xprint(issues_tree)
                xprint(issue['body'])
                log_repo_issues(issue, repo_name)
        else:
            xprint(response.json())

    # Repo releases
    def repo_releases(self):
        if args.repository and args.username and args.limit:
            repo_name = args.repository
            username = args.username
            limit = args.limit
        else:
            repo_name = Prompt.ask(f"{white}%{green}Repository{reset}")
            username =  Prompt.ask(f"{white}@{green}Username{reset}")
            limit = Prompt.ask(limit_output.format("repository releases"))
        response = requests.get(f"{self.endpoint}/repos/{username}/{repo_name}/releases?per_page={limit}")
        if response.status_code == 404:
            xprint(f"{NEGATIVE} {repo_or_user_not_found.format(repo_name, username)}")
        elif not response.json():
            xprint(f"{NEGATIVE} Repository does not have releases -> ({repo_name})")
        elif response.status_code == 200:
            for release in response.json():
                releases_tree = Tree("\n" + release['name'])
                for attr in self.repo_releases_attrs:
                    releases_tree.add(f"{self.repo_releases_attr_dict[attr]}: {release[attr]}")
                xprint(releases_tree)
                xprint(release['body'])

                if args.log_csv or Confirm.ask(f"\n{PROMPT} {prompt_log_csv}"):
                    log_repo_releases(release, repo_name)
        else:
            xprint(response.json())

    # Fetching organisation repositories
    def org_repos(self):
        if args.organisation and args.limit:
            organisation = args.organisation
            limit = args.limit
        else:
            organisation = Prompt.ask(f"{white}@{green}Organisation{reset}")
            limit = Prompt.ask(limit_output.format("organisation repositories"))
        response = requests.get(f"{self.endpoint}/orgs/{organisation}/repos?per_page={limit}")
        if response.status_code == 404:
            xprint(f"{NEGATIVE} {org_not_found.format(organisation)}")
        elif response.status_code == 200:
            for repository in response.json():
                repos_tree = Tree("\n" + repository['full_name'])
                for attr in self.repo_attrs:
                    repos_tree.add(f"{self.repo_attr_dict[attr]}: {repository[attr]}")
                xprint(repos_tree)
                
                if args.log_csv or Prompt.ask(f"{PROMPT} {prompt_log_csv}") == "yes":
                    log_org_repos(repository, organisation)
        else:
            xprint(response.json())

    # organisation events
    def org_events(self):
        if args.organisation and args.limit:
            organisation = args.organisation
            limit = args.limit
        else:
            organisation = Prompt.ask(f"{white}@{green}Organisation{reset}")
            limit = Prompt.ask(limit_output.format("organisation events"))
        response = requests.get(f"{self.endpoint}/orgs/{organisation}/events?per_page={limit}")
        if response.status_code == 404:
            xprint(f"{NEGATIVE} {org_not_found.format(organisation)}")
        elif response.status_code == 200:
            for event in response.json():
                events_tree = Tree("\n" + event['id'])
                events_tree.add(f"Type: {event['type']}")
                events_tree.add(f"Created at: {event['created_at']}")
                xprint(events_tree)
                xprint(event['payload'])
            # log_org_events(event, organisation)
        else:
            xprint(response.json())

    # organisation member
    def org_member(self):
        if args.organisation and args.username:
            organisation = args.organisation
            username = args.username
        else:
            organisation = Prompt.ask(f"{white}@{green}Organisation{reset}")
            username = Prompt.ask(f"{white}@{green}Username{reset}")
        response = requests.get(f"{self.endpoint}/orgs/{organisation}/public_members/{username}")
        if response.status_code == 204:
            xprint(f"{POSITIVE} User ({username}) is a public member of the organisation -> ({organisation})")
        else:
            xprint(f"{NEGATIVE} {response.json()['message']}")

    # Fetching user repositories
    def user_repos(self):
        if args.username and args.limit:
            username = args.username
            limit = args.limit
        else:
            username = Prompt.ask(f"{white}@{green}Username{reset}")
            limit = Prompt.ask(limit_output.format("repositories"))
        response = requests.get(f"{self.endpoint}/users/{username}/repos?per_page={limit}")
        if response.status_code == 404:
            xprint(f"{NEGATIVE} {user_not_found.format(username)}")
        elif response.status_code == 200:
            for repository in response.json():
                repos_tree = Tree("\n" + repository['full_name'])
                for attr in self.repo_attrs:
                    repos_tree.add(f"{self.repo_attr_dict[attr]}: {repository[attr]}")
                xprint(repos_tree)

                if args.log_csv or Confirm.ask(f"\n{PROMPT} {prompt_log_csv}"):
                    log_user_repos(repository, username)
        else:
            xprint(response.json())

    # Fetching user's gists
    def user_gists(self):
        if args.username and args.limit:
            username = args.username
            limit = args.limit
        else:
            username = Prompt.ask(f"{white}@{green}Username{reset}")
            limit = Prompt.ask(limit_output.format('gists'))
        response = requests.get(f"{self.endpoint}/users/{username}/gists?per_page={limit}")
        if not response.json():
            xprint(f"{NEGATIVE} User does not have gists.")
        elif response.status_code == 404:
            xprint(f"{NEGATIVE} {user_not_found.format(username)}")
        elif response.status_code == 200:
            for gist in response.json():
                gists_tree = Tree("\n" + gist['id'])
                for attr in self.gists_attrs:
                    gists_tree.add(f"{self.gists_attr_dict[attr]}: {gist[attr]}")
                xprint(gists_tree)
                
                if args.log_csv or Confirm.ask(f"\n{PROMPT} {prompt_log_csv}"):
                    log_user_gists(gist)
        else:
            xprint(response.json())

    # Fetching a list of organisations that a user owns or belongs to
    def user_orgs(self):
        if args.username and args.limit:
            username = args.username
            limit = args.limit
        else:
            username = Prompt.ask(f"{white}@{green}Username{reset}")
            limit = Prompt.ask(limit_output.format("user organisations"))
        response = requests.get(f"{self.endpoint}/users/{username}/orgs?per_page={limit}")
        if not response.json():
            xprint(f"{NEGATIVE} User ({username}) does not (belong to/own) any organisations.")
        elif response.status_code == 404:
            xprint(f"{NEGATIVE} {user_not_found.format(username)}")
        elif response.status_code == 200:
            for organisation in response.json():
                org_tree = Tree("\n" + organisation['login'])
                for attr in self.user_orgs_attrs:
                    org_tree.add(f"{self.user_orgs_attr_dict[attr]}: {organisation[attr]}")
                xprint(org_tree)
                
                if args.log_csv or Confirm.ask(f"\n{PROMPT} {prompt_log_csv}"):
                    log_user_orgs(organisation, username)
        else:
            xprint(response.json())

    # Fetching a users events 
    def user_events(self):
        if args.username and args.limit:
            username = args.username
            limit = args.limit
        else:
            username = Prompt.ask(f"{white}@{green}Username{reset}")
            limit = Prompt.ask(limit_output.format("events"))
        response = requests.get(f"{self.endpoint}/users/{username}/events/public?per_page={limit}")
        if response.status_code == 404:
            xprint(f"{NEGATIVE} {user_not_found.format(username)}")
        elif response.status_code == 200:
            for event in response.json():
                events_tree = Tree("\n" + event['id'])
                events_tree.add(f"Actor: {event['actor']['login']}")
                events_tree.add(f"Type: {event['type']}")
                events_tree.add(f"Repository: {event['repo']['name']}")
                events_tree.add(f"Created at: {event['created_at']}")
                xprint(events_tree)
                xprint(event['payload'])
                log_user_events(event)
        else:
            xprint(response.json())

    # Fetching a target user's subscriptions
    def user_subscriptions(self):
        if args.username and args.limit:
            username = args.username
            limit = args.limit
        else:
            username = Prompt.ask(f"{white}@{green}Username{reset}")
            limit = Prompt.ask(limit_output.format("user subscriptions"))
        response = requests.get(f"{self.endpoint}/users/{username}/subscriptions?per_page={limit}")
        if not response.json():
            xprint(f"{NEGATIVE} User does not have any subscriptions.")
        elif response.status_code == 404:
            xprint(f"{NEGATIVE} {user_not_found.format(username)}")
        elif response.status_code == 200:
            for repository in response.json():
                subscriptions_tree = Tree("\n" + repository['full_name'])
                for attr in self.repo_attrs:
                    subscriptions_tree.add(f"{self.repo_attr_dict[attr]}: {repository[attr]}")
                xprint(subscriptions_tree)
                
                if args.log_csv or Confirm.ask(f"\n{PROMPT} {prompt_log_csv}"):
                    log_user_subscriptions(repository, username)
        else:
            xprint(response.json())

    # Fetching a list of users the target follows        
    def user_following(self):
        if args.username and args.limit:
            username = args.username
            limit = args.limit
        else:
            username = Prompt.ask(f"{white}@{green}Username{reset}")
            limit = Prompt.ask(limit_output.format("user' following"))
        response = requests.get(f"{self.endpoint}/users/{username}/following?per_page={limit}")
        if not response.json():
            xprint(f"{NEGATIVE} User ({username})does not follow anyone.")
        elif response.status_code == 404:
            xprint(f"{NEGATIVE} {user_not_found.format(username)}")
        elif response.status_code == 200:
            for user in response.json():
                following_tree = Tree("\n" + user['login'])
                for attr in self.user_attrs:
                    following_tree.add(f"{self.user_attr_dict[attr]}: {user[attr]}")
                xprint(following_tree)
                
                if args.log_csv or Confirm.ask(f"\n{PROMPT} {prompt_log_csv}"):
                    log_user_following(user, username)
        else:
            xprint(response.json())

    # Fetching user's followers
    def user_followers(self):
        if args.username and args.limit:
            username = args.username
            limit = args.limit
        else:
            username = Prompt.ask(f"{white}@{green}Username{reset}")
            limit = Prompt.ask(limit_output.format("user followers"))
        response = requests.get(f"{self.endpoint}/users/{username}/followers?per_page={limit}")
        if not response.json():
            xprint(f"{NEGATIVE} User ({username})does not have followers.")
        elif response.status_code == 404:
            xprint(f"{NEGATIVE} {user_not_found.format(username)}")
        elif response.status_code == 200:
            for follower in response.json():
                followers_tree = Tree("\n" + follower['login'])
                for attr in self.user_attrs:
                    followers_tree.add(f"{self.user_attr_dict[attr]}: {follower[attr]}")
                xprint(followers_tree)
                
                if args.log_csv or Confirm.ask(f"\n{PROMPT} {prompt_log_csv}"):
                    log_user_followers(follower, username)
        else:
            xprint(response.json())

    # Checking whether user[A] follows user[B]
    def user_follows(self):
        if args.username and args.username_b:
            user_a = args.username
            user_b = args.username_b
        else:
            user_a = Prompt.ask(f"{white}@{green}User_A{reset}")
            user_b = Prompt.ask(f"{white}@{green}User_B{reset}")
        response = requests.get(f"{self.endpoint}/users/{user_a}/following/{user_b}")
        if response.status_code == 204:
            xprint(f"{POSITIVE} @{user_a} FOLLOWS @{user_b}")
        else:
            xprint(f"{NEGATIVE} @{user_a} DOES NOT FOLLOW @{user_b}")

    # User search
    def users_search(self):
        if args.query and args.limit and args.limit:
            query = args.query
            limit = args.limit
        else:
            query = Prompt.ask(f"{white}@{green}Username{reset} (search)")
            limit = Prompt.ask(limit_output.format("user search"))
        response = requests.get(f"{self.endpoint}/search/users?q={query}&per_page={limit}").json()
        for user in response['items']:
            users_search_tree = Tree("\n" + user['login'])
            for attr in self.user_attrs:
                users_search_tree.add(f"{self.user_attr_dict[attr]}: {user[attr]}")
            xprint(users_search_tree)
            
            if args.log_csv or Confirm.ask(f"\n{PROMPT} {prompt_log_csv}"):
                log_users_search(user, query)

    # Repository search
    def repos_search(self):
        if args.query and args.limit:
            query = args.query
            limit = args.limit
        else:
            query = Prompt.ask(f"{white}%{green}Repository{reset} (search)")
            limit = Prompt.ask(limit_output.format("repositor[y][ies] search"))
        response = requests.get(f"{self.endpoint}/search/repositories?q={query}&per_page={limit}").json()
        for repository in response['items']:
            repos_search_tree = Tree("\n" + repository['full_name'])
            for attr in self.repo_attrs:
                repos_search_tree.add(f"{self.repo_attr_dict[attr]}: {repository[attr]}")
            xprint(repos_search_tree)
            
            if args.log_csv or Confirm.ask(f"\n{PROMPT} {prompt_log_csv}"):
                log_repos_search(repository, query)

    # Topics search
    def topics_search(self):
        if args.query and args.limit:
            query = args.query
            limit = args.limit
        else:
            query = Prompt.ask(f"{white}:{green}Topics{reset} (search)")
            limit = Prompt.ask(limit_output.format("topic(s) search"))
        response = requests.get(f"{self.endpoint}/search/topics?q={query}&per_page={limit}").json()
        for topic in response['items']:
            topics_search_tree = Tree("\n" + topic['name'])
            for attr in self.topic_attrs:
                topics_search_tree.add(f"{self.topic_attr_dict[attr]}: {topic[attr]}")
            xprint(topics_search_tree)
            
            if args.log_csv or Confirm.ask(f"\n{PROMPT} {prompt_log_csv}"):
                log_topics_search(topic, query)

    # Issue search
    def issues_search(self):
        if args.query and args.limit:
            query = args.query
            limit = args.limit
        else:
            query = Prompt.ask(f"{white}!{green}Issues{reset} (search)")
            limit = Prompt.ask(limit_output.format("issue(s) search"))
        response = requests.get(f"{self.endpoint}/search/issues?q={query}&per_page={limit}").json()
        for issue in response['items']:
            issues_search_tree = Tree("\n" + issue['title'])
            for attr in self.repo_issues_attrs:
                issues_search_tree.add(f"{self.repo_issues_attr_dict[attr]}: {issue[attr]}")
            xprint(issues_search_tree)
            xprint(issue['body'])
            
            if args.log_csv or Confirm.ask(f"\n{PROMPT} {prompt_log_csv}"):
                log_issues_search(issue, query)

    # Commits search
    def commits_search(self):
        if args.query and args.limit:
            query = args.query
            limit = args.limit
        else:
            query = Prompt.ask(f"{white};{green}Commits{reset} (search)")
            limit = Prompt.ask(limit_output.format("commit(s) search"))
        response = requests.get(f"{self.endpoint}/search/commits?q={query}&per_page={limit}").json()
        for commit in response['items']:
            commits_search_tree = Tree("\n" + commit['commit']['tree']['sha'])
            commits_search_tree.add(f"Author: {commit['commit']['author']['name']}")
            commits_search_tree.add(f"Username: {commit['author']['login']}")
            commits_search_tree.add(f"Email: {commit['commit']['author']['email']}")
            commits_search_tree.add(f"Commiter: {commit['commit']['committer']['name']}")
            commits_search_tree.add(f"Repository: {commit['repository']['full_name']}")
            commits_search_tree.add(f"URL: {commit['html_url']}")
            xprint(commits_search_tree)
            xprint(commit['commit']['message'])
            
            if args.log_csv or Confirm.ask(f"\n{PROMPT} {prompt_log_csv}"):
                log_commits_search(commit, query)

    # Author info
    def author(self):
        author_tree = Tree(f"{white}Richard Mwewa (Ritchie){reset}")
        for author_key, author_value in self.author_dict.items():
            author_tree.add(f"{white}{author_key}:{reset} {author_value}")
        xprint(author_tree)
