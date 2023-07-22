<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class UserProfileForm
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
        Dim DataGridViewCellStyle1 As System.Windows.Forms.DataGridViewCellStyle = New System.Windows.Forms.DataGridViewCellStyle()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(UserProfileForm))
        Me.DataGridUserProfile = New System.Windows.Forms.DataGridView()
        CType(Me.DataGridUserProfile, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'DataGridUserProfile
        '
        Me.DataGridUserProfile.AllowUserToAddRows = False
        Me.DataGridUserProfile.AllowUserToDeleteRows = False
        DataGridViewCellStyle1.BackColor = System.Drawing.Color.White
        Me.DataGridUserProfile.AlternatingRowsDefaultCellStyle = DataGridViewCellStyle1
        Me.DataGridUserProfile.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill
        Me.DataGridUserProfile.BackgroundColor = System.Drawing.Color.White
        Me.DataGridUserProfile.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.DataGridUserProfile.ColumnHeadersVisible = False
        Me.DataGridUserProfile.Dock = System.Windows.Forms.DockStyle.Fill
        Me.DataGridUserProfile.EnableHeadersVisualStyles = False
        Me.DataGridUserProfile.Location = New System.Drawing.Point(0, 0)
        Me.DataGridUserProfile.Name = "DataGridUserProfile"
        Me.DataGridUserProfile.ReadOnly = True
        Me.DataGridUserProfile.RowHeadersVisible = False
        Me.DataGridUserProfile.RowTemplate.Height = 25
        Me.DataGridUserProfile.Size = New System.Drawing.Size(800, 428)
        Me.DataGridUserProfile.TabIndex = 1
        '
        'UserProfileForm
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(7.0!, 15.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(800, 428)
        Me.Controls.Add(Me.DataGridUserProfile)
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.MaximizeBox = False
        Me.Name = "UserProfileForm"
        Me.Text = "Octosuite - User:Profile"
        CType(Me.DataGridUserProfile, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)

    End Sub

    Friend WithEvents DataGridUserProfile As DataGridView
End Class
