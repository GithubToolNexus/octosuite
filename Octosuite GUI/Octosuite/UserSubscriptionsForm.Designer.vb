<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class UserSubscriptionsForm
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
        Dim resources As ComponentModel.ComponentResourceManager = New ComponentModel.ComponentResourceManager(GetType(UserSubscriptionsForm))
        DataGridViewUserSubscriptions = New DataGridView()
        CType(DataGridViewUserSubscriptions, ComponentModel.ISupportInitialize).BeginInit()
        SuspendLayout()
        ' 
        ' DataGridViewUserSubscriptions
        ' 
        DataGridViewUserSubscriptions.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize
        DataGridViewUserSubscriptions.Dock = DockStyle.Fill
        DataGridViewUserSubscriptions.Location = New Point(0, 0)
        DataGridViewUserSubscriptions.Name = "DataGridViewUserSubscriptions"
        DataGridViewUserSubscriptions.ReadOnly = True
        DataGridViewUserSubscriptions.RowHeadersVisible = False
        DataGridViewUserSubscriptions.RowTemplate.Height = 25
        DataGridViewUserSubscriptions.Size = New Size(755, 450)
        DataGridViewUserSubscriptions.TabIndex = 1
        ' 
        ' UserSubscriptionsForm
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(755, 450)
        Controls.Add(DataGridViewUserSubscriptions)
        Icon = CType(resources.GetObject("$this.Icon"), Icon)
        Name = "UserSubscriptionsForm"
        ShowIcon = False
        StartPosition = FormStartPosition.CenterScreen
        Text = "UserSubsriptionsForm"
        CType(DataGridViewUserSubscriptions, ComponentModel.ISupportInitialize).EndInit()
        ResumeLayout(False)
    End Sub

    Friend WithEvents DataGridViewUserSubscriptions As DataGridView
End Class
