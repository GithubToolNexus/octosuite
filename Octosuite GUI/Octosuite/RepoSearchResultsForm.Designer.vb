<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class RepoSearchResultsForm
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
        DataGridViewRepoSearchResults = New DataGridView()
        CType(DataGridViewRepoSearchResults, ComponentModel.ISupportInitialize).BeginInit()
        SuspendLayout()
        ' 
        ' DataGridViewRepoSearchResults
        ' 
        DataGridViewRepoSearchResults.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize
        DataGridViewRepoSearchResults.Dock = DockStyle.Fill
        DataGridViewRepoSearchResults.Location = New Point(0, 0)
        DataGridViewRepoSearchResults.Name = "DataGridViewRepoSearchResults"
        DataGridViewRepoSearchResults.ReadOnly = True
        DataGridViewRepoSearchResults.RowHeadersVisible = False
        DataGridViewRepoSearchResults.RowTemplate.Height = 25
        DataGridViewRepoSearchResults.Size = New Size(755, 450)
        DataGridViewRepoSearchResults.TabIndex = 2
        ' 
        ' RepoSearchResultsForm
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(755, 450)
        Controls.Add(DataGridViewRepoSearchResults)
        Name = "RepoSearchResultsForm"
        ShowIcon = False
        StartPosition = FormStartPosition.CenterScreen
        Text = "RepoSearchResultsForm"
        CType(DataGridViewRepoSearchResults, ComponentModel.ISupportInitialize).EndInit()
        ResumeLayout(False)
    End Sub

    Friend WithEvents DataGridViewRepoSearchResults As DataGridView
End Class
