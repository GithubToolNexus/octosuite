<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class AboutBox
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
        Dim resources As ComponentModel.ComponentResourceManager = New ComponentModel.ComponentResourceManager(GetType(AboutBox))
        PictureBox1 = New PictureBox()
        RichTextBoxLicenseNotice = New RichTextBox()
        LabelProductName = New Label()
        LabelProgramDescription = New Label()
        LinkLabelReadtheWiki = New LinkLabel()
        LabelVersion = New Label()
        CType(PictureBox1, ComponentModel.ISupportInitialize).BeginInit()
        SuspendLayout()
        ' 
        ' PictureBox1
        ' 
        PictureBox1.Image = CType(resources.GetObject("PictureBox1.Image"), Image)
        PictureBox1.Location = New Point(13, 13)
        PictureBox1.Name = "PictureBox1"
        PictureBox1.Size = New Size(98, 105)
        PictureBox1.SizeMode = PictureBoxSizeMode.StretchImage
        PictureBox1.TabIndex = 0
        PictureBox1.TabStop = False
        ' 
        ' RichTextBoxLicenseNotice
        ' 
        RichTextBoxLicenseNotice.Font = New Font("Cambria", 9.75F, FontStyle.Regular, GraphicsUnit.Point)
        RichTextBoxLicenseNotice.Location = New Point(13, 124)
        RichTextBoxLicenseNotice.Name = "RichTextBoxLicenseNotice"
        RichTextBoxLicenseNotice.ReadOnly = True
        RichTextBoxLicenseNotice.Size = New Size(461, 239)
        RichTextBoxLicenseNotice.TabIndex = 1
        RichTextBoxLicenseNotice.Text = "License Notice"
        ' 
        ' LabelProductName
        ' 
        LabelProductName.AutoSize = True
        LabelProductName.Font = New Font("Segoe UI Semibold", 14.25F, FontStyle.Bold, GraphicsUnit.Point)
        LabelProductName.Location = New Point(117, 21)
        LabelProductName.Name = "LabelProductName"
        LabelProductName.Size = New Size(138, 25)
        LabelProductName.TabIndex = 2
        LabelProductName.Text = "ProgramName"
        ' 
        ' LabelProgramDescription
        ' 
        LabelProgramDescription.AutoSize = True
        LabelProgramDescription.Location = New Point(117, 65)
        LabelProgramDescription.Name = "LabelProgramDescription"
        LabelProgramDescription.Size = New Size(67, 15)
        LabelProgramDescription.TabIndex = 3
        LabelProgramDescription.Text = "Description"
        ' 
        ' LinkLabelReadtheWiki
        ' 
        LinkLabelReadtheWiki.AutoSize = True
        LinkLabelReadtheWiki.Location = New Point(395, 65)
        LinkLabelReadtheWiki.Name = "LinkLabelReadtheWiki"
        LinkLabelReadtheWiki.Size = New Size(79, 15)
        LinkLabelReadtheWiki.TabIndex = 4
        LinkLabelReadtheWiki.TabStop = True
        LinkLabelReadtheWiki.Text = "Read the Wiki"
        ' 
        ' LabelVersion
        ' 
        LabelVersion.AutoSize = True
        LabelVersion.Font = New Font("Segoe UI", 9F, FontStyle.Underline, GraphicsUnit.Point)
        LabelVersion.Location = New Point(429, 31)
        LabelVersion.Name = "LabelVersion"
        LabelVersion.Size = New Size(45, 15)
        LabelVersion.TabIndex = 5
        LabelVersion.Text = "Version"
        ' 
        ' AboutBox
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        BackColor = Color.Gainsboro
        ClientSize = New Size(487, 375)
        Controls.Add(LabelVersion)
        Controls.Add(LinkLabelReadtheWiki)
        Controls.Add(LabelProgramDescription)
        Controls.Add(LabelProductName)
        Controls.Add(RichTextBoxLicenseNotice)
        Controls.Add(PictureBox1)
        FormBorderStyle = FormBorderStyle.FixedDialog
        Margin = New Padding(4, 3, 4, 3)
        MaximizeBox = False
        MinimizeBox = False
        Name = "AboutBox"
        Padding = New Padding(10)
        ShowInTaskbar = False
        StartPosition = FormStartPosition.CenterParent
        Text = "About"
        CType(PictureBox1, ComponentModel.ISupportInitialize).EndInit()
        ResumeLayout(False)
        PerformLayout()
    End Sub

    Friend WithEvents PictureBox1 As PictureBox
    Friend WithEvents RichTextBoxLicenseNotice As RichTextBox
    Friend WithEvents LabelProductName As Label
    Friend WithEvents LabelProgramDescription As Label
    Friend WithEvents LinkLabelReadtheWiki As LinkLabel
    Friend WithEvents LabelVersion As Label
End Class
