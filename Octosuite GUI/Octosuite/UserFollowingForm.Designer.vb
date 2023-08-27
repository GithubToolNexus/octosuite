<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class UserFollowingForm
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
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(UserFollowingForm))
        Me.DataGridViewUserFollowing = New System.Windows.Forms.DataGridView()
        CType(Me.DataGridViewUserFollowing, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'DataGridViewUserFollowing
        '
        Me.DataGridViewUserFollowing.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.DataGridViewUserFollowing.Dock = System.Windows.Forms.DockStyle.Fill
        Me.DataGridViewUserFollowing.Location = New System.Drawing.Point(0, 0)
        Me.DataGridViewUserFollowing.Name = "DataGridViewUserFollowing"
        Me.DataGridViewUserFollowing.ReadOnly = True
        Me.DataGridViewUserFollowing.RowTemplate.Height = 25
        Me.DataGridViewUserFollowing.Size = New System.Drawing.Size(800, 450)
        Me.DataGridViewUserFollowing.TabIndex = 3
        '
        'UserFollowingForm
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(7.0!, 15.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(800, 450)
        Me.Controls.Add(Me.DataGridViewUserFollowing)
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.Name = "UserFollowingForm"
        Me.Text = "Octosuite - User:Following"
        CType(Me.DataGridViewUserFollowing, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)

    End Sub

    Friend WithEvents DataGridViewUserFollowing As DataGridView
End Class
