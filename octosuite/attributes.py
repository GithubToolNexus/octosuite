class Attributes:
    @staticmethod
    def path_attributes() -> tuple:
        attributes_list = ['size', 'type', 'path', 'sha', 'html_url']
        attributes_dictionary = {
            'size': 'Size (bytes)',
            'type': 'Type',
            'path': 'Path',
            'sha': 'SHA',
            'html_url': 'URL'
        }

        return attributes_list, attributes_dictionary

    @staticmethod
    def organisation_profile_attributes() -> tuple:
        attributes_list = ['avatar_url',
                           'login',
                           'id',
                           'node_id',
                           'email',
                           'description',
                           'location',
                           'blog',
                           'followers',
                           'following',
                           'twitter_username',
                           'public_gists',
                           'public_repos',
                           'type',
                           'is_verified',
                           'has_organization_projects',
                           'has_repository_projects',
                           'created_at',
                           'updated_at'
                           ]

        attribute_dictionary = {
            'avatar_url': 'Profile Photo',
            'login': 'Username',
            'id': 'ID',
            'node_id': 'Node ID',
            'email': 'Email',
            'description': 'About',
            'location': 'Location',
            'blog': 'Blog',
            'followers': 'Followers',
            'following': 'Following',
            'twitter_username': 'Twitter handle',
            'public_gists': 'Gists',
            'public_repos': 'Repositories',
            'type': 'Account type',
            'is_verified': 'Is verified?',
            'has_organization_projects': 'Has organisation projects?',
            'has_repository_projects': 'Has repository projects?',
            'created_at': 'Created at',
            'updated_at': 'Updated at'
        }

        return attributes_list, attribute_dictionary

    @staticmethod
    def repository_profile_attributes() -> tuple:
        attributes_list = ['id', 'description', 'forks', 'stargazers_count', 'watchers', 'license', 'default_branch',
                           'visibility',
                           'language', 'open_issues', 'topics', 'homepage', 'clone_url', 'ssh_url', 'fork',
                           'allow_forking',
                           'private', 'archived', 'has_downloads', 'has_issues', 'has_pages', 'has_projects',
                           'has_wiki',
                           'pushed_at', 'created_at', 'updated_at'
                           ]

        attributes_dictionary = {
            'id': 'ID',
            'description': 'About',
            'forks': 'Forks',
            'stargazers_count': 'Stars',
            'watchers': 'Watchers',
            'license': 'License',
            'default_branch': 'Branch',
            'visibility': 'Visibility',
            'language': 'Language(s)',
            'open_issues': 'Open issues',
            'topics': 'Topics',
            'homepage': 'Homepage',
            'clone_url': 'Clone URL',
            'ssh_url': 'SSH URL',
            'fork': 'Is fork?',
            'allow_forking': 'Is forkable?',
            'private': 'Is private?',
            'archived': 'Is archived?',
            'is_template': 'Is template?',
            'has_wiki': 'Has wiki?',
            'has_pages': 'Has pages?',
            'has_projects': 'Has projects?',
            'has_issues': 'Has issues?',
            'has_downloads': 'Has downloads?',
            'pushed_at': 'Pushed at',
            'created_at': 'Created at',
            'updated_at': 'Updated at'
        }

        return attributes_list, attributes_dictionary

    @staticmethod
    def repo_releases_attributes() -> tuple:
        attribute_list = [
            'id',
            'node_id',
            'tag_name',
            'target_commitish',
            'assets',
            'draft',
            'prerelease',
            'created_at',
            'published_at']

        attribute_dictionary = {
            'id': 'ID',
            'node_id': 'Node ID',
            'tag_name': 'Tag',
            'target_commitish': 'Branch',
            'assets': 'Assets',
            'draft': 'Is draft?',
            'prerelease': 'Is pre-release?',
            'created_at': 'Created at',
            'published_at': 'Published at'
        }

        return attribute_list, attribute_dictionary

    @staticmethod
    def repository_issues_attributes() -> tuple:
        attributes_list = ['id', 'node_id', 'state', 'reactions', 'number', 'comments', 'milestone', 'assignee',
                           'active_lock_reason', 'author_association', 'assignees', 'labels', 'locked',
                           'closed_at',
                           'created_at', 'updated_at']
        attributes_dictionary = {
            'id': 'ID',
            'node_id': 'Node ID',
            'number': 'Number',
            'state': 'State',
            'reactions': 'Reactions',
            'comments': 'Comments',
            'milestone': 'Milestone',
            'assignee': 'Assignee',
            'assignees': 'Assignees',
            'author_association': 'Author association',
            'labels': 'Labels',
            'locked': 'Is locked?',
            'active_lock_reason': 'Lock reason',
            'closed_at': 'Closed at',
            'created_at': 'Created at',
            'updated_at': 'Updated at'
        }

        return attributes_list, attributes_dictionary

    @staticmethod
    def user_profile_attributes() -> tuple:
        attributes_list = ['avatar_url',
                           'login',
                           'id',
                           'node_id',
                           'bio',
                           'blog',
                           'location',
                           'followers',
                           'following',
                           'twitter_username',
                           'public_gists',
                           'public_repos',
                           'company',
                           'hireable',
                           'site_admin',
                           'created_at',
                           'updated_at'
                           ]

        attributes_dictionary = {
            'avatar_url': 'Profile Photo',
            'login': 'Username',
            'id': 'ID',
            'node_id': 'Node ID',
            'bio': 'Bio',
            'blog': 'Blog',
            'location': 'Location',
            'followers': 'Followers',
            'following': 'Following',
            'twitter_username': 'Twitter Handle',
            'public_gists': 'Gists (public)',
            'public_repos': 'Repositories (public)',
            'company': 'organisation',
            'hireable': 'Is hireable?',
            'site_admin': 'Is site admin?',
            'created_at': 'Joined at',
            'updated_at': 'Updated at'
        }

        return attributes_list, attributes_dictionary

    @staticmethod
    def user_summary_attributes() -> tuple:
        attributes_list = ['avatar_url', 'id', 'node_id', 'gravatar_id', 'site_admin', 'type', 'html_url']

        attributes_dictionary = {
            'avatar_url': 'Profile Photo',
            'id': 'ID',
            'node_id': 'Node ID',
            'gravatar_id': 'Gravatar ID',
            'site_admin': 'Is site admin?',
            'type': 'Account type',
            'html_url': 'URL'
        }

        return attributes_list, attributes_dictionary

    @staticmethod
    def topic_information_attributes() -> tuple:
        attributes_list = ['score', 'curated', 'featured', 'display_name', 'created_by', 'created_at', 'updated_at']

        attribute_dictionary = {
            'score': 'Score',
            'curated': 'Curated',
            'featured': 'Featured',
            'display_name': 'Display name',
            'created_by': 'Created by',
            'created_at': 'Created at',
            'updated_at': 'Updated at'
        }

        return attributes_list, attribute_dictionary

    @staticmethod
    def gist_information_attributes() -> tuple:
        attributes_list = ['node_id', 'description', 'comments', 'files', 'git_push_url', 'public', 'truncated',
                           'updated_at'
                           ]

        attributes_dictionary = {
            'node_id': 'Node ID',
            'description': 'About',
            'comments': 'Comments',
            'files': 'Files',
            'git_push_url': 'Git Push URL',
            'public': 'Is public?',
            'truncated': 'Is truncated?',
            'updated_at': 'Updated at'
        }

        return attributes_list, attributes_dictionary

    @staticmethod
    def issue_information_attributes() -> tuple:
        attributes_list = ['id',
                           'node_id',
                           'score',
                           'state',
                           'number',
                           'comments',
                           'milestone',
                           'assignee',
                           'assignees',
                           'labels',
                           'locked',
                           'draft',
                           'closed_at'
                           ]

        attributes_dictionary = {
            'id': 'ID',
            'node_id': 'Node ID',
            'score': 'Score',
            'state': 'State',
            'closed_at': 'Closed at',
            'number': 'Number',
            'comments': 'Comments',
            'milestone': 'Milestone',
            'assignee': 'Assignee',
            'assignees': 'Assignees',
            'labels': 'Labels',
            'draft': 'Is draft?',
            'locked': 'Is locked?',
            'created_at': 'Created at'
        }

        return attributes_list, attributes_dictionary

    @staticmethod
    def repo_issues_attributes() -> tuple:
        attributes_list = ['id',
                           'node_id',
                           'number',
                           'state',
                           'reactions',
                           'comments',
                           'milestone',
                           'assignee',
                           'assignees',
                           'author_association',
                           'labels',
                           'locked',
                           'active_lock_reason',
                           'closed_at',
                           'created_at',
                           'updated_at'
                           ]

        attributes_dictionary = {
            'id': 'ID',
            'node_id': 'Node ID',
            'number': 'Number',
            'state': 'State',
            'reactions': 'Reactions',
            'comments': 'Comments',
            'milestone': 'Milestone',
            'assignee': 'Assignee',
            'assignees': 'Assignees',
            'author_association': 'Author association',
            'labels': 'Labels',
            'locked': 'Is locked?',
            'active_lock_reason': 'Lock reason',
            'closed_at': 'Closed at',
            'created_at': 'Created at',
            'updated_at': 'Updated at'
        }

        return attributes_list, attributes_dictionary

    @staticmethod
    def user_orgs_information_attributes() -> tuple:
        attributes_list = ['avatar_url', 'id', 'node_id', 'url', 'description']

        attribute_dictionary = {
            'avatar_url': 'Profile Photo',
            'id': 'ID',
            'node_id': 'Node ID',
            'url': 'URL',
            'description': 'About'
        }

        return attributes_list, attribute_dictionary

    @staticmethod
    def gist_attributes() -> tuple:
        attributes_list = ['node_id', 'description', 'comments', 'files', 'git_push_url', 'public', 'truncated',
                           'updated_at']

        attributes_dictionary = {
            'node_id': 'Node ID',
            'description': 'About',
            'comments': 'Comments',
            'files': 'Files',
            'git_push_url': 'Git Push URL',
            'public': 'Is public?',
            'truncated': 'Is truncated?',
            'updated_at': 'Updated at'
        }

        return attributes_list, attributes_dictionary
