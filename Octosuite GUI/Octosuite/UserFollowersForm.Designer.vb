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
        Dim resources As ComponentModel.ComponentResourceManager = New ComponentModel.ComponentResourceManager(GetType(UserFollowersForm))
        DataGridViewUserFollowers = New DataGridView()
        CType(DataGridViewUserFollowers, ComponentModel.ISupportInitialize).BeginInit()
        SuspendLayout()
        ' 
        ' DataGridViewUserFollowers
        ' 
        DataGridViewUserFollowers.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize
        DataGridViewUserFollowers.Dock = DockStyle.Fill
        DataGridViewUserFollowers.Location = New Point(0, 0)
        DataGridViewUserFollowers.Name = "DataGridViewUserFollowers"
        DataGridViewUserFollowers.ReadOnly = True
        DataGridViewUserFollowers.RowHeadersVisible = False
        DataGridViewUserFollowers.RowTemplate.Height = 25
        DataGridViewUserFollowers.Size = New Size(696, 450)
        DataGridViewUserFollowers.TabIndex = 2
        ' 
        ' UserFollowersForm
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(696, 450)
        Controls.Add(DataGridViewUserFollowers)
        FormBorderStyle = FormBorderStyle.FixedSingle
        Icon = CType(resources.GetObject("$this.Icon"), Icon)
        Name = "UserFollowersForm"
        ShowIcon = False
        StartPosition = FormStartPosition.CenterScreen
        Text = "UserFollowersForm"
        CType(DataGridViewUserFollowers, ComponentModel.ISupportInitialize).EndInit()
        ResumeLayout(False)
    End Sub

    Friend WithEvents DataGridViewUserFollowers As DataGridView
End Class
