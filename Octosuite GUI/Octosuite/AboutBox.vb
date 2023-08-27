Public NotInheritable Class AboutBox
    Public ReadOnly LicenseText As String = $"{My.Application.Info.Copyright}

{My.Application.Info.ProductName} is free software: 
you can redistribute it and/or modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

{My.Application.Info.ProductName} is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with {My.Application.Info.ProductName}. If not, see <http://www.gnu.org/licenses/>."

    Private Sub AboutBox_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        ' Initialize all of the text displayed on the About Box.
        ' TODO: Customize the application's assembly information in the "Application" pane of the project 
        '    properties dialog (under the "Project" menu).
        Me.LabelProductName.Text = My.Application.Info.ProductName
        Me.LabelProgramDescription.Text = "An all-in-one framework
for gathering  Open-Source Intelligence (OSINT)
on GitHub Users, Repositories and Organisations."
        Me.LabelVersion.Text = $"v{My.Application.Info.Version.ToString}"
        Me.RichTextBoxLicenseNotice.Text = LicenseText
    End Sub

    Private Sub LinkLabelReadtheWiki_LinkClicked(sender As Object, e As LinkLabelLinkClickedEventArgs) Handles LinkLabelReadtheWiki.LinkClicked
        Shell("cmd /c start https://github.com/bellingcat/octosuite/wiki")
    End Sub
End Class
