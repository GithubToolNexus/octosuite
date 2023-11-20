__author__ = "Richard Mwewa"
__about__ = "https://about.me/rly0nheart"
__version__ = "4.0.0.0"
__description__ = """
# OctoSuite
> An **All-In-One** framework for gathering **Open-Source Intelligence** on GitHub entities."""
__epilog__ = f"""
# by [{__author__}]({__about__})
```
Copyright © 2022-2023 {__author__}

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see https://www.gnu.org/licenses/.
```
"""

__user_examples__ = """
# Examples
## Get a User's Profile
```
octosuite user USERNAME --profile
```

## Get Emails from a User's PushEvents
```
octosuite user USERNAME --emails
```

## Get a User's Repositories (public) (optional: -l/--limit)
```
octosuite --limit INTEGER user USERNAME --repos
```

## Get a User's Gists (public) (optional: -l/--limit)
```
octosuite --limit INTEGER user USERNAME --gists
```

## Get a User's Organisations (public) (optional: -l/--limit)
```
octosuite --limit INTEGER user USERNAME -- orgs
```

## Get a User's Events (public) (optional: -l/--limit)
```
octosuite --limit INTEGER user USERNAME --events
```

## Get a User's Starred Repositories (public) (optional: -l/--limit)
```
octosuite --limit INTEGER user USERNAME --starred
```

## Check if User follows a Second Specified User
```
octosuite user USERNAME --follows --secondary-user SECONDARY_USERNAME
```

## Get a User's Followers (optional: -l/--limit)
```
octosuite --limit INTEGER user USERNAME --followers
```

## Get Accounts followed by User
```
octosuite --limit INTEGER user USERNAME --following
```
"""

__organisation_examples__ = """
# Examples
## Get an Organisation's Profile
```
octosuite org ORGANISATION --profile
```

## Get an Organisation's Repositories (public) (optional: -l/--limit)
```
octosuite --limit 10 org ORGANISATION --repos
```

## Get an Organisation's Events (public) (optional: -l/--limit)
```
octosuite --limit 10 org ORGANISATION --events
```

## Check if a User is a public Member of an Organisation
```
octosuite org ORGANISATION --is-member -u USERNAME
```
"""

__repository_examples__ = """
# Examples
## Get a Post's data (similar to profile data)
```
octosuite repo REPO_NAME --owner REPO_OWNER_USERNAME --profile
```
"""
