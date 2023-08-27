<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class UserEventsForm
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
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(UserEventsForm))
        Me.DataGridViewUserEvents = New System.Windows.Forms.DataGridView()
        CType(Me.DataGridViewUserEvents, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'DataGridViewUserEvents
        '
        Me.DataGridViewUserEvents.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.AllCells
        Me.DataGridViewUserEvents.AutoSizeRowsMode = System.Windows.Forms.DataGridViewAutoSizeRowsMode.AllCellsExceptHeaders
        Me.DataGridViewUserEvents.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.DataGridViewUserEvents.Dock = System.Windows.Forms.DockStyle.Fill
        Me.DataGridViewUserEvents.Location = New System.Drawing.Point(0, 0)
        Me.DataGridViewUserEvents.Name = "DataGridViewUserEvents"
        Me.DataGridViewUserEvents.ReadOnly = True
        Me.DataGridViewUserEvents.RowTemplate.Height = 25
        Me.DataGridViewUserEvents.Size = New System.Drawing.Size(763, 450)
        Me.DataGridViewUserEvents.TabIndex = 4
        '
        'UserEventsForm
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(7.0!, 15.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(763, 450)
        Me.Controls.Add(Me.DataGridViewUserEvents)
        Me.Icon = CType(resources.GetObject("$this.Icon"), System.Drawing.Icon)
        Me.Name = "UserEventsForm"
        Me.Text = "Octosuite - User:Events"
        CType(Me.DataGridViewUserEvents, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)

    End Sub

    Friend WithEvents DataGridViewUserEvents As DataGridView
End Class
