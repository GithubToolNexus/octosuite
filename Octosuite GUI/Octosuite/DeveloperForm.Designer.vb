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
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(DeveloperForm))
        Me.GreetingLabel = New System.Windows.Forms.Label()
        Me.AboutMeLinkLabel = New System.Windows.Forms.LinkLabel()
        Me.BuyMeACoffeeLinkLabel = New System.Windows.Forms.LinkLabel()
        Me.SuspendLayout()
        '
        'GreetingLabel
        '
        Me.GreetingLabel.AutoSize = True
        Me.GreetingLabel.Font = New System.Drawing.Font("Verdana", 27.75!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point)
        Me.GreetingLabel.Location = New System.Drawing.Point(59, 34)
        Me.GreetingLabel.Name = "GreetingLabel"
        Me.GreetingLabel.Size = New System.Drawing.Size(382, 45)
        Me.GreetingLabel.TabIndex = 4
        Me.GreetingLabel.Text = "Hello, I'm Ritchie"
        '
        'AboutMeLinkLabel
        '
        Me.AboutMeLinkLabel.AutoSize = True
        Me.AboutMeLinkLabel.BackColor = System.Drawing.Color.White
        Me.AboutMeLinkLabel.Location = New System.Drawing.Point(59, 422)
        Me.AboutMeLinkLabel.Name = "AboutMeLinkLabel"
        Me.AboutMeLinkLabel.Size = New System.Drawing.Size(60, 15)
        Me.AboutMeLinkLabel.TabIndex = 5
        Me.AboutMeLinkLabel.TabStop = True
        Me.AboutMeLinkLabel.Text = "About.me"
        '
        'BuyMeACoffeeLinkLabel
        '
        Me.BuyMeACoffeeLinkLabel.AutoSize = True
        Me.BuyMeACoffeeLinkLabel.Location = New System.Drawing.Point(59, 446)
        Me.BuyMeACoffeeLinkLabel.Name = "BuyMeACoffeeLinkLabel"
        Me.BuyMeACoffeeLinkLabel.Size = New System.Drawing.Size(96, 15)
        Me.BuyMeACoffeeLinkLabel.TabIndex = 6
        Me.BuyMeACoffeeLinkLabel.TabStop = True
        Me.BuyMeACoffeeLinkLabel.Text = "Buy Me A Coffee"
        '
        'DeveloperForm
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(7.0!, 15.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.BackgroundImage = CType(resources.GetObject("$this.BackgroundImage"), System.Drawing.Image)
        Me.ClientSize = New System.Drawing.Size(514, 511)
        Me.Controls.Add(Me.BuyMeACoffeeLinkLabel)
        Me.Controls.Add(Me.AboutMeLinkLabel)
        Me.Controls.Add(Me.GreetingLabel)
        Me.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle
        Me.MaximizeBox = False
        Me.Name = "DeveloperForm"
        Me.ShowIcon = False
        Me.ShowInTaskbar = False
        Me.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
        Me.Text = "Developer"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents GreetingLabel As Label
    Friend WithEvents AboutMeLinkLabel As LinkLabel
    Friend WithEvents BuyMeACoffeeLinkLabel As LinkLabel
End Class
