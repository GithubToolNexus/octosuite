<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class UserGistsForm
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
        Dim resources As ComponentModel.ComponentResourceManager = New ComponentModel.ComponentResourceManager(GetType(UserGistsForm))
        DataGridViewUserGists = New DataGridView()
        CType(DataGridViewUserGists, ComponentModel.ISupportInitialize).BeginInit()
        SuspendLayout()
        ' 
        ' DataGridViewUserGists
        ' 
        DataGridViewUserGists.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize
        DataGridViewUserGists.Dock = DockStyle.Fill
        DataGridViewUserGists.Location = New Point(0, 0)
        DataGridViewUserGists.Name = "DataGridViewUserGists"
        DataGridViewUserGists.ReadOnly = True
        DataGridViewUserGists.RowHeadersVisible = False
        DataGridViewUserGists.RowTemplate.Height = 25
        DataGridViewUserGists.Size = New Size(759, 309)
        DataGridViewUserGists.TabIndex = 1
        ' 
        ' UserGistsForm
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(759, 309)
        Controls.Add(DataGridViewUserGists)
        Icon = CType(resources.GetObject("$this.Icon"), Icon)
        Name = "UserGistsForm"
        ShowIcon = False
        StartPosition = FormStartPosition.CenterScreen
        Text = "UserGistsForm"
        CType(DataGridViewUserGists, ComponentModel.ISupportInitialize).EndInit()
        ResumeLayout(False)
    End Sub

    Friend WithEvents DataGridViewUserGists As DataGridView
End Class
