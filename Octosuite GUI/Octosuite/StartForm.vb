Public Class StartForm

    Private Sub MainWindow_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Dim handler As New DataGridViewHandler()

        Me.Text = My.Application.Info.AssemblyName
        ToolsToolStripMenuItem.Text = $"👤{Environment.UserName}"

        handler.HandlePathFinding()
        handler.HandleLogFirstLaunch(AboutBox.LicenseText)
    End Sub

    Private Sub ExitToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles ExitToolStripMenuItem.Click
        Dim result As DialogResult = MessageBox.Show("This will close the program, continue?", "Quit", MessageBoxButtons.YesNo, MessageBoxIcon.Question)
        If result = DialogResult.Yes Then
            Me.Close()
        End If
    End Sub


    Private Async Sub UserProfileToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles UserProfileToolStripMenuItem.Click
        Dim username As String = InputBox("", "Username")
        If String.IsNullOrEmpty(username) Then
            MessageBox.Show("Please enter a valid username.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If
        Dim handler As New DataGridViewHandler()
        Await handler.LoadUserProfile(username:=username, form:=UserProfileForm)
    End Sub


    Private Async Sub UserRepositoriesToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles UserRepositoriesToolStripMenuItem.Click
        Dim username As String = InputBox("", "Username")
        If String.IsNullOrEmpty(username) Then
            MessageBox.Show("Please enter a valid username.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If
        Dim handler As New DataGridViewHandler()
        Await handler.LoadUserRepositories(username:=username, form:=UserReposForm)
    End Sub


    Private Async Sub UserSubscriptionsToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles UserSubscriptionsToolStripMenuItem.Click
        Dim username As String = InputBox("", "Username")
        If String.IsNullOrEmpty(username) Then
            MessageBox.Show("Please enter a valid username.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If
        Dim handler As New DataGridViewHandler()
        Await handler.LoadUserSubscriptions(username:=username, form:=UserSubscriptionsForm)
    End Sub


    Private Async Sub UserFollowingToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles UserFollowingToolStripMenuItem.Click
        Dim username As String = InputBox("", "Username")
        If String.IsNullOrEmpty(username) Then
            MessageBox.Show("Please enter a valid username.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If
        Dim handler As New DataGridViewHandler()
        Await handler.LoadUserFollowing(username:=username, form:=UserFollowingForm)
    End Sub


    Private Async Sub UserFollowersToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles UserFollowersToolStripMenuItem.Click
        Dim username As String = InputBox("", "Username")
        If String.IsNullOrEmpty(username) Then
            MessageBox.Show("Please enter a valid username.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If
        Dim handler As New DataGridViewHandler()
        Await handler.LoadUserFollowers(username:=username, form:=UserFollowersForm)
    End Sub


    Private Async Sub UserFollowsToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles UserFollowsToolStripMenuItem.Click
        Dim user_a As String = InputBox("", "User A (username)")
        Dim user_b As String = InputBox("", "User B (username)")
        If String.IsNullOrEmpty(user_a) OrElse String.IsNullOrEmpty(user_b) Then
            MessageBox.Show("Please enter valid usernames.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If
        Dim handler As New DataGridViewHandler()
        Await handler.CheckIfUserFollows(user_a:=user_a, user_b:=user_b)
    End Sub


    Private Async Sub UserOrganisationsToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles UserOrganisationsToolStripMenuItem.Click
        Dim username As String = InputBox("", "Username")
        If String.IsNullOrEmpty(username) Then
            MessageBox.Show("Please enter a valid username.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If
        Dim handler As New DataGridViewHandler()
        Await handler.LoadUserOrganisations(username:=username, form:=UserOrgsForm)
    End Sub


    Private Async Sub UserEventsToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles UserEventsToolStripMenuItem.Click
        Dim username As String = InputBox("", "Username")
        If String.IsNullOrEmpty(username) Then
            MessageBox.Show("Please enter a valid username.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If
        Dim handler As New DataGridViewHandler()
        Await handler.LoadUserEvents(username:=username, form:=UserEventsForm)
    End Sub


    Private Async Sub OrgProfileToolStripMenuItem1_Click(sender As Object, e As EventArgs) Handles OrgProfileToolStripMenuItem1.Click
        Dim org_username As String = InputBox("", "Organisation (username)")
        If String.IsNullOrEmpty(org_username) Then
            MessageBox.Show("Please enter a valid organisation username.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If
        Dim handler As New DataGridViewHandler()
        Await handler.LoadOrganisationProfile(organisation:=org_username, form:=OrgProfileForm)
    End Sub


    Private Sub AboutToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles AboutToolStripMenuItem.Click
        AboutBox.Show()
    End Sub


    Private Sub DeveloperToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles DeveloperToolStripMenuItem.Click
        DeveloperForm.ShowDialog()
    End Sub


    Private Async Sub CheckUpdatesToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles CheckUpdatesToolStripMenuItem.Click
        Dim handler As New DataGridViewHandler()
        Await handler.HandleCheckingUpdates(My.Application.Info.Version)
    End Sub


    Private Async Sub RepositoriesToolStripMenuItem1_Click(sender As Object, e As EventArgs) Handles RepositoriesToolStripMenuItem1.Click
        Dim organisation As String = InputBox("", "Organisation (username)")
        If String.IsNullOrEmpty(organisation) Then
            MessageBox.Show("Please enter valid organisation username.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If
        Dim handler As New DataGridViewHandler()
        Await handler.LoadOrganisationRepositories(organisation:=organisation, form:=OrgReposForm)
    End Sub

    Private Async Sub SearchUsersToolStripMenuItem_Click(sender As Object, e As EventArgs) Handles SearchUsersToolStripMenuItem.Click
        Dim query As String = InputBox("", "Query (username)")
        If String.IsNullOrEmpty(query) Then
            MessageBox.Show("Please enter a valid query string.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If
        Dim handler As New DataGridViewHandler()
        Await handler.LoadUserSearchResults(query:=query, form:=UserSearchResultsForm)
    End Sub

    Private Async Sub SearchRepositoriesToolStripMenuItem1_Click(sender As Object, e As EventArgs) Handles SearchRepositoriesToolStripMenuItem1.Click
        Dim query As String = InputBox("", "Query (repository name)")
        If String.IsNullOrEmpty(query) Then
            MessageBox.Show("Please enter a valid query string.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            Return
        End If
        Dim handler As New DataGridViewHandler()
        Await handler.LoadRepoSearchResults(query:=query, form:=RepoSearchResultsForm)
    End Sub
End Class
