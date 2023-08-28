<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class UserOrgsForm
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
        Dim resources As ComponentModel.ComponentResourceManager = New ComponentModel.ComponentResourceManager(GetType(UserOrgsForm))
        DataGridViewUserOrgs = New DataGridView()
        CType(DataGridViewUserOrgs, ComponentModel.ISupportInitialize).BeginInit()
        SuspendLayout()
        ' 
        ' DataGridViewUserOrgs
        ' 
        DataGridViewUserOrgs.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize
        DataGridViewUserOrgs.Dock = DockStyle.Fill
        DataGridViewUserOrgs.Location = New Point(0, 0)
        DataGridViewUserOrgs.Name = "DataGridViewUserOrgs"
        DataGridViewUserOrgs.ReadOnly = True
        DataGridViewUserOrgs.RowHeadersVisible = False
        DataGridViewUserOrgs.RowTemplate.Height = 25
        DataGridViewUserOrgs.Size = New Size(714, 450)
        DataGridViewUserOrgs.TabIndex = 4
        ' 
        ' UserOrgsForm
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(714, 450)
        Controls.Add(DataGridViewUserOrgs)
        Icon = CType(resources.GetObject("$this.Icon"), Icon)
        Name = "UserOrgsForm"
        ShowIcon = False
        StartPosition = FormStartPosition.CenterScreen
        Text = "UserOrgsForm"
        CType(DataGridViewUserOrgs, ComponentModel.ISupportInitialize).EndInit()
        ResumeLayout(False)
    End Sub

    Friend WithEvents DataGridViewUserOrgs As DataGridView
End Class
