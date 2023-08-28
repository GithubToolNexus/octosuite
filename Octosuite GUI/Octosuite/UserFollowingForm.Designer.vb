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
        Dim resources As ComponentModel.ComponentResourceManager = New ComponentModel.ComponentResourceManager(GetType(UserFollowingForm))
        DataGridViewUserFollowing = New DataGridView()
        CType(DataGridViewUserFollowing, ComponentModel.ISupportInitialize).BeginInit()
        SuspendLayout()
        ' 
        ' DataGridViewUserFollowing
        ' 
        DataGridViewUserFollowing.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize
        DataGridViewUserFollowing.Dock = DockStyle.Fill
        DataGridViewUserFollowing.Location = New Point(0, 0)
        DataGridViewUserFollowing.Name = "DataGridViewUserFollowing"
        DataGridViewUserFollowing.ReadOnly = True
        DataGridViewUserFollowing.RowHeadersVisible = False
        DataGridViewUserFollowing.RowTemplate.Height = 25
        DataGridViewUserFollowing.Size = New Size(696, 450)
        DataGridViewUserFollowing.TabIndex = 3
        ' 
        ' UserFollowingForm
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(696, 450)
        Controls.Add(DataGridViewUserFollowing)
        FormBorderStyle = FormBorderStyle.FixedSingle
        Icon = CType(resources.GetObject("$this.Icon"), Icon)
        Name = "UserFollowingForm"
        ShowIcon = False
        StartPosition = FormStartPosition.CenterScreen
        Text = "UserFollowingForm"
        CType(DataGridViewUserFollowing, ComponentModel.ISupportInitialize).EndInit()
        ResumeLayout(False)
    End Sub

    Friend WithEvents DataGridViewUserFollowing As DataGridView
End Class
