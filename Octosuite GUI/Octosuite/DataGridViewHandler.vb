Imports System.IO
Imports Newtonsoft.Json.Linq

Public Class DataGridViewHandler

    ''' <summary>
    ''' Sets up the DataGridView by clearing its existing columns and rows, and then adding new columns.
    ''' </summary>
    ''' <param name="dataGrid">The DataGridView to set up.</param>
    ''' <param name="columnHeaders">A Dictionary containing column keys and their display names.</param>
    Private Sub SetupDataGrid(dataGrid As DataGridView, columnHeaders As Dictionary(Of String, String))
        dataGrid.Rows.Clear()
        dataGrid.Columns.Clear()

        For Each kvp In columnHeaders
            dataGrid.Columns.Add(kvp.Key, kvp.Value)
        Next
    End Sub

    ''' <summary>
    ''' Populates the DataGridView with rows of data based on an array of JObject items.
    ''' </summary>
    ''' <param name="dataGrid">The DataGridView to populate.</param>
    ''' <param name="subscriptions">The JArray containing subscription data.</param>
    ''' <param name="columnKeys">A List of keys to fetch data from each JObject.</param>
    Private Sub PopulateDataGrid(dataGrid As DataGridView, subscriptions As JArray, columnKeys As List(Of String))
        Dim count As Integer = 0
        For Each subscription As JObject In subscriptions
            Dim rowData As New List(Of Object)

            count += 1
            rowData.Add(count)

            For Each key In columnKeys
                rowData.Add(subscription(key)?.ToString())
            Next

            dataGrid.Rows.Add(rowData.ToArray())
        Next
    End Sub



    ''' <summary>
    ''' Loads the user profile asynchronously and updates the form.
    ''' </summary>
    ''' <param name="username">The username to fetch data for.</param>
    ''' <param name="form">The UserProfileForm to update.</param>
    Public Async Function LoadUserProfile(username As String, form As UserProfileForm) As Task
        ''' <summary>
        ''' Instantiate a new ApiHandler object for interacting with the GitHub API.
        ''' </summary>
        ''' 
        Dim apiHandler As New ApiHandler()
        Dim data As JObject = Await apiHandler.UserProfile(username)

        If data Is Nothing Then
            MessageBox.Show("Unable to retrieve user profile.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        form.Text = $"User Profile - {username}"

        ' Setup the columns in the DataGridView
        Dim columnHeaders As New Dictionary(Of String, String) From {
            {"Field", "Field"},
            {"Value", "Value"}
        }

        SetupDataGrid(form.DataGridViewUserProfile, columnHeaders)

        ' Populate the DataGridView rows
        Dim columnKeys As New List(Of String) From {
            "name",
            "avatar_url",
            "login",
            "id",
            "node_id",
            "bio",
            "location",
            "followers",
            "following",
            "twitter_username",
            "public_gists",
            "public_repos",
            "company",
            "hireable",
            "created_at",
            "updated_at"
        }

        For Each key In columnKeys
            Dim value As Object = data(key)?.ToString()
            form.DataGridViewUserProfile.Rows.Add(New Object() {key, value})
        Next

        form.Show()
    End Function



    ''' <summary>
    ''' Loads the organisation profile asynchronously and updates the form.
    ''' </summary>
    ''' <param name="organisation">The organisation name to fetch data for.</param>
    ''' <param name="form">The OrgProfileForm to update.</param>
    Public Async Function LoadOrganisationProfile(organisation As String, form As OrgProfileForm) As Task
        ''' <summary>
        ''' Instantiate a new ApiHandler object for interacting with the GitHub API.
        ''' </summary>
        Dim apiHandler As New ApiHandler()
        Dim data As JObject = Await apiHandler.OrgProfile(organisation)

        If data Is Nothing Then
            MessageBox.Show("Unable to retrieve organisation profile.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        form.Text = $"Organisation Profile - {organisation}"

        ' Setup the columns in the DataGridView
        Dim columnHeaders As New Dictionary(Of String, String) From {
        {"Field", "Field"},
        {"Value", "Value"}
    }

        SetupDataGrid(form.DataGridOrgProfile, columnHeaders)

        ' Populate the DataGridView rows
        Dim columnKeys As New List(Of String) From {
            "name",
            "avatar_url",
            "login",
            "id",
            "node_id",
            "email",
            "description",
            "location",
            "blog",
            "followers",
            "following",
            "twitter_username",
            "public_gists",
            "public_repos",
            "type",
            "is_verified",
            "has_organization_projects",
            "has_repository_projects",
            "created_at",
            "updated_at"
        }

        For Each key In columnKeys
            Dim value As Object = data(key)?.ToString()
            form.DataGridOrgProfile.Rows.Add(New Object() {key, value})
        Next

        form.Show()
    End Function



    ''' <summary>
    ''' Asynchronously loads the user repositories into the UserReposForm.
    ''' </summary>
    ''' <param name="username">The username for which to fetch the repositories.</param>
    ''' <param name="form">The UserReposForm instance to update.</param>
    ''' <returns></returns>
    Public Async Function LoadUserRepositories(username As String, form As UserReposForm) As Task
        ''' <summary>
        ''' Instantiate a new ApiHandler object for interacting with the GitHub API.
        ''' </summary>
        Dim apiHandler As New ApiHandler()


        ''' <summary>
        ''' Fetch user repositories using the ApiHandler.
        ''' </summary>
        Dim repos As JArray = Await apiHandler.UserRepos(username)

        ''' <summary>
        ''' Handle null or empty repositories.
        ''' </summary>
        If repos Is Nothing OrElse repos.Count = 0 Then
            MessageBox.Show("Unable to retrieve user repositories.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ''' <summary>
        ''' Set the form title.
        ''' </summary>
        form.Text = $"📂 User Repositories - {username}"

        ''' <summary>
        ''' Setup the DataGridView columns.
        ''' </summary>
        Dim columnHeaders As New Dictionary(Of String, String) From {
            {"RepoCount", "🔢 Count"},
            {"RepoName", " 👤 Name"},
            {"RepoID", "ID"},
            {"RepoAbout", "ℹ️ About"},
            {"RepoForks", "📂 Forks"},
            {"RepoStars", "🌟 Stars"},
            {"RepoWatchers", "👀 Watchers"},
            {"RepoLicense", "🗒️ License"},
            {"RepoDefaultBranch", "🌳 Default Branch"},
            {"RepoVisibility", "🫣 Visibility"},
            {"RepoLanguages", "🖥️ Language(s)"},
            {"RepoOpenIssues", "❗Open Issues"},
            {"RepoTopics", "❕Topics"},
            {"RepoHomepage", "🏠 Homepage"},
            {"RepoCloneUrl", "🌐 Clone URL"},
            {"RepoSSHUrl", "🌐 SSH URL"},
            {"RepoIsFork", "❔Is Fork?"},
            {"RepoIsForkable", "❔Is Forkable?"},
            {"RepoIsPrivate", "❔Is Private?"},
            {"RepoIsArchived", "❔Is Archived?"},
            {"RepoIsTemplate", "❔Is Template?"},
            {"RepoHasWiki", "❔Has Wiki?"},
            {"RepoHasPages", "❔Has Pages?"},
            {"RepoHasProjects", "❔Has Projects?"},
            {"RepoHasIssues", "❔Has Issues?"},
            {"RepoHasDownloads", "❔Has Downloads?"},
            {"RepoPushedAt", "📅 Pushed At"},
            {"RepoCreatedAt", "📅 Created At"},
            {"RepoUpdatedAt", "📅 Updated At"}
        }

        ''' <summary>
        ''' Call SetupDataGrid to initialize DataGridView.
        ''' </summary>
        SetupDataGrid(form.DataGridViewUserRepos, columnHeaders)

        Dim count As Integer = 0

        ''' <summary>
        ''' Iterate through each repository to populate DataGridView rows.
        ''' </summary>
        For Each repo As JObject In repos
            count += 1

            Dim rowValues As New List(Of String) From {
                count.ToString(),
                repo("name")?.ToString(),
                repo("id")?.ToString(),
                repo("description")?.ToString(),
                repo("forks")?.ToString(),
                repo("stargazers_count")?.ToString(),
                repo("watchers")?.ToString(),
                If(repo("license").Type <> JTokenType.Null, repo("license")("name")?.ToString(), "Not Found"),
                repo("default_branch")?.ToString(),
                repo("visibility")?.ToString(),
                repo("language")?.ToString(),
                repo("open_issues")?.ToString(),
                repo("topics")?.ToString(),
                repo("homepage")?.ToString(),
                repo("clone_url")?.ToString(),
                repo("ssh_url")?.ToString(),
                repo("fork")?.ToString(),
                repo("allow_forking")?.ToString(),
                repo("private")?.ToString(),
                repo("archived")?.ToString(),
                repo("is_template")?.ToString(),
                repo("has_wiki")?.ToString(),
                repo("has_pages")?.ToString(),
                repo("has_projects")?.ToString(),
                repo("has_issues")?.ToString(),
                repo("has_downloads")?.ToString(),
                repo("pushed_at")?.ToString(),
                repo("created_at")?.ToString(),
                repo("updated_at")?.ToString()
            }

            form.DataGridViewUserRepos.Rows.Add(rowValues.ToArray())
        Next

        ''' <summary>
        ''' Show the form.
        ''' </summary>
        form.Show()
    End Function

    ''' <summary>
    ''' Asynchronously loads the user subscriptions into the UserSubscriptionsForm.
    ''' </summary>
    ''' <param name="username">The GitHub username for which to fetch the subscriptions.</param>
    ''' <param name="form">The UserSubscriptionsForm instance to populate.</param>
    ''' <returns>A Task representing the asynchronous operation.</returns>
    Public Async Function LoadUserSubscriptions(username As String, form As UserSubscriptionsForm) As Task
        ''' <summary>
        ''' Instantiate a new ApiHandler object for interacting with the GitHub API.
        ''' </summary>
        Dim apiHandler As New ApiHandler()

        ''' <summary>
        ''' Fetch user subscriptions using the ApiHandler.
        ''' </summary>
        Dim subscriptions As JArray = Await apiHandler.UserSubscriptions(username)

        ''' <summary>
        ''' Handle null or empty subscriptions.
        ''' </summary>
        If subscriptions Is Nothing OrElse subscriptions.Count = 0 Then
            MessageBox.Show("Unable to retrieve user subscriptions.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ''' <summary>
        ''' Set the form title.
        ''' </summary>
        form.Text = $"📂 User Subscriptions (Starred repositories) - {username}"

        ''' <summary>
        ''' Setup the DataGridView columns.
        ''' </summary>
        Dim columnHeaders As New Dictionary(Of String, String) From {
            {"RepoCount", "🔢 Count"},
            {"RepoName", " 👤 Name"},
            {"RepoID", "ID"},
            {"RepoAbout", "ℹ️ About"},
            {"RepoForks", "📂 Forks"},
            {"RepoStars", "🌟 Stars"},
            {"RepoWatchers", "👀 Watchers"},
            {"RepoLicense", "🗒️ License"},
            {"RepoDefaultBranch", "🌳 Default Branch"},
            {"RepoVisibility", "🫣 Visibility"},
            {"RepoLanguages", "🖥️ Language(s)"},
            {"RepoOpenIssues", "❗Open Issues"},
            {"RepoTopics", "❕Topics"},
            {"RepoHomepage", "🏠 Homepage"},
            {"RepoCloneUrl", "🌐 Clone URL"},
            {"RepoSSHUrl", "🌐 SSH URL"},
            {"RepoIsFork", "❔Is Fork?"},
            {"RepoIsForkable", "❔Is Forkable?"},
            {"RepoIsPrivate", "❔Is Private?"},
            {"RepoIsArchived", "❔Is Archived?"},
            {"RepoIsTemplate", "❔Is Template?"},
            {"RepoHasWiki", "❔Has Wiki?"},
            {"RepoHasPages", "❔Has Pages?"},
            {"RepoHasProjects", "❔Has Projects?"},
            {"RepoHasIssues", "❔Has Issues?"},
            {"RepoHasDownloads", "❔Has Downloads?"},
            {"RepoPushedAt", "📅 Pushed At"},
            {"RepoCreatedAt", "📅 Created At"},
            {"RepoUpdatedAt", "📅 Updated At"}
        }

        ''' <summary>
        ''' Call SetupDataGrid to initialize DataGridView.
        ''' </summary>
        SetupDataGrid(form.DataGridViewUserSubscriptions, columnHeaders)

        Dim count As Integer = 0

        ''' <summary>
        ''' Iterate through each subscription to populate DataGridView rows.
        ''' </summary>
        For Each subscription As JObject In subscriptions
            count += 1
            Dim rowValues As New List(Of String) From {
                count.ToString(),
                subscription("name")?.ToString(),
                subscription("id")?.ToString(),
                subscription("description")?.ToString(),
                subscription("forks")?.ToString(),
                subscription("stargazers_count")?.ToString(),
                subscription("watchers")?.ToString(),
                If(subscription("license").Type <> JTokenType.Null, subscription("license")("name")?.ToString(), "Not Found"),
                subscription("default_branch")?.ToString(),
                subscription("visibility")?.ToString(),
                subscription("language")?.ToString(),
                subscription("open_issues")?.ToString(),
                subscription("topics")?.ToString(),
                subscription("homepage")?.ToString(),
                subscription("clone_url")?.ToString(),
                subscription("ssh_url")?.ToString(),
                subscription("fork")?.ToString(),
                subscription("allow_forking")?.ToString(),
                subscription("private")?.ToString(),
                subscription("archived")?.ToString(),
                subscription("is_template")?.ToString(),
                subscription("has_wiki")?.ToString(),
                subscription("has_pages")?.ToString(),
                subscription("has_projects")?.ToString(),
                subscription("has_issues")?.ToString(),
                subscription("has_downloads")?.ToString(),
                subscription("pushed_at")?.ToString(),
                subscription("created_at")?.ToString(),
                subscription("updated_at")?.ToString()
            }

            form.DataGridViewUserSubscriptions.Rows.Add(rowValues.ToArray())
        Next

        ''' <summary>
        ''' Show the form.
        ''' </summary>
        form.Show()
    End Function


    ''' <summary>
    ''' Asynchronously loads the user's followers into a UserFollowersForm's DataGridView.
    ''' </summary>
    ''' <param name="username">The GitHub username for which to fetch followers.</param>
    ''' <param name="form">The UserFollowersForm instance where the followers will be displayed.</param>
    ''' <returns>A Task representing the asynchronous operation.</returns>
    Public Async Function LoadUserFollowers(username As String, form As UserFollowersForm) As Task

        ''' <summary>
        ''' Instantiate a new ApiHandler object for interacting with the API.
        ''' </summary>
        Dim apiHandler As New ApiHandler()

        ''' <summary>
        ''' Retrieve the followers as a JSON array.
        ''' </summary>
        Dim followers As JArray = Await apiHandler.UserFollowers(username)

        ''' <summary>
        ''' Check if followers could be retrieved.
        ''' </summary>
        If followers Is Nothing OrElse followers.Count = 0 Then
            MessageBox.Show("Unable to retrieve user followers.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ''' <summary>
        ''' Set the title for the form.
        ''' </summary>
        form.Text = $"User Followers - {username}"

        ''' <summary>
        ''' Set up the columns in the DataGridView using a dictionary.
        ''' </summary>
        Dim columnHeaders As New Dictionary(Of String, String) From {
        {"FollowerCount", "Count"},
        {"FollowerLogin", "Username"},
        {"FollowerAvatar", "Avatar URL"},
        {"FollowerGravatarID", "Gravatar ID"},
        {"FollowerID", "ID"},
        {"FollowerNodeID", "Node ID"},
        {"FollowerAccountType", "Account Type"},
        {"FollowerIsSiteAdmin", "Is Site Admin?"},
        {"FollowerUrl", "URL"}
    }

        SetupDataGrid(form.DataGridViewUserFollowers, columnHeaders)

        ''' <summary>
        ''' Populate the DataGridView rows with the followers' information.
        ''' </summary>
        Dim count As Integer = 0
        For Each follower As JObject In followers
            count += 1
            Dim rowValues As New List(Of String) From {
            count.ToString(),
            follower("login")?.ToString(),
            follower("avatar_url")?.ToString(),
            follower("gravatar_id")?.ToString(),
            follower("id")?.ToString(),
            follower("node_id")?.ToString(),
            follower("type")?.ToString(),
            follower("site_admin")?.ToString(),
            follower("html_url")?.ToString()
        }

            form.DataGridViewUserFollowers.Rows.Add(rowValues.ToArray())
        Next

        ''' <summary>
        ''' Show the form after populating the DataGridView.
        ''' </summary>
        form.Show()
    End Function



    ''' <summary>
    ''' Asynchronously loads the accounts that the user is following into a UserFollowingForm's DataGridView.
    ''' </summary>
    ''' <param name="username">The GitHub username for which to fetch following accounts.</param>
    ''' <param name="form">The UserFollowingForm instance where the following accounts will be displayed.</param>
    ''' <returns>A Task representing the asynchronous operation.</returns>
    Public Async Function LoadUserFollowing(username As String, form As UserFollowingForm) As Task

        ''' <summary>
        ''' Instantiate a new ApiHandler object for interacting with the GitHub API.
        ''' </summary>
        Dim apiHandler As New ApiHandler()

        ''' <summary>
        ''' Retrieve the following accounts as a JSON array.
        ''' </summary>
        Dim followings As JArray = Await apiHandler.UserFollowing(username)

        ''' <summary>
        ''' Check if the following accounts could be retrieved.
        ''' </summary>
        If followings Is Nothing OrElse followings.Count = 0 Then
            MessageBox.Show("Unable to retrieve user followings.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ''' <summary>
        ''' Set the title for the form.
        ''' </summary>
        form.Text = $"User Following - {username}"

        ''' <summary>
        ''' Clear existing columns and rows before setting up new ones.
        ''' </summary>
        form.DataGridViewUserFollowing.Rows.Clear()
        form.DataGridViewUserFollowing.Columns.Clear()

        ''' <summary>
        ''' Set up the columns in the DataGridView using a dictionary.
        ''' </summary>
        Dim columnHeaders As New Dictionary(Of String, String) From {
        {"FollowerCount", "Count"},
        {"FollowerLogin", "Username"},
        {"FollowerAvatar", "Avatar URL"},
        {"FollowerGravatarID", "Gravatar ID"},
        {"FollowerID", "ID"},
        {"FollowerNodeID", "Node ID"},
        {"FollowerAccountType", "Account Type"},
        {"FollowerIsSiteAdmin", "Is Site Admin?"},
        {"FollowerUrl", "URL"}
    }

        SetupDataGrid(form.DataGridViewUserFollowing, columnHeaders)

        ''' <summary>
        ''' Populate the DataGridView rows with the following accounts' information.
        ''' </summary>
        Dim count As Integer = 0
        For Each following As JObject In followings
            count += 1
            Dim rowValues As New List(Of String) From {
            count.ToString(),
            following("login")?.ToString(),
            following("avatar_url")?.ToString(),
            following("gravatar_id")?.ToString(),
            following("id")?.ToString(),
            following("node_id")?.ToString(),
            following("type")?.ToString(),
            following("site_admin")?.ToString(),
            following("html_url")?.ToString()
        }

            form.DataGridViewUserFollowing.Rows.Add(rowValues.ToArray())
        Next

        ''' <summary>
        ''' Show the form after populating the DataGridView.
        ''' </summary>
        form.Show()
    End Function


    ''' <summary>
    ''' Asynchronously loads the user search results into a UserSearchResultsForm's DataGridView.
    ''' </summary>
    ''' <param name="query">The search query for which to fetch user information.</param>
    ''' <param name="form">The UserSearchResultsForm instance where the search results will be displayed.</param>
    ''' <returns>A Task representing the asynchronous operation.</returns>
    Public Async Function LoadUserSearchResults(query As String, form As UserSearchResultsForm) As Task

        ''' <summary>
        ''' Instantiate a new ApiHandler object for interacting with the GitHub API.
        ''' </summary>
        Dim apiHandler As New ApiHandler()

        ''' <summary>
        ''' Retrieve the search results as a JSON object.
        ''' </summary>
        Dim results As JObject = Await apiHandler.UserSearch(query)

        ''' <summary>
        ''' Check if the search results could be retrieved.
        ''' </summary>
        If results Is Nothing OrElse results("items").Count = 0 Then
            MessageBox.Show("Unable to retrieve search results.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ''' <summary>
        ''' Set the title for the form.
        ''' </summary>
        form.Text = $"User Search - {query}"

        ''' <summary>
        ''' Clear existing columns and rows before setting up new ones.
        ''' </summary>
        form.DataGridViewUserSearchResults.Rows.Clear()
        form.DataGridViewUserSearchResults.Columns.Clear()

        ''' <summary>
        ''' Set up the columns in the DataGridView using a dictionary.
        ''' </summary>
        Dim columnHeaders As New Dictionary(Of String, String) From {
        {"FollowerCount", "Count"},
        {"FollowerLogin", "Username"},
        {"FollowerAvatar", "Avatar URL"},
        {"FollowerGravatarID", "Gravatar ID"},
        {"FollowerID", "ID"},
        {"FollowerNodeID", "Node ID"},
        {"FollowerAccountType", "Account Type"},
        {"FollowerIsSiteAdmin", "Is Site Admin?"},
        {"FollowerUrl", "URL"}
    }

        SetupDataGrid(form.DataGridViewUserSearchResults, columnHeaders)

        ''' <summary>
        ''' Populate the DataGridView rows with the search results' information.
        ''' </summary>
        Dim count As Integer = 0
        For Each result As JObject In results("items").ToObject(Of JArray)()
            count += 1
            Dim rowValues As New List(Of String) From {
            count.ToString(),
            result("login")?.ToString(),
            result("avatar_url")?.ToString(),
            result("gravatar_id")?.ToString(),
            result("id")?.ToString(),
            result("node_id")?.ToString(),
            result("type")?.ToString(),
            result("site_admin")?.ToString(),
            result("html_url")?.ToString()
        }

            form.DataGridViewUserSearchResults.Rows.Add(rowValues.ToArray())
        Next

        ''' <summary>
        ''' Show the form after populating the DataGridView.
        ''' </summary>
        form.Show()
    End Function


    ''' <summary>
    ''' Asynchronously loads the repository search results into a RepoSearchResultsForm's DataGridView.
    ''' </summary>
    ''' <param name="query">The search query for which to fetch repository information.</param>
    ''' <param name="form">The RepoSearchResultsForm instance where the search results will be displayed.</param>
    ''' <returns>A Task representing the asynchronous operation.</returns>
    Public Async Function LoadRepoSearchResults(query As String, form As RepoSearchResultsForm) As Task
        ''' <summary>
        ''' Instantiate a new ApiHandler object for interacting with the GitHub API.
        ''' </summary>
        Dim apiHandler As New ApiHandler()

        ''' <summary>
        ''' Retrieve the search results as a JSON object.
        ''' </summary>
        Dim results As JObject = Await apiHandler.RepoSearch(query)

        ''' <summary>
        ''' Check if the search results could be retrieved.
        ''' </summary>
        If results Is Nothing OrElse results("items").Count = 0 Then
            MessageBox.Show("Unable to retrieve search results.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ''' <summary>
        ''' Set the title for the form.
        ''' </summary>
        form.Text = $"📂 Repository Search - {query}"

        ''' <summary>
        ''' Setup the columns in the DataGridView.
        ''' </summary>
        Dim columnHeaders As New Dictionary(Of String, String) From {
            {"RepoCount", "🔢 Count"},
            {"RepoName", " 👤 Name"},
            {"RepoID", "ID"},
            {"RepoAbout", "ℹ️ About"},
            {"RepoForks", "📂 Forks"},
            {"RepoStars", "🌟 Stars"},
            {"RepoWatchers", "👀 Watchers"},
            {"RepoLicense", "🗒️ License"},
            {"RepoDefaultBranch", "🌳 Default Branch"},
            {"RepoVisibility", "🫣 Visibility"},
            {"RepoLanguages", "🖥️ Language(s)"},
            {"RepoOpenIssues", "❗Open Issues"},
            {"RepoTopics", "❕Topics"},
            {"RepoHomepage", "🏠 Homepage"},
            {"RepoCloneUrl", "🌐 Clone URL"},
            {"RepoSSHUrl", "🌐 SSH URL"},
            {"RepoIsFork", "❔Is Fork?"},
            {"RepoIsForkable", "❔Is Forkable?"},
            {"RepoIsPrivate", "❔Is Private?"},
            {"RepoIsArchived", "❔Is Archived?"},
            {"RepoIsTemplate", "❔Is Template?"},
            {"RepoHasWiki", "❔Has Wiki?"},
            {"RepoHasPages", "❔Has Pages?"},
            {"RepoHasProjects", "❔Has Projects?"},
            {"RepoHasIssues", "❔Has Issues?"},
            {"RepoHasDownloads", "❔Has Downloads?"},
            {"RepoPushedAt", "📅 Pushed At"},
            {"RepoCreatedAt", "📅 Created At"},
            {"RepoUpdatedAt", "📅 Updated At"}
        }

        SetupDataGrid(form.DataGridViewRepoSearchResults, columnHeaders)

        Dim count As Integer = 0

        ''' <summary>
        ''' Populate the DataGridView rows with the search results' information.
        ''' </summary>
        For Each result As JObject In results("items").ToObject(Of JArray)()
            count += 1
            Dim rowValues As New List(Of String) From {
                count.ToString(),
                result("name")?.ToString(),
                result("id")?.ToString(),
                result("description")?.ToString(),
                result("forks")?.ToString(),
                result("stargazers_count")?.ToString(),
                result("watchers")?.ToString(),
                If(result("license").Type <> JTokenType.Null, result("license")("name")?.ToString(), "Not Found"),
                result("default_branch")?.ToString(),
                result("visibility")?.ToString(),
                result("language")?.ToString(),
                result("open_issues")?.ToString(),
                result("topics")?.ToString(),
                result("homepage")?.ToString(),
                result("clone_url")?.ToString(),
                result("ssh_url")?.ToString(),
                result("fork")?.ToString(),
                result("allow_forking")?.ToString(),
                result("private")?.ToString(),
                result("archived")?.ToString(),
                result("is_template")?.ToString(),
                result("has_wiki")?.ToString(),
                result("has_pages")?.ToString(),
                result("has_projects")?.ToString(),
                result("has_issues")?.ToString(),
                result("has_downloads")?.ToString(),
                result("pushed_at")?.ToString(),
                result("created_at")?.ToString(),
                result("updated_at")?.ToString()
            }

            form.DataGridViewRepoSearchResults.Rows.Add(rowValues.ToArray())
        Next

        ''' <summary>
        ''' Show the form after populating the DataGridView.
        ''' </summary>
        form.Show()
    End Function

    ''' <summary>
    ''' Asynchronously checks if a GitHub user (user_a) follows another GitHub user (user_b).
    ''' </summary>
    ''' <param name="user_a">The username of the first user (the follower).</param>
    ''' <param name="user_b">The username of the second user (the one being followed).</param>
    ''' <returns>A Task representing the asynchronous operation.</returns>
    Public Async Function CheckIfUserFollows(user_a As String, user_b As String) As Task
        ''' <summary>
        ''' Instantiate a new ApiHandler object for interacting with the GitHub API.
        ''' </summary>
        Dim apiHandler As New ApiHandler()

        ''' <summary>
        ''' Retrieve the following status as a JSON array.
        ''' </summary>
        Dim follows As JArray = Await apiHandler.UserFollows(user_a, user_b)

        ''' <summary>
        ''' Check if the following status could be retrieved.
        ''' </summary>
        If follows Is Nothing Then
            MessageBox.Show("Unable to retrieve user following status.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ''' <summary>
        ''' Determine if user_a follows user_b and display appropriate message box.
        ''' </summary>
        If follows.Count > 0 Then
            MessageBox.Show($"{user_a} follows {user_b}", "Follows", MessageBoxButtons.OK, MessageBoxIcon.Information)
        Else
            MessageBox.Show($"{user_a} does not follow {user_b}", "Doesn't Follow", MessageBoxButtons.OK, MessageBoxIcon.Exclamation)
        End If
    End Function



    Public Async Function LoadUserOrganisations(username As String, form As UserOrgsForm) As Task
        ''' <summary>
        ''' Instantiate a new ApiHandler object for interacting with the GitHub API.
        ''' </summary>
        Dim apiHandler As New ApiHandler()

        ''' <summary>
        ''' Retrieve the organisations as a JSON object.
        ''' </summary>
        Dim organisations As JArray = Await apiHandler.UserOrgs(username)

        ''' <summary>
        ''' Check if the search organisations could be retrieved.
        ''' </summary>
        If organisations Is Nothing OrElse organisations.Count = 0 Then
            MessageBox.Show("Unable to retrieve user organisations.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ''' <summary>
        ''' Set the title for the form.
        ''' </summary>
        form.Text = $"User Organisations - {username}"

        ''' <summary>
        ''' Setup the columns in the DataGridView.
        ''' </summary>
        Dim columnHeaders As New Dictionary(Of String, String) From {
            {"OrgCount", "Count"},
            {"OrgLogin", "Username"},
            {"OrgAvatar", "Avatar URL"},
            {"OrgID", "ID"},
            {"OrgNodeID", "Node ID"},
            {"OrgURL", "URL"},
            {"OrgAbout", "About"}
        }

        SetupDataGrid(form.DataGridViewUserOrgs, columnHeaders)

        Dim count As Integer = 0

        ''' <summary>
        ''' Populate the DataGridView rows with the search results' information.
        ''' </summary>
        For Each organisation As JObject In organisations
            count += 1
            Dim rowValues As New List(Of String) From {
                count,
                organisation("login")?.ToString(),
                organisation("avatar_url")?.ToString(),
                organisation("id")?.ToString(),
                organisation("node_id")?.ToString(),
                organisation("url")?.ToString(), organisation("description")?.ToString()
            }

            form.DataGridViewUserOrgs.Rows.Add(rowValues.ToArray())
        Next

        ''' <summary>
        ''' Show the form after populating the DataGridView.
        ''' </summary>
        form.Show()
    End Function


    Public Async Function LoadUserEvents(username As String, form As UserEventsForm) As Task
        Dim apiHandler As New ApiHandler()
        Dim events As JArray = Await apiHandler.UserEvents(username)

        If events Is Nothing OrElse events.Count = 0 Then
            MessageBox.Show("Unable to retrieve user events.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        UserEventsForm.Text = $"User Events = {username}"

        ' Clear the Columns and Rows before adding Items to them 
        UserEventsForm.DataGridViewUserEvents.Rows.Clear()
        UserEventsForm.DataGridViewUserEvents.Columns.Clear()

        UserEventsForm.DataGridViewUserEvents.Columns.Add("EventCount", "Count")
        UserEventsForm.DataGridViewUserEvents.Columns.Add("EventID", "ID")
        UserEventsForm.DataGridViewUserEvents.Columns.Add("EventActor", "Actor")
        UserEventsForm.DataGridViewUserEvents.Columns.Add("EventType", "Type")
        UserEventsForm.DataGridViewUserEvents.Columns.Add("EventRepository", "Repository")
        UserEventsForm.DataGridViewUserEvents.Columns.Add("EventPayload", "Payload")
        UserEventsForm.DataGridViewUserEvents.Columns.Add("EventCreatedAt", "Created At")

        Dim count As Integer = 0
        For Each user_event As JObject In events
            count += 1
            UserEventsForm.DataGridViewUserEvents.Rows.Add(count, user_event("id")?.ToString(), user_event("actor")("login")?.ToString(),
                                                        user_event("type")?.ToString(), user_event("repo")("name")?.ToString(),
                                                        user_event("payload")?.ToString(), user_event("created_at")?.ToString())
        Next

        UserEventsForm.Show()
    End Function


    Public Async Function LoadOrganisationRepositories(organisation As String, form As OrgReposForm) As Task
        ''' <summary>
        ''' Instantiate a new ApiHandler object for interacting with the GitHub API.
        ''' </summary>
        Dim apiHandler As New ApiHandler()
        Dim repos As JArray = Await apiHandler.OrgRepos(organisation)

        If repos Is Nothing OrElse repos.Count = 0 Then
            MessageBox.Show("Unable to retrieve user repositories.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        OrgReposForm.Text = $"📂 Organisation Repositories - {organisation}"

        ''' <summary>
        ''' Setup the DataGridView columns.
        ''' </summary>
        Dim columnHeaders As New Dictionary(Of String, String) From {
            {"RepoCount", "🔢 Count"},
            {"RepoName", " 👤 Name"},
            {"RepoID", "ID"},
            {"RepoAbout", "ℹ️ About"},
            {"RepoForks", "📂 Forks"},
            {"RepoStars", "🌟 Stars"},
            {"RepoWatchers", "👀 Watchers"},
            {"RepoLicense", "🗒️ License"},
            {"RepoDefaultBranch", "🌳 Default Branch"},
            {"RepoVisibility", "🫣 Visibility"},
            {"RepoLanguages", "🖥️ Language(s)"},
            {"RepoOpenIssues", "❗Open Issues"},
            {"RepoTopics", "❕Topics"},
            {"RepoHomepage", "🏠 Homepage"},
            {"RepoCloneUrl", "🌐 Clone URL"},
            {"RepoSSHUrl", "🌐 SSH URL"},
            {"RepoIsFork", "❔Is Fork?"},
            {"RepoIsForkable", "❔Is Forkable?"},
            {"RepoIsPrivate", "❔Is Private?"},
            {"RepoIsArchived", "❔Is Archived?"},
            {"RepoIsTemplate", "❔Is Template?"},
            {"RepoHasWiki", "❔Has Wiki?"},
            {"RepoHasPages", "❔Has Pages?"},
            {"RepoHasProjects", "❔Has Projects?"},
            {"RepoHasIssues", "❔Has Issues?"},
            {"RepoHasDownloads", "❔Has Downloads?"},
            {"RepoPushedAt", "📅 Pushed At"},
            {"RepoCreatedAt", "📅 Created At"},
            {"RepoUpdatedAt", "📅 Updated At"}
        }

        ''' <summary>
        ''' Call SetupDataGrid to initialize DataGridView.
        ''' </summary>
        SetupDataGrid(form.DataGridViewOrgRepos, columnHeaders)

        Dim count As Integer = 0

        ''' <summary>
        ''' Iterate through each repository to populate DataGridView rows.
        ''' </summary>
        For Each repo As JObject In repos
            count += 1
            Dim rowValues As New List(Of String) From {
                count.ToString(),
                repo("name")?.ToString(),
                repo("id")?.ToString(),
                repo("description")?.ToString(),
                repo("forks")?.ToString(),
                repo("stargazers_count")?.ToString(),
                repo("watchers")?.ToString(),
                If(repo("license").Type <> JTokenType.Null, repo("license")("name")?.ToString(), "Not Found"),
                repo("default_branch")?.ToString(),
                repo("visibility")?.ToString(),
                repo("language")?.ToString(),
                repo("open_issues")?.ToString(),
                repo("topics")?.ToString(),
                repo("homepage")?.ToString(),
                repo("clone_url")?.ToString(),
                repo("ssh_url")?.ToString(),
                repo("fork")?.ToString(),
                repo("allow_forking")?.ToString(),
                repo("private")?.ToString(),
                repo("archived")?.ToString(),
                repo("is_template")?.ToString(),
                repo("has_wiki")?.ToString(),
                repo("has_pages")?.ToString(),
                repo("has_projects")?.ToString(),
                repo("has_issues")?.ToString(),
                repo("has_downloads")?.ToString(),
                repo("pushed_at")?.ToString(),
                repo("created_at")?.ToString(),
                repo("updated_at")?.ToString()
            }

            form.DataGridViewOrgRepos.Rows.Add(rowValues.ToArray())
        Next

        ''' <summary>
        ''' Show the form after populating the DataGridView.
        ''' </summary>
        form.Show()
    End Function


    Public Async Function HandleCheckingUpdates(current_version As Version) As Task
        ''' <summary>
        ''' Instantiate a new ApiHandler object for interacting with the GitHub API.
        ''' </summary>
        Dim apiHandler As New ApiHandler()
        Dim data As JObject = Await apiHandler.CheckUpdates()

        If data Is Nothing Then
            MessageBox.Show("Unable to retrieve updates.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        If data("tag_name").ToString = $"{current_version}" Then
            MessageBox.Show($"You're running the current version v{My.Application.Info.Version} of {My.Application.Info.ProductName}. Check again soon! :)",
                        "Information", MessageBoxButtons.OK, MessageBoxIcon.Information)
        Else
            Dim confirm As DialogResult = MessageBox.Show($"A new version v{data("tag_name")} of {My.Application.Info.ProductName} is available, would you like to get it?

What's new in v{data("tag_name")}?
{data("body")}
", "Update", MessageBoxButtons.YesNo, MessageBoxIcon.Question)

            If confirm = DialogResult.Yes Then
                Shell($"cmd /c start https://github.com/bellingcat/octosuite/releases/tag/{data("tag_name")}")
            End If
        End If
    End Function


    Public Sub HandleLogFirstLaunch(license_text As String)
        Dim filePath As String = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "Octosuite GUI", "logs", "launched.log")

        If Not File.Exists(filePath) Then
            MessageBox.Show(license_text, "License", MessageBoxButtons.OK, MessageBoxIcon.Information)

            Dim textToWrite As String = $"
{My.Application.Info.AssemblyName}
---------

User: {Environment.UserName}
Host: {Environment.MachineName}
OS: {Environment.OSVersion}
Is x64?: {Environment.Is64BitOperatingSystem}
First launched on: {DateTime.Now}"

            File.WriteAllText(filePath, textToWrite)
        End If
    End Sub


    Public Sub HandlePathFinding()
        Dim directoryPath As String = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "Octosuite GUI", "logs")

        If Not Directory.Exists(directoryPath) Then
            Directory.CreateDirectory(directoryPath)
        End If
    End Sub
End Class
