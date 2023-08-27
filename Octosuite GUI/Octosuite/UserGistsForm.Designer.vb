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
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(UserGistsForm))
        Me.DataGridViewUserGists = New System.Windows.Forms.DataGridView()
        CType(Me.DataGridViewUserGists, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'DataGridViewUserGists
        '
        Me.DataGridViewUserGists.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.DataGridViewUserGists.Dock = System.Windows.Forms.DockStyle.Fill
        Me.DataGridViewUserGists.Location = New System.Drawing.Point(0, 0)
        Me.DataGridViewUserGists.Name = "DataGridViewUserGists"
        Me.DataGridViewUserGists.ReadOnly = True
        Me.DataGridViewUserGists.RowTemplate.Height = 25
        Me.DataGridViewUserGists.Size = New System.Drawing.Size(1042, 309)
        Me.DataGridViewUserGists.TabIndex = 1
        '
        'UserGistsForm
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(7.0!, 15.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(1042, 309)
        Me.Controls.Add(Me.DataGridViewUserGists)
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.Name = "UserGistsForm"
        Me.Text = "Octosuite - User:Gists"
        CType(Me.DataGridViewUserGists, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)

    End Sub

    Friend WithEvents DataGridViewUserGists As DataGridView
End Class
