from datetime import date


class Help:
    """
    Container for documentation-related data for OctoSuite.

    Attributes:
          author (str): A markdown-formatted string of author name and url.
          copyright (str): Copyright notice for the current year, including the author's details.
          summary (str): A brief description of Knew Karma as a tool for Reddit data analysis.
          description (str): A full description of Knew Karma as a CLI, Library,
                and GUI program for Reddit data analysis.
          examples (dict): Usage examples for different operations within Knew Karma.
    """

    author: str = "[Richard Mwewa](https://rly0nheart.github.io)"
    copyright: str = (
        f"© Copyright 2022-{date.today().year} {author}. All rights reserved."
    )

    summary: str = f"**OctoSuite**: *A GitHub Data Analysis Framework* — by {author}"
    description: str = """
**OctoSuite** (/ˈɒk.toʊ.swiːt/) is an all-in-one **GitHub** data analysis framework designed to provide
insights and a thorough understanding of GitHub entities (e.i, **Users**, **Repositories** and **Organisations**). 
It offers a wide array of functionalities and tools including a **Command-Line Interface (CLI)**, 
a **Python Library** and a **Graphical User
Interface (GUI)**, enabling users to fetch and analyse GitHub data effectively and efficiently.
"""

    examples: dict = {
        "user": """
# Examples
## Get a User's Profile
```
octosuite user torvalds --profile
```
***
## Get Emails from a User's PushEvents
```
octosuite user torvalds --emails
```
***
## Get a User's Public Repositories
```
octosuite user torvalds --repos
```
***
## Get a User's Public Gists
```
octosuite user octocat --gists
```
***
## Get a User's Organisations
```
octosuite user torvalds --orgs
```
***
## Get a User's Public Events
```
octosuite user torvalds --events
```
***
## Get a User's Starred Repositories
```
octosuite user octocat --starred
```
***
## Check if User follows a Second Specified User
```
octosuite user torvalds --follows --secondary-user SECONDARY_USERNAME
```
***
## Get a User's Followers
```
octosuite user torvalds --followers
```
***
## Get Accounts followed by User
```
octosuite user torvalds --following
```
***
## Check If Target Follows The Specified User
```
octosuite user wang920509 --follows torvalds
```
""",
        "org": """
# Examples
## Get an Organisation's Profile
```
octosuite org github --profile
```
***
## Get an Organisation's Public Repositories
```
octosuite org github --repos
```
***
## Get an Organisation's Public Events
```
octosuite org github --events
```
***
## Get an Organisation's Public Members
```
octosuite org github --members
```
***
## CHeck If User Is a Public Member of the Target Organisation
```
octosuite org DROPCitizenShip --is-member torvalds
```
    """,
        "repo": """
# Examples
## Get a Repository's profile
```
octosuite repo linux torvalds --profile
```
***
## Get a Repository's Forks
```
octosuite repo linux torvalds --forks
```
***
## Get a Repository's Stargazers
```
octosuite repo linux torvalds --stargazers
```
***
## Get a Repository's Contents (from root directory)
```
octosuite repo linux torvalds --contents
```
***
## Get a Repository's Contents (from a specified directory)
```
octosuite repo linux torvalds --contents kernel
```
    """,
        "search": """
# Examples
## Search Users
```
octosuite search john --users
```
## Search Repositories
```
octosuite search octo --repos
```
***
## Search Issues
```
octosuite search error --issues
```
***
## Search Topics
```
octosuite search git --topics
```
***
## Search Commits
```
octosuite search fix --commits
```
""",
    }
