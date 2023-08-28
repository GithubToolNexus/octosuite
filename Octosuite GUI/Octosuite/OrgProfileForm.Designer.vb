<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class OrgProfileForm
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
        Dim DataGridViewCellStyle1 As DataGridViewCellStyle = New DataGridViewCellStyle()
        DataGridOrgProfile = New DataGridView()
        CType(DataGridOrgProfile, ComponentModel.ISupportInitialize).BeginInit()
        SuspendLayout()
        ' 
        ' DataGridOrgProfile
        ' 
        DataGridOrgProfile.AllowUserToAddRows = False
        DataGridOrgProfile.AllowUserToDeleteRows = False
        DataGridViewCellStyle1.BackColor = Color.White
        DataGridOrgProfile.AlternatingRowsDefaultCellStyle = DataGridViewCellStyle1
        DataGridOrgProfile.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill
        DataGridOrgProfile.BackgroundColor = Color.White
        DataGridOrgProfile.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize
        DataGridOrgProfile.ColumnHeadersVisible = False
        DataGridOrgProfile.Dock = DockStyle.Fill
        DataGridOrgProfile.EnableHeadersVisualStyles = False
        DataGridOrgProfile.Location = New Point(0, 0)
        DataGridOrgProfile.Name = "DataGridOrgProfile"
        DataGridOrgProfile.ReadOnly = True
        DataGridOrgProfile.RowHeadersVisible = False
        DataGridOrgProfile.RowTemplate.Height = 25
        DataGridOrgProfile.Size = New Size(715, 450)
        DataGridOrgProfile.TabIndex = 2
        ' 
        ' OrgProfileForm
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(715, 450)
        Controls.Add(DataGridOrgProfile)
        FormBorderStyle = FormBorderStyle.FixedSingle
        MaximizeBox = False
        Name = "OrgProfileForm"
        ShowIcon = False
        StartPosition = FormStartPosition.CenterScreen
        Text = "OrgProfileForm"
        CType(DataGridOrgProfile, ComponentModel.ISupportInitialize).EndInit()
        ResumeLayout(False)
    End Sub

    Friend WithEvents DataGridOrgProfile As DataGridView
End Class
