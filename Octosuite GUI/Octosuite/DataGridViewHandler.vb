Imports System.IO
Imports Newtonsoft.Json.Linq

Public Class DataGridViewHandler

    Public Async Function LoadUserProfile(username As String, form As UserProfileForm) As Task
        Dim apiHandler As New ApiHandler()
        Dim data As JObject = Await apiHandler.UserProfile(username)

        If data Is Nothing Then
            ' The API call failed or returned a null object. You might want to show an error message here.
            MessageBox.Show("Unable to retrieve user profile.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ' Clear the Columns and Rows before adding Items to them 
        UserProfileForm.DataGridUserProfile.Rows.Clear()
        UserProfileForm.DataGridUserProfile.Columns.Clear()

        ' Create Column and Row headers
        UserProfileForm.DataGridUserProfile.Columns.Add("Field", "Field")
        UserProfileForm.DataGridUserProfile.Columns.Add("Value", "Value")

        ' Add items to the Rows. Safely handle potential null values with the ?. operator.
        UserProfileForm.DataGridUserProfile.Rows.Add("Name", data("name")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("Avatar", data("avatar_url")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("Username", data("login")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("ID", data("id")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("Node ID", data("node_id")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("Bio", data("bio")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("Location", data("location")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("Followers", data("followers")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("Following", data("following")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("Twitter handle", data("twitter_username")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("Gists", data("public_gists")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("Repositories", data("public_repos")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("Organization", data("company")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("Is hirable?", data("hireable")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("Joined on", data("created_at")?.ToString())
        UserProfileForm.DataGridUserProfile.Rows.Add("Updated on", data("updated_at")?.ToString())

        UserProfileForm.Show()
    End Function


    Public Async Function LoadOrganisationProfile(org_username As String, form As OrgProfileForm) As Task
        Dim apiHandler As New ApiHandler()
        Dim data As JObject = Await apiHandler.OrgProfile(org_username)

        If data Is Nothing Then
            MessageBox.Show("Unable to retrieve organisation profile.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ' Clear the Columns and Rows before adding Items to them 
        OrgProfileForm.DataGridOrgProfile.Rows.Clear()
        OrgProfileForm.DataGridOrgProfile.Columns.Clear()

        ' Create Column and Row headers
        OrgProfileForm.DataGridOrgProfile.Columns.Add("Field", "Value")
        OrgProfileForm.DataGridOrgProfile.Columns.Add("Field", "Value")

        OrgProfileForm.DataGridOrgProfile.Rows.Add("Name", data("name").ToString)
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Avatar", data("avatar_url").ToString)
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Username", data("login").ToString)
        OrgProfileForm.DataGridOrgProfile.Rows.Add("ID", data("id"))
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Node ID", data("node_id").ToString)
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Email", data("email").ToString)
        OrgProfileForm.DataGridOrgProfile.Rows.Add("About", data("description").ToString)
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Location", data("location").ToString)
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Blog", data("blog").ToString)
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Followers", data("followers"))
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Following", data("following"))
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Twitter handle", data("twitter_username").ToString)
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Gists", data("public_gists").ToString)
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Repositories", data("public_repos"))
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Account Type", data("type").ToString)
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Is Verified?", data("is_verified"))
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Has Organisation Projects?", data("has_organization_projects").ToString)
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Has Repository Projects?", data("has_repository_projects").ToString)
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Joined on", data("created_at").ToString)
        OrgProfileForm.DataGridOrgProfile.Rows.Add("Updated on", data("updated_at").ToString)

        OrgProfileForm.Show()
    End Function


    Public Async Function LoadUserRepositories(username As String, form As UserReposForm) As Task
        Dim apiHandler As New ApiHandler()
        Dim repos As JArray = Await apiHandler.UserRepos(username)

        If repos Is Nothing OrElse repos.Count = 0 Then
            ' The API call failed or returned a null or empty array. You might want to show an error message here.
            MessageBox.Show("Unable to retrieve user repositories.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ' Clear the Columns and Rows before adding Items to them 
        UserReposForm.DataGridViewUserRepos.Rows.Clear()
        UserReposForm.DataGridViewUserRepos.Columns.Clear()

        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoCount", "Count")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoName", "Name")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoID", "ID")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoAbout", "About")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoForks", "Forks")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoStars", "Stars")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoWatchers", "Watchers")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoLicense", "License")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoDefaultBranch", "Default Branch")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoVisibility", "Visibility")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoLanguages", "Language(s)")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoOpenIssues", "Open Issues")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoTopics", "Topics")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoHomepage", "Homepage")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoCloneUrl", "Clone URL")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoSSHUrl", "SSH URL")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoIsFork", "Is Fork?")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoIsForkable", "Is Forkable?")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoIsPrivate", "Is Private?")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoIsArchived", "Is Archived?")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoIsTemplate", "Is Template?")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoHasWiki", "Has Wiki?")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoHasPages", "Has Pages?")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoHasProjects", "Has Projects?")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoHasIssues", "Has Issues?")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoHasDownloads", "Has Downloads?")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoPushedAt", "Pushed At")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoCreatedAt", "Created At")
        UserReposForm.DataGridViewUserRepos.Columns.Add("RepoUpdatedAt", "Update At")

        Dim count As Integer = 0
        For Each repo As JObject In repos
            count += 1
            ' Add items to the Rows. Safely handle potential null values with the ?. operator.
            UserReposForm.DataGridViewUserRepos.Rows.Add(count, repo("name")?.ToString(), repo("id")?.ToString(),
                                                         repo("description")?.ToString(), repo("forks")?.ToString(),
                                                         repo("stargazers_count")?.ToString(), repo("watchers")?.ToString(),
                                                         repo("license")?.ToString(), repo("default_branch")?.ToString(),
                                                         repo("visibility")?.ToString(), repo("language")?.ToString(),
                                                         repo("open_issues")?.ToString(), repo("topics")?.ToString(),
                                                         repo("homepage")?.ToString(), repo("clone_url")?.ToString(),
                                                         repo("ssh_url")?.ToString(), repo("fork")?.ToString(),
                                                         repo("allow_forking")?.ToString(), repo("private")?.ToString(),
                                                         repo("archived")?.ToString(), repo("is_template")?.ToString(),
                                                         repo("has_wiki")?.ToString(), repo("has_pages")?.ToString(),
                                                         repo("has_projects")?.ToString(), repo("has_issues")?.ToString(),
                                                         repo("has_downloads")?.ToString(), repo("pushed_at")?.ToString(),
                                                         repo("created_at")?.ToString(), repo("updated_at")?.ToString())
        Next

        UserReposForm.Show()
    End Function


    Public Async Function LoadUserSubscriptions(username As String, form As UserSubscriptionsForm) As Task
        Dim apiHandler As New ApiHandler()
        Dim subscriptions As JArray = Await apiHandler.UserSubscriptions(username)

        If subscriptions Is Nothing OrElse subscriptions.Count = 0 Then
            ' The API call failed or returned a null or empty array. You might want to show an error message here.
            MessageBox.Show("Unable to retrieve user subscriptions.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ' Clear the Columns and Rows before adding Items to them 
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Rows.Clear()
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Clear()

        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoCount", "Count")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoName", "Name")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoID", "ID")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoAbout", "About")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoForks", "Forks")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoStars", "Stars")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoWatchers", "Watchers")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoLicense", "License")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoDefaultBranch", "Default Branch")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoVisibility", "Visibility")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoLanguages", "Language(s)")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoOpenIssues", "Open Issues")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoTopics", "Topics")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoHomepage", "Homepage")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoCloneUrl", "Clone URL")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoSSHUrl", "SSH URL")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoIsFork", "Is Fork?")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoIsForkable", "Is Forkable?")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoIsPrivate", "Is Private?")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoIsArchived", "Is Archived?")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoIsTemplate", "Is Template?")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoHasWiki", "Has Wiki?")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoHasPages", "Has Pages?")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoHasProjects", "Has Projects?")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoHasIssues", "Has Issues?")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoHasDownloads", "Has Downloads?")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoPushedAt", "Pushed At")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoCreatedAt", "Created At")
        UserSubscriptionsForm.DataGridViewUserSubscriptions.Columns.Add("RepoUpdatedAt", "Update At")

        Dim count As Integer = 0
        For Each subscription As JObject In subscriptions
            count += 1
            ' Add items to the Rows. Safely handle potential null values with the ?. operator.
            UserSubscriptionsForm.DataGridViewUserSubscriptions.Rows.Add(count, subscription("full_name")?.ToString(), subscription("id")?.ToString(),
                                                                     subscription("description")?.ToString(), subscription("forks")?.ToString(),
                                                                     subscription("stargazers_count")?.ToString(), subscription("watchers")?.ToString(),
                                                                     subscription("license")?.ToString(), subscription("default_branch")?.ToString(),
                                                                     subscription("visibility")?.ToString(), subscription("language")?.ToString(),
                                                                     subscription("open_issues")?.ToString(), subscription("topics")?.ToString(),
                                                                     subscription("homepage")?.ToString(), subscription("clone_url")?.ToString(),
                                                                     subscription("ssh_url")?.ToString(), subscription("fork")?.ToString(),
                                                                     subscription("allow_forking")?.ToString(), subscription("private")?.ToString(),
                                                                     subscription("archived")?.ToString(), subscription("is_template")?.ToString(),
                                                                     subscription("has_wiki")?.ToString(), subscription("has_pages")?.ToString(),
                                                                     subscription("has_projects")?.ToString(), subscription("has_issues")?.ToString(),
                                                                     subscription("has_downloads")?.ToString(), subscription("pushed_at")?.ToString(),
                                                                     subscription("created_at")?.ToString(), subscription("updated_at")?.ToString())
        Next

        UserSubscriptionsForm.Show()
    End Function


    Public Async Function LoadUserFollowers(username As String, form As UserFollowersForm) As Task
        Dim apiHandler As New ApiHandler()
        Dim followers As JArray = Await apiHandler.UserFollowers(username)

        If followers Is Nothing OrElse followers.Count = 0 Then
            ' The API call failed or returned a null or empty array. You might want to show an error message here.
            MessageBox.Show("Unable to retrieve user followers.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ' Clear the Columns and Rows before adding Items to them 
        UserFollowersForm.DataGridViewUserFollowers.Rows.Clear()
        UserFollowersForm.DataGridViewUserFollowers.Columns.Clear()

        UserFollowersForm.DataGridViewUserFollowers.Columns.Add("FollowerCount", "Count")
        UserFollowersForm.DataGridViewUserFollowers.Columns.Add("FollowerLogin", "Username")
        UserFollowersForm.DataGridViewUserFollowers.Columns.Add("FollowerAvatar", "Avatar URL")
        UserFollowersForm.DataGridViewUserFollowers.Columns.Add("FollowerGravatarID", "Gravatar ID")
        UserFollowersForm.DataGridViewUserFollowers.Columns.Add("FollowerID", "ID")
        UserFollowersForm.DataGridViewUserFollowers.Columns.Add("FollowerNodeID", "Node ID")
        UserFollowersForm.DataGridViewUserFollowers.Columns.Add("FollowerAccountType", "Account Type")
        UserFollowersForm.DataGridViewUserFollowers.Columns.Add("FollowerIsSiteAdmin", "Is Site Admin?")
        UserFollowersForm.DataGridViewUserFollowers.Columns.Add("FollowerUrl", "URL")

        Dim count As Integer = 0
        For Each follower As JObject In followers
            count += 1
            ' Add items to the Rows. Safely handle potential null values with the ?. operator.
            UserFollowersForm.DataGridViewUserFollowers.Rows.Add(count, follower("login")?.ToString(), follower("avatar_url")?.ToString(),
                                                             follower("gravatar_id")?.ToString(), follower("id")?.ToString(), follower("node_id")?.ToString(),
                                                             follower("type")?.ToString(), follower("site_admin")?.ToString(), follower("html_url")?.ToString())
        Next

        UserFollowersForm.Show()
    End Function


    Public Async Function LoadUserFollowing(username As String, form As UserFollowingForm) As Task
        Dim apiHandler As New ApiHandler()
        Dim followings As JArray = Await apiHandler.UserFollowing(username)

        If followings Is Nothing OrElse followings.Count = 0 Then
            MessageBox.Show("Unable to retrieve user followings.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ' Clear the Columns and Rows before adding Items to them 
        UserFollowingForm.DataGridViewUserFollowing.Rows.Clear()
        UserFollowingForm.DataGridViewUserFollowing.Columns.Clear()

        UserFollowingForm.DataGridViewUserFollowing.Columns.Add("FollowerCount", "Count")
        UserFollowingForm.DataGridViewUserFollowing.Columns.Add("FollowerLogin", "Username")
        UserFollowingForm.DataGridViewUserFollowing.Columns.Add("FollowerAvatar", "Avatar URL")
        UserFollowingForm.DataGridViewUserFollowing.Columns.Add("FollowerGravatarID", "Gravatar ID")
        UserFollowingForm.DataGridViewUserFollowing.Columns.Add("FollowerID", "ID")
        UserFollowingForm.DataGridViewUserFollowing.Columns.Add("FollowerNodeID", "Node ID")
        UserFollowingForm.DataGridViewUserFollowing.Columns.Add("FollowerAccountType", "Account Type")
        UserFollowingForm.DataGridViewUserFollowing.Columns.Add("FollowerIsSiteAdmin", "Is Site Admin?")
        UserFollowingForm.DataGridViewUserFollowing.Columns.Add("FollowerUrl", "URL")

        Dim count As Integer = 0
        For Each following As JObject In followings
            count += 1
            UserFollowingForm.DataGridViewUserFollowing.Rows.Add(count, following("login")?.ToString(), following("avatar_url")?.ToString(),
                                                             following("gravatar_id")?.ToString(), following("id")?.ToString(),
                                                             following("node_id")?.ToString(), following("type")?.ToString(),
                                                             following("site_admin")?.ToString(), following("html_url")?.ToString())
        Next

        UserFollowingForm.Show()
    End Function


    Public Async Function CheckIfUserFollows(user_a As String, user_b As String) As Task
        Dim apiHandler As New ApiHandler()
        Dim follows As JArray = Await apiHandler.UserFollows(user_a, user_b)

        If follows Is Nothing Then
            MessageBox.Show("Unable to retrieve user following status.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        If follows.Count > 0 Then
            MessageBox.Show($"{user_a} follows {user_b}", "Follows", MessageBoxButtons.OK, MessageBoxIcon.Information)
        Else
            MessageBox.Show($"{user_a} does not follos {user_b}", "Doesn't Follow", MessageBoxButtons.OK, MessageBoxIcon.Exclamation)
        End If
    End Function


    Public Async Function LoadUserOrganisations(username As String, form As UserOrgsForm) As Task
        Dim apiHandler As New ApiHandler()
        Dim organisations As JArray = Await apiHandler.UserOrgs(username)

        If organisations Is Nothing OrElse organisations.Count = 0 Then
            MessageBox.Show("Unable to retrieve user organisations.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ' Clear the Columns and Rows before adding Items to them 
        UserOrgsForm.DataGridViewUserOrgs.Rows.Clear()
        UserOrgsForm.DataGridViewUserOrgs.Columns.Clear()

        UserOrgsForm.DataGridViewUserOrgs.Columns.Add("OrgCount", "Count")
        UserOrgsForm.DataGridViewUserOrgs.Columns.Add("OrgLogin", "Username")
        UserOrgsForm.DataGridViewUserOrgs.Columns.Add("OrgAvatar", "Avatar URL")
        UserOrgsForm.DataGridViewUserOrgs.Columns.Add("OrgID", "ID")
        UserOrgsForm.DataGridViewUserOrgs.Columns.Add("OrgNodeID", "Node ID")
        UserOrgsForm.DataGridViewUserOrgs.Columns.Add("OrgURL", "URL")
        UserOrgsForm.DataGridViewUserOrgs.Columns.Add("OrgAbout", "About")

        Dim count As Integer = 0
        For Each organisation As JObject In organisations
            count += 1
            UserOrgsForm.DataGridViewUserOrgs.Rows.Add(count, organisation("login")?.ToString(), organisation("avatar_url")?.ToString(),
                                                    organisation("id")?.ToString(), organisation("node_id")?.ToString(),
                                                    organisation("url")?.ToString(), organisation("description")?.ToString())
        Next

        UserOrgsForm.Show()
    End Function


    Public Async Function LoadUserEvents(username As String, form As UserEventsForm) As Task
        Dim apiHandler As New ApiHandler()
        Dim events As JArray = Await apiHandler.UserEvents(username)

        If events Is Nothing OrElse events.Count = 0 Then
            MessageBox.Show("Unable to retrieve user events.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

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
        Dim apiHandler As New ApiHandler()
        Dim repos As JArray = Await apiHandler.OrgRepos(organisation)

        If repos Is Nothing OrElse repos.Count = 0 Then
            ' The API call failed or returned a null or empty array. You might want to show an error message here.
            MessageBox.Show("Unable to retrieve user repositories.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If

        ' Clear the Columns and Rows before adding Items to them 
        OrgReposForm.DataGridViewOrgRepos.Rows.Clear()
        OrgReposForm.DataGridViewOrgRepos.Columns.Clear()

        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoCount", "Count")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoName", "Name")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoID", "ID")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoAbout", "About")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoForks", "Forks")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoStars", "Stars")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoWatchers", "Watchers")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoLicense", "License")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoDefaultBranch", "Default Branch")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoVisibility", "Visibility")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoLanguages", "Language(s)")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoOpenIssues", "Open Issues")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoTopics", "Topics")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoHomepage", "Homepage")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoCloneUrl", "Clone URL")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoSSHUrl", "SSH URL")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoIsFork", "Is Fork?")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoIsForkable", "Is Forkable?")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoIsPrivate", "Is Private?")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoIsArchived", "Is Archived?")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoIsTemplate", "Is Template?")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoHasWiki", "Has Wiki?")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoHasPages", "Has Pages?")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoHasProjects", "Has Projects?")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoHasIssues", "Has Issues?")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoHasDownloads", "Has Downloads?")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoPushedAt", "Pushed At")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoCreatedAt", "Created At")
        OrgReposForm.DataGridViewOrgRepos.Columns.Add("RepoUpdatedAt", "Update At")

        Dim count As Integer = 0
        For Each repo As JObject In repos
            count += 1
            ' Add items to the Rows. Safely handle potential null values with the ?. operator.
            OrgReposForm.DataGridViewOrgRepos.Rows.Add(count, repo("name")?.ToString(), repo("id")?.ToString(),
                                                         repo("description")?.ToString(), repo("forks")?.ToString(),
                                                         repo("stargazers_count")?.ToString(), repo("watchers")?.ToString(),
                                                         repo("license")?.ToString(), repo("default_branch")?.ToString(),
                                                         repo("visibility")?.ToString(), repo("language")?.ToString(),
                                                         repo("open_issues")?.ToString(), repo("topics")?.ToString(),
                                                         repo("homepage")?.ToString(), repo("clone_url")?.ToString(),
                                                         repo("ssh_url")?.ToString(), repo("fork")?.ToString(),
                                                         repo("allow_forking")?.ToString(), repo("private")?.ToString(),
                                                         repo("archived")?.ToString(), repo("is_template")?.ToString(),
                                                         repo("has_wiki")?.ToString(), repo("has_pages")?.ToString(),
                                                         repo("has_projects")?.ToString(), repo("has_issues")?.ToString(),
                                                         repo("has_downloads")?.ToString(), repo("pushed_at")?.ToString(),
                                                         repo("created_at")?.ToString(), repo("updated_at")?.ToString())
        Next

        OrgReposForm.Show()
    End Function


    Public Async Function HandleCheckingUpdates(current_version As Version) As Task
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
