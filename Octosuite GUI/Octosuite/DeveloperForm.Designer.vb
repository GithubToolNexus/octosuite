<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class DeveloperForm
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
        Dim resources As ComponentModel.ComponentResourceManager = New ComponentModel.ComponentResourceManager(GetType(DeveloperForm))
        GreetingLabel = New Label()
        AboutMeLinkLabel = New LinkLabel()
        BuyMeACoffeeLinkLabel = New LinkLabel()
        SuspendLayout()
        ' 
        ' GreetingLabel
        ' 
        GreetingLabel.AutoSize = True
        GreetingLabel.Font = New Font("Ink Free", 27.75F, FontStyle.Bold, GraphicsUnit.Point)
        GreetingLabel.Location = New Point(94, 35)
        GreetingLabel.Name = "GreetingLabel"
        GreetingLabel.Size = New Size(310, 46)
        GreetingLabel.TabIndex = 4
        GreetingLabel.Text = "Hello, I'm Ritchie"
        ' 
        ' AboutMeLinkLabel
        ' 
        AboutMeLinkLabel.AutoSize = True
        AboutMeLinkLabel.BackColor = Color.White
        AboutMeLinkLabel.Location = New Point(59, 422)
        AboutMeLinkLabel.Name = "AboutMeLinkLabel"
        AboutMeLinkLabel.Size = New Size(60, 15)
        AboutMeLinkLabel.TabIndex = 5
        AboutMeLinkLabel.TabStop = True
        AboutMeLinkLabel.Text = "About.me"
        ' 
        ' BuyMeACoffeeLinkLabel
        ' 
        BuyMeACoffeeLinkLabel.AutoSize = True
        BuyMeACoffeeLinkLabel.Location = New Point(59, 446)
        BuyMeACoffeeLinkLabel.Name = "BuyMeACoffeeLinkLabel"
        BuyMeACoffeeLinkLabel.Size = New Size(96, 15)
        BuyMeACoffeeLinkLabel.TabIndex = 6
        BuyMeACoffeeLinkLabel.TabStop = True
        BuyMeACoffeeLinkLabel.Text = "Buy Me A Coffee"
        ' 
        ' DeveloperForm
        ' 
        AutoScaleDimensions = New SizeF(7F, 15F)
        AutoScaleMode = AutoScaleMode.Font
        BackgroundImage = CType(resources.GetObject("$this.BackgroundImage"), Image)
        ClientSize = New Size(514, 511)
        Controls.Add(BuyMeACoffeeLinkLabel)
        Controls.Add(AboutMeLinkLabel)
        Controls.Add(GreetingLabel)
        FormBorderStyle = FormBorderStyle.FixedSingle
        MaximizeBox = False
        Name = "DeveloperForm"
        ShowIcon = False
        ShowInTaskbar = False
        StartPosition = FormStartPosition.CenterScreen
        Text = "Developer"
        ResumeLayout(False)
        PerformLayout()
    End Sub

    Friend WithEvents GreetingLabel As Label
    Friend WithEvents AboutMeLinkLabel As LinkLabel
    Friend WithEvents BuyMeACoffeeLinkLabel As LinkLabel
End Class
