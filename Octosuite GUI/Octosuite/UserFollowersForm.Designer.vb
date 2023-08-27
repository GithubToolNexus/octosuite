<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class UserFollowersForm
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
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(UserFollowersForm))
        Me.DataGridViewUserFollowers = New System.Windows.Forms.DataGridView()
        CType(Me.DataGridViewUserFollowers, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'DataGridViewUserFollowers
        '
        Me.DataGridViewUserFollowers.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.DataGridViewUserFollowers.Dock = System.Windows.Forms.DockStyle.Fill
        Me.DataGridViewUserFollowers.Location = New System.Drawing.Point(0, 0)
        Me.DataGridViewUserFollowers.Name = "DataGridViewUserFollowers"
        Me.DataGridViewUserFollowers.ReadOnly = True
        Me.DataGridViewUserFollowers.RowTemplate.Height = 25
        Me.DataGridViewUserFollowers.Size = New System.Drawing.Size(850, 450)
        Me.DataGridViewUserFollowers.TabIndex = 2
        '
        'UserFollowersForm
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(7.0!, 15.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(850, 450)
        Me.Controls.Add(Me.DataGridViewUserFollowers)
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.Name = "UserFollowersForm"
        Me.Text = "Octosuite - User:Followers"
        CType(Me.DataGridViewUserFollowers, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)

    End Sub

    Friend WithEvents DataGridViewUserFollowers As DataGridView
End Class
