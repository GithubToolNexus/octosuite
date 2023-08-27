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
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(UserReposForm))
        Me.DataGridViewUserRepos = New System.Windows.Forms.DataGridView()

        Me.DataGridViewUserRepos.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.DataGridViewUserRepos.Dock = System.Windows.Forms.DockStyle.Fill
        Me.DataGridViewUserRepos.Location = New System.Drawing.Point(0, 0)
        Me.DataGridViewUserRepos.Name = "DataGridViewUserRepos"
        Me.DataGridViewUserRepos.ReadOnly = True
        Me.DataGridViewUserRepos.RowTemplate.Height = 25
        Me.DataGridViewUserRepos.Size = New System.Drawing.Size(1221, 580)
        Me.DataGridViewUserRepos.TabIndex = 0

        Me.AutoScaleDimensions = New System.Drawing.SizeF(7.0!, 15.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(1221, 580)
        Me.Controls.Add(Me.DataGridViewUserRepos)
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.Text = "Octosuite - User:Repos"
        CType(Me.DataGridViewUserRepos, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)

    End Sub

    Friend WithEvents DataGridViewUserRepos As DataGridView
End Class
