<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class StartForm
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Dim resources As ComponentModel.ComponentResourceManager = New ComponentModel.ComponentResourceManager(GetType(StartForm))
        MenuStrip1 = New MenuStrip()
        ToolsToolStripMenuItem = New ToolStripMenuItem()
        LogsToolStripMenuItem = New ToolStripMenuItem()
        AboutToolStripMenuItem = New ToolStripMenuItem()
        DeveloperToolStripMenuItem = New ToolStripMenuItem()
        CheckUpdatesToolStripMenuItem = New ToolStripMenuItem()
        ToolStripSeparator1 = New ToolStripSeparator()
        ExitToolStripMenuItem = New ToolStripMenuItem()
        DiscoveryToolStripMenuItem = New ToolStripMenuItem()
        SearchUsersToolStripMenuItem = New ToolStripMenuItem()
        SearchRepositoriesToolStripMenuItem1 = New ToolStripMenuItem()
        SearchTopicsToolStripMenuItem = New ToolStripMenuItem()
        SearchIssuesToolStripMenuItem = New ToolStripMenuItem()
        InvestigationToolStripMenuItem = New ToolStripMenuItem()
        UserToolStripMenuItem = New ToolStripMenuItem()
        UserProfileToolStripMenuItem = New ToolStripMenuItem()
        UserFollowsToolStripMenuItem = New ToolStripMenuItem()
        UserFollowingToolStripMenuItem = New ToolStripMenuItem()
        UserFollowersToolStripMenuItem = New ToolStripMenuItem()
        GistsToolStripMenuItem = New ToolStripMenuItem()
        UserEventsToolStripMenuItem = New ToolStripMenuItem()
        UserRepositoriesToolStripMenuItem = New ToolStripMenuItem()
        UserSubscriptionsToolStripMenuItem = New ToolStripMenuItem()
        UserOrganisationsToolStripMenuItem = New ToolStripMenuItem()
        RepositoriesToolStripMenuItem = New ToolStripMenuItem()
        OrganisationToolStripMenuItem = New ToolStripMenuItem()
        OrgProfileToolStripMenuItem1 = New ToolStripMenuItem()
        RepositoriesToolStripMenuItem1 = New ToolStripMenuItem()
        MenuStrip1.SuspendLayout()
        SuspendLayout()
        ' 
        ' MenuStrip1
        ' 
        MenuStrip1.Items.AddRange(New ToolStripItem() {ToolsToolStripMenuItem, DiscoveryToolStripMenuItem, InvestigationToolStripMenuItem})
        MenuStrip1.Location = New Point(0, 0)
        MenuStrip1.Name = "MenuStrip1"
        MenuStrip1.Size = New Size(301, 24)
        MenuStrip1.TabIndex = 0
        MenuStrip1.Text = "MenuStrip1"
        ' 
        ' ToolsToolStripMenuItem
        ' 
        ToolsToolStripMenuItem.DropDownItems.AddRange(New ToolStripItem() {LogsToolStripMenuItem, AboutToolStripMenuItem, DeveloperToolStripMenuItem, CheckUpdatesToolStripMenuItem, ToolStripSeparator1, ExitToolStripMenuItem})
        ToolsToolStripMenuItem.Image = CType(resources.GetObject("ToolsToolStripMenuItem.Image"), Image)
        ToolsToolStripMenuItem.Name = "ToolsToolStripMenuItem"
        ToolsToolStripMenuItem.Size = New Size(98, 20)
        ToolsToolStripMenuItem.Text = "CurrentUser"
        ToolsToolStripMenuItem.ToolTipText = "Logs management"
        ' 
        ' LogsToolStripMenuItem
        ' 
        LogsToolStripMenuItem.AutoToolTip = True
        LogsToolStripMenuItem.Enabled = False
        LogsToolStripMenuItem.Image = CType(resources.GetObject("LogsToolStripMenuItem.Image"), Image)
        LogsToolStripMenuItem.Name = "LogsToolStripMenuItem"
        LogsToolStripMenuItem.Size = New Size(152, 22)
        LogsToolStripMenuItem.Text = "Logs"
        LogsToolStripMenuItem.ToolTipText = vbCrLf
        ' 
        ' AboutToolStripMenuItem
        ' 
        AboutToolStripMenuItem.AutoToolTip = True
        AboutToolStripMenuItem.Image = CType(resources.GetObject("AboutToolStripMenuItem.Image"), Image)
        AboutToolStripMenuItem.Name = "AboutToolStripMenuItem"
        AboutToolStripMenuItem.Size = New Size(152, 22)
        AboutToolStripMenuItem.Text = "About"
        ' 
        ' DeveloperToolStripMenuItem
        ' 
        DeveloperToolStripMenuItem.AutoToolTip = True
        DeveloperToolStripMenuItem.Image = CType(resources.GetObject("DeveloperToolStripMenuItem.Image"), Image)
        DeveloperToolStripMenuItem.Name = "DeveloperToolStripMenuItem"
        DeveloperToolStripMenuItem.Size = New Size(152, 22)
        DeveloperToolStripMenuItem.Text = "Developer"
        ' 
        ' CheckUpdatesToolStripMenuItem
        ' 
        CheckUpdatesToolStripMenuItem.Image = CType(resources.GetObject("CheckUpdatesToolStripMenuItem.Image"), Image)
        CheckUpdatesToolStripMenuItem.Name = "CheckUpdatesToolStripMenuItem"
        CheckUpdatesToolStripMenuItem.Size = New Size(152, 22)
        CheckUpdatesToolStripMenuItem.Text = "Check updates"
        CheckUpdatesToolStripMenuItem.ToolTipText = "Check program updates"
        ' 
        ' ToolStripSeparator1
        ' 
        ToolStripSeparator1.Name = "ToolStripSeparator1"
        ToolStripSeparator1.Size = New Size(149, 6)
        ' 
        ' ExitToolStripMenuItem
        ' 
        ExitToolStripMenuItem.AutoToolTip = True
        ExitToolStripMenuItem.Image = CType(resources.GetObject("ExitToolStripMenuItem.Image"), Image)
        ExitToolStripMenuItem.Name = "ExitToolStripMenuItem"
        ExitToolStripMenuItem.Size = New Size(152, 22)
        ExitToolStripMenuItem.Text = "Quit"
        ' 
        ' DiscoveryToolStripMenuItem
        ' 
        DiscoveryToolStripMenuItem.DropDownItems.AddRange(New ToolStripItem() {SearchUsersToolStripMenuItem, SearchRepositoriesToolStripMenuItem1, SearchTopicsToolStripMenuItem, SearchIssuesToolStripMenuItem})
        DiscoveryToolStripMenuItem.Image = CType(resources.GetObject("DiscoveryToolStripMenuItem.Image"), Image)
        DiscoveryToolStripMenuItem.Name = "DiscoveryToolStripMenuItem"
        DiscoveryToolStripMenuItem.Size = New Size(86, 20)
        DiscoveryToolStripMenuItem.Text = "Discovery"
        ' 
        ' SearchUsersToolStripMenuItem
        ' 
        SearchUsersToolStripMenuItem.Name = "SearchUsersToolStripMenuItem"
        SearchUsersToolStripMenuItem.Size = New Size(138, 22)
        SearchUsersToolStripMenuItem.Text = "Users"
        ' 
        ' SearchRepositoriesToolStripMenuItem1
        ' 
        SearchRepositoriesToolStripMenuItem1.Name = "SearchRepositoriesToolStripMenuItem1"
        SearchRepositoriesToolStripMenuItem1.Size = New Size(138, 22)
        SearchRepositoriesToolStripMenuItem1.Text = "Repositories"
        ' 
        ' SearchTopicsToolStripMenuItem
        ' 
        SearchTopicsToolStripMenuItem.Name = "SearchTopicsToolStripMenuItem"
        SearchTopicsToolStripMenuItem.Size = New Size(138, 22)
        SearchTopicsToolStripMenuItem.Text = "Topics"
        ' 
        ' SearchIssuesToolStripMenuItem
        ' 
        SearchIssuesToolStripMenuItem.Name = "SearchIssuesToolStripMenuItem"
        SearchIssuesToolStripMenuItem.Size = New Size(138, 22)
        SearchIssuesToolStripMenuItem.Text = "Issues"
        ' 
        ' InvestigationToolStripMenuItem
        ' 
        InvestigationToolStripMenuItem.DropDownItems.AddRange(New ToolStripItem() {UserToolStripMenuItem, RepositoriesToolStripMenuItem, OrganisationToolStripMenuItem})
        InvestigationToolStripMenuItem.Image = CType(resources.GetObject("InvestigationToolStripMenuItem.Image"), Image)
        InvestigationToolStripMenuItem.Name = "InvestigationToolStripMenuItem"
        InvestigationToolStripMenuItem.Size = New Size(103, 20)
        InvestigationToolStripMenuItem.Text = "Investigation"
        ' 
        ' UserToolStripMenuItem
        ' 
        UserToolStripMenuItem.DropDownItems.AddRange(New ToolStripItem() {UserProfileToolStripMenuItem, UserFollowsToolStripMenuItem, UserFollowingToolStripMenuItem, UserFollowersToolStripMenuItem, GistsToolStripMenuItem, UserEventsToolStripMenuItem, UserRepositoriesToolStripMenuItem, UserSubscriptionsToolStripMenuItem, UserOrganisationsToolStripMenuItem})
        UserToolStripMenuItem.Image = CType(resources.GetObject("UserToolStripMenuItem.Image"), Image)
        UserToolStripMenuItem.Name = "UserToolStripMenuItem"
        UserToolStripMenuItem.Size = New Size(147, 22)
        UserToolStripMenuItem.Text = "Users"
        UserToolStripMenuItem.ToolTipText = "Investigate a user"
        ' 
        ' UserProfileToolStripMenuItem
        ' 
        UserProfileToolStripMenuItem.Image = CType(resources.GetObject("UserProfileToolStripMenuItem.Image"), Image)
        UserProfileToolStripMenuItem.Name = "UserProfileToolStripMenuItem"
        UserProfileToolStripMenuItem.Size = New Size(147, 22)
        UserProfileToolStripMenuItem.Text = "Profile"
        UserProfileToolStripMenuItem.ToolTipText = "Get user profile"
        ' 
        ' UserFollowsToolStripMenuItem
        ' 
        UserFollowsToolStripMenuItem.Image = CType(resources.GetObject("UserFollowsToolStripMenuItem.Image"), Image)
        UserFollowsToolStripMenuItem.Name = "UserFollowsToolStripMenuItem"
        UserFollowsToolStripMenuItem.Size = New Size(147, 22)
        UserFollowsToolStripMenuItem.Text = "Follows"
        UserFollowsToolStripMenuItem.ToolTipText = "Check whether or not User A follows User B"
        ' 
        ' UserFollowingToolStripMenuItem
        ' 
        UserFollowingToolStripMenuItem.Image = CType(resources.GetObject("UserFollowingToolStripMenuItem.Image"), Image)
        UserFollowingToolStripMenuItem.Name = "UserFollowingToolStripMenuItem"
        UserFollowingToolStripMenuItem.Size = New Size(147, 22)
        UserFollowingToolStripMenuItem.Text = "Following"
        UserFollowingToolStripMenuItem.ToolTipText = "Get accouhnts that a user follows"
        ' 
        ' UserFollowersToolStripMenuItem
        ' 
        UserFollowersToolStripMenuItem.Image = CType(resources.GetObject("UserFollowersToolStripMenuItem.Image"), Image)
        UserFollowersToolStripMenuItem.Name = "UserFollowersToolStripMenuItem"
        UserFollowersToolStripMenuItem.Size = New Size(147, 22)
        UserFollowersToolStripMenuItem.Text = "Followers"
        UserFollowersToolStripMenuItem.ToolTipText = "Get user followers"
        ' 
        ' GistsToolStripMenuItem
        ' 
        GistsToolStripMenuItem.Enabled = False
        GistsToolStripMenuItem.Image = CType(resources.GetObject("GistsToolStripMenuItem.Image"), Image)
        GistsToolStripMenuItem.Name = "GistsToolStripMenuItem"
        GistsToolStripMenuItem.Size = New Size(147, 22)
        GistsToolStripMenuItem.Text = "Gists"
        GistsToolStripMenuItem.ToolTipText = "Get user gists"
        ' 
        ' UserEventsToolStripMenuItem
        ' 
        UserEventsToolStripMenuItem.Image = CType(resources.GetObject("UserEventsToolStripMenuItem.Image"), Image)
        UserEventsToolStripMenuItem.Name = "UserEventsToolStripMenuItem"
        UserEventsToolStripMenuItem.Size = New Size(147, 22)
        UserEventsToolStripMenuItem.Text = "Events"
        UserEventsToolStripMenuItem.ToolTipText = "Get user events"
        ' 
        ' UserRepositoriesToolStripMenuItem
        ' 
        UserRepositoriesToolStripMenuItem.Image = CType(resources.GetObject("UserRepositoriesToolStripMenuItem.Image"), Image)
        UserRepositoriesToolStripMenuItem.Name = "UserRepositoriesToolStripMenuItem"
        UserRepositoriesToolStripMenuItem.Size = New Size(147, 22)
        UserRepositoriesToolStripMenuItem.Text = "Repositories"
        UserRepositoriesToolStripMenuItem.ToolTipText = "Get user repositories"
        ' 
        ' UserSubscriptionsToolStripMenuItem
        ' 
        UserSubscriptionsToolStripMenuItem.Image = CType(resources.GetObject("UserSubscriptionsToolStripMenuItem.Image"), Image)
        UserSubscriptionsToolStripMenuItem.Name = "UserSubscriptionsToolStripMenuItem"
        UserSubscriptionsToolStripMenuItem.Size = New Size(147, 22)
        UserSubscriptionsToolStripMenuItem.Text = "Subscriptions"
        UserSubscriptionsToolStripMenuItem.ToolTipText = "Get user subscriptions (starred repositories)"
        ' 
        ' UserOrganisationsToolStripMenuItem
        ' 
        UserOrganisationsToolStripMenuItem.Image = CType(resources.GetObject("UserOrganisationsToolStripMenuItem.Image"), Image)
        UserOrganisationsToolStripMenuItem.Name = "UserOrganisationsToolStripMenuItem"
        UserOrganisationsToolStripMenuItem.Size = New Size(147, 22)
        UserOrganisationsToolStripMenuItem.Text = "Organisations"
        UserOrganisationsToolStripMenuItem.ToolTipText = "Get user organisations"
        ' 
        ' RepositoriesToolStripMenuItem
        ' 
        RepositoriesToolStripMenuItem.Name = "RepositoriesToolStripMenuItem"
        RepositoriesToolStripMenuItem.Size = New Size(147, 22)
        RepositoriesToolStripMenuItem.Text = "Repositories"
        ' 
        ' OrganisationToolStripMenuItem
        ' 
        OrganisationToolStripMenuItem.DropDownItems.AddRange(New ToolStripItem() {OrgProfileToolStripMenuItem1, RepositoriesToolStripMenuItem1})
        OrganisationToolStripMenuItem.Image = CType(resources.GetObject("OrganisationToolStripMenuItem.Image"), Image)
        OrganisationToolStripMenuItem.Name = "OrganisationToolStripMenuItem"
        OrganisationToolStripMenuItem.Size = New Size(147, 22)
        OrganisationToolStripMenuItem.Text = "Organisations"
        OrganisationToolStripMenuItem.ToolTipText = "Investigate an organisation"
        ' 
        ' OrgProfileToolStripMenuItem1
        ' 
        OrgProfileToolStripMenuItem1.Image = CType(resources.GetObject("OrgProfileToolStripMenuItem1.Image"), Image)
        OrgProfileToolStripMenuItem1.Name = "OrgProfileToolStripMenuItem1"
        OrgProfileToolStripMenuItem1.Size = New Size(138, 22)
        OrgProfileToolStripMenuItem1.Text = "Profile"
        OrgProfileToolStripMenuItem1.ToolTipText = "Get an organisation's profile"
        ' 
        ' RepositoriesToolStripMenuItem1
        ' 
        RepositoriesToolStripMenuItem1.Image = CType(resources.GetObject("RepositoriesToolStripMenuItem1.Image"), Image)
        RepositoriesToolStripMenuItem1.Name = "RepositoriesToolStripMenuItem1"
        RepositoriesToolStripMenuItem1.Size = New Size(138, 22)
        RepositoriesToolStripMenuItem1.Text = "Repositories"
        ' 
        ' StartForm
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        BackColor = SystemColors.ButtonFace
        ClientSize = New Size(301, 27)
        Controls.Add(MenuStrip1)
        FormBorderStyle = FormBorderStyle.FixedSingle
        Icon = CType(resources.GetObject("$this.Icon"), Icon)
        MainMenuStrip = MenuStrip1
        MaximizeBox = False
        Name = "StartForm"
        StartPosition = FormStartPosition.CenterScreen
        Text = "Octosuite GUI"
        MenuStrip1.ResumeLayout(False)
        MenuStrip1.PerformLayout()
        ResumeLayout(False)
        PerformLayout()
    End Sub

    Friend WithEvents MenuStrip1 As MenuStrip
    Friend WithEvents ToolsToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents LogsToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents AboutToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents DeveloperToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents ToolStripSeparator1 As ToolStripSeparator
    Friend WithEvents ExitToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents InvestigationToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents UserToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents UserProfileToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents UserRepositoriesToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents GistsToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents UserSubscriptionsToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents UserFollowersToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents UserFollowingToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents UserFollowsToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents UserOrganisationsToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents UserEventsToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents OrganisationToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents OrgProfileToolStripMenuItem1 As ToolStripMenuItem
    Friend WithEvents CheckUpdatesToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents SystemRAMLabel As Label
    Friend WithEvents OSNameLabel As Label
    Friend WithEvents RepositoriesToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents DiscoveryToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents SearchUsersToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents SearchRepositoriesToolStripMenuItem1 As ToolStripMenuItem
    Friend WithEvents SearchTopicsToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents SearchIssuesToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents RepositoriesToolStripMenuItem1 As ToolStripMenuItem
End Class
