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
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(UserSubscriptionsForm))
        Me.DataGridViewUserSubscriptions = New System.Windows.Forms.DataGridView()
        CType(Me.DataGridViewUserSubscriptions, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'DataGridViewUserSubscriptions
        '
        Me.DataGridViewUserSubscriptions.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.DataGridViewUserSubscriptions.Dock = System.Windows.Forms.DockStyle.Fill
        Me.DataGridViewUserSubscriptions.Location = New System.Drawing.Point(0, 0)
        Me.DataGridViewUserSubscriptions.Name = "DataGridViewUserSubscriptions"
        Me.DataGridViewUserSubscriptions.ReadOnly = True
        Me.DataGridViewUserSubscriptions.RowTemplate.Height = 25
        Me.DataGridViewUserSubscriptions.Size = New System.Drawing.Size(1072, 490)
        Me.DataGridViewUserSubscriptions.TabIndex = 1
        '
        'UserSubscriptionsForm
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(7.0!, 15.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(1072, 490)
        Me.Controls.Add(Me.DataGridViewUserSubscriptions)
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.Name = "UserSubscriptionsForm"
        Me.Text = "Octosuite - User:Subscriptions"
        CType(Me.DataGridViewUserSubscriptions, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)

    End Sub

    Friend WithEvents DataGridViewUserSubscriptions As DataGridView
End Class
