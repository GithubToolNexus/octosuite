<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class UserReposForm
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
        Dim resources As ComponentModel.ComponentResourceManager = New ComponentModel.ComponentResourceManager(GetType(UserReposForm))
        DataGridViewUserRepos = New DataGridView()
        CType(DataGridViewUserRepos, ComponentModel.ISupportInitialize).BeginInit()
        SuspendLayout()
        ' 
        ' DataGridViewUserRepos
        ' 
        DataGridViewUserRepos.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize
        DataGridViewUserRepos.Dock = DockStyle.Fill
        DataGridViewUserRepos.Location = New Point(0, 0)
        DataGridViewUserRepos.Name = "DataGridViewUserRepos"
        DataGridViewUserRepos.ReadOnly = True
        DataGridViewUserRepos.RowHeadersVisible = False
        DataGridViewUserRepos.RowTemplate.Height = 25
        DataGridViewUserRepos.Size = New Size(755, 450)
        DataGridViewUserRepos.TabIndex = 0
        ' 
        ' UserReposForm
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(755, 450)
        Controls.Add(DataGridViewUserRepos)
        Icon = CType(resources.GetObject("$this.Icon"), Icon)
        Name = "UserReposForm"
        ShowIcon = False
        StartPosition = FormStartPosition.CenterScreen
        Text = "UserReposForm"
        CType(DataGridViewUserRepos, ComponentModel.ISupportInitialize).EndInit()
        ResumeLayout(False)
    End Sub

    Friend WithEvents DataGridViewUserRepos As DataGridView
End Class
