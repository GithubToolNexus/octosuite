<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class OrgReposForm
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
        DataGridViewOrgRepos = New DataGridView()
        CType(DataGridViewOrgRepos, ComponentModel.ISupportInitialize).BeginInit()
        SuspendLayout()
        ' 
        ' DataGridViewOrgRepos
        ' 
        DataGridViewOrgRepos.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells
        DataGridViewOrgRepos.AutoSizeRowsMode = DataGridViewAutoSizeRowsMode.AllCellsExceptHeaders
        DataGridViewOrgRepos.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize
        DataGridViewOrgRepos.Dock = DockStyle.Fill
        DataGridViewOrgRepos.EnableHeadersVisualStyles = False
        DataGridViewOrgRepos.Location = New Point(0, 0)
        DataGridViewOrgRepos.Name = "DataGridViewOrgRepos"
        DataGridViewOrgRepos.ReadOnly = True
        DataGridViewOrgRepos.RowHeadersVisible = False
        DataGridViewOrgRepos.RowTemplate.Height = 25
        DataGridViewOrgRepos.Size = New Size(800, 450)
        DataGridViewOrgRepos.TabIndex = 5
        ' 
        ' OrgReposForm
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(800, 450)
        Controls.Add(DataGridViewOrgRepos)
        Name = "OrgReposForm"
        Text = "OrgReposForm"
        CType(DataGridViewOrgRepos, ComponentModel.ISupportInitialize).EndInit()
        ResumeLayout(False)
    End Sub

    Friend WithEvents DataGridViewOrgRepos As DataGridView
End Class
