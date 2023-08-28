<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class UserProfileForm
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
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
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Dim DataGridViewCellStyle2 As DataGridViewCellStyle = New DataGridViewCellStyle()
        Dim resources As ComponentModel.ComponentResourceManager = New ComponentModel.ComponentResourceManager(GetType(UserProfileForm))
        DataGridViewUserProfile = New DataGridView()
        CType(DataGridViewUserProfile, ComponentModel.ISupportInitialize).BeginInit()
        SuspendLayout()
        ' 
        ' DataGridViewUserProfile
        ' 
        DataGridViewUserProfile.AllowUserToAddRows = False
        DataGridViewUserProfile.AllowUserToDeleteRows = False
        DataGridViewCellStyle2.BackColor = Color.White
        DataGridViewUserProfile.AlternatingRowsDefaultCellStyle = DataGridViewCellStyle2
        DataGridViewUserProfile.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill
        DataGridViewUserProfile.BackgroundColor = Color.White
        DataGridViewUserProfile.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize
        DataGridViewUserProfile.ColumnHeadersVisible = False
        DataGridViewUserProfile.Dock = DockStyle.Fill
        DataGridViewUserProfile.EnableHeadersVisualStyles = False
        DataGridViewUserProfile.Location = New Point(0, 0)
        DataGridViewUserProfile.Name = "DataGridViewUserProfile"
        DataGridViewUserProfile.ReadOnly = True
        DataGridViewUserProfile.RowHeadersVisible = False
        DataGridViewUserProfile.RowTemplate.Height = 25
        DataGridViewUserProfile.Size = New Size(800, 428)
        DataGridViewUserProfile.TabIndex = 1
        ' 
        ' UserProfileForm
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(800, 428)
        Controls.Add(DataGridViewUserProfile)
        FormBorderStyle = FormBorderStyle.FixedSingle
        Icon = CType(resources.GetObject("$this.Icon"), Icon)
        MaximizeBox = False
        Name = "UserProfileForm"
        ShowIcon = False
        StartPosition = FormStartPosition.CenterScreen
        Text = "UserProfileForm"
        CType(DataGridViewUserProfile, ComponentModel.ISupportInitialize).EndInit()
        ResumeLayout(False)
    End Sub

    Friend WithEvents DataGridViewUserProfile As DataGridView
End Class
