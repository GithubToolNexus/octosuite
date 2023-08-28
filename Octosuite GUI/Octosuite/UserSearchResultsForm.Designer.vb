<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class UserSearchResultsForm
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
        DataGridViewUserSearchResults = New DataGridView()
        CType(DataGridViewUserSearchResults, ComponentModel.ISupportInitialize).BeginInit()
        SuspendLayout()
        ' 
        ' DataGridViewUserSearchResults
        ' 
        DataGridViewUserSearchResults.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize
        DataGridViewUserSearchResults.Dock = DockStyle.Fill
        DataGridViewUserSearchResults.Location = New Point(0, 0)
        DataGridViewUserSearchResults.Name = "DataGridViewUserSearchResults"
        DataGridViewUserSearchResults.ReadOnly = True
        DataGridViewUserSearchResults.RowHeadersVisible = False
        DataGridViewUserSearchResults.RowTemplate.Height = 25
        DataGridViewUserSearchResults.Size = New Size(722, 450)
        DataGridViewUserSearchResults.TabIndex = 3
        ' 
        ' UserSearchResultsForm
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(722, 450)
        Controls.Add(DataGridViewUserSearchResults)
        FormBorderStyle = FormBorderStyle.FixedSingle
        Name = "UserSearchResultsForm"
        ShowIcon = False
        StartPosition = FormStartPosition.CenterScreen
        Text = "UserSearchResultsForm"
        CType(DataGridViewUserSearchResults, ComponentModel.ISupportInitialize).EndInit()
        ResumeLayout(False)
    End Sub

    Friend WithEvents DataGridViewUserSearchResults As DataGridView
End Class
