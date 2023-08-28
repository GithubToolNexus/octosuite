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
        Dim resources As ComponentModel.ComponentResourceManager = New ComponentModel.ComponentResourceManager(GetType(UserEventsForm))
        DataGridViewUserEvents = New DataGridView()
        CType(DataGridViewUserEvents, ComponentModel.ISupportInitialize).BeginInit()
        SuspendLayout()
        ' 
        ' DataGridViewUserEvents
        ' 
        DataGridViewUserEvents.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells
        DataGridViewUserEvents.AutoSizeRowsMode = DataGridViewAutoSizeRowsMode.AllCellsExceptHeaders
        DataGridViewUserEvents.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize
        DataGridViewUserEvents.Dock = DockStyle.Fill
        DataGridViewUserEvents.Location = New Point(0, 0)
        DataGridViewUserEvents.Name = "DataGridViewUserEvents"
        DataGridViewUserEvents.ReadOnly = True
        DataGridViewUserEvents.RowHeadersVisible = False
        DataGridViewUserEvents.RowTemplate.Height = 25
        DataGridViewUserEvents.Size = New Size(694, 450)
        DataGridViewUserEvents.TabIndex = 4
        ' 
        ' UserEventsForm
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(694, 450)
        Controls.Add(DataGridViewUserEvents)
        FormBorderStyle = FormBorderStyle.FixedSingle
        Icon = CType(resources.GetObject("$this.Icon"), Icon)
        Name = "UserEventsForm"
        ShowIcon = False
        StartPosition = FormStartPosition.CenterScreen
        Text = "UserEventsForm"
        CType(DataGridViewUserEvents, ComponentModel.ISupportInitialize).EndInit()
        ResumeLayout(False)
    End Sub

    Friend WithEvents DataGridViewUserEvents As DataGridView
End Class
