Imports System.IO
Imports System.Net
Imports System.Net.Http
Imports Newtonsoft.Json
Imports Newtonsoft.Json.Linq

''' <summary>
''' Handles communication with the API.
''' </summary>
Public Class ApiHandler
    Private Const Headers As String = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
    Private ReadOnly Logfile As String = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "Octosuite GUI", "logs", $"debug.log")

    Private Async Function FetchDataFromApi(endpoint As String) As Task(Of JArray)
        Try
            Using httpClient As New HttpClient()
                httpClient.DefaultRequestHeaders.Add("User-Agent", Headers)
                Dim response As HttpResponseMessage = Await httpClient.GetAsync(endpoint)

                If response.IsSuccessStatusCode Then
                    Dim json As String = Await response.Content.ReadAsStringAsync()
                    Return JsonConvert.DeserializeObject(Of JArray)(json)
                Else
                    MessageBox.Show(response.ReasonPhrase, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
                End If
            End Using
        Catch ex As Exception
            WriteToLog(ex)
        End Try

        Return New JArray()
    End Function

    Private Async Function FetchObjectFromApi(endpoint As String) As Task(Of JObject)
        Try
            Using httpClient As New HttpClient()
                httpClient.DefaultRequestHeaders.Add("User-Agent", Headers)
                Dim response As HttpResponseMessage = Await httpClient.GetAsync(endpoint)

                If response.IsSuccessStatusCode Then
                    Dim json As String = Await response.Content.ReadAsStringAsync()
                    Return JsonConvert.DeserializeObject(Of JObject)(json)
                Else
                    MessageBox.Show(response.ReasonPhrase, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
                End If
            End Using
        Catch ex As Exception
            WriteToLog(ex)
        End Try

        Return New JObject()
    End Function

    Public Async Function UserFollows(user_a As String, user_b As String) As Task(Of Boolean)
        Try
            Dim ApiEndpoint As String = $"https://api.github.com/users/{user_a}/following/{user_b}"
            Using httpClient As New HttpClient()
                httpClient.DefaultRequestHeaders.Add("User-Agent", Headers)
                Dim response As HttpResponseMessage = Await httpClient.GetAsync(ApiEndpoint)
                If response.StatusCode = HttpStatusCode.NoContent Then
                    Return True
                Else
                    Return False
                End If
            End Using
        Catch ex As Exception
            WriteToLog(ex)
            Return False
        End Try
    End Function

    Public Function CheckUpdates() As Task(Of JObject)
        Dim apiEndpoint As String = "https://api.github.com/repos/bellingcat/octosuite/releases/latest"
        Return FetchObjectFromApi(apiEndpoint)
    End Function


    Public Function UserRepos(username As String) As Task(Of JArray)
        Dim apiEndpoint As String = $"https://api.github.com/users/{username}/repos?per_page=100"
        Return FetchDataFromApi(apiEndpoint)
    End Function

    Public Function UserSubscriptions(username As String) As Task(Of JArray)
        Dim apiEndpoint As String = $"https://api.github.com/users/{username}/subscriptions?per_page=100"
        Return FetchDataFromApi(apiEndpoint)
    End Function

    Public Function UserGists(username As String) As Task(Of JArray)
        Dim apiEndpoint As String = $"https://api.github.com/users/{username}/gists?per_page=100"
        Return FetchDataFromApi(apiEndpoint)
    End Function

    Public Function UserFollowers(username As String) As Task(Of JArray)
        Dim apiEndpoint As String = $"https://api.github.com/users/{username}/followers?per_page=100"
        Return FetchDataFromApi(apiEndpoint)
    End Function

    Public Function UserFollowing(username As String) As Task(Of JArray)
        Dim apiEndpoint As String = $"https://api.github.com/users/{username}/following?per_page=100"
        Return FetchDataFromApi(apiEndpoint)
    End Function

    Public Function UserOrgs(username As String) As Task(Of JArray)
        Dim apiEndpoint As String = $"https://api.github.com/users/{username}/orgs?per_page=100"
        Return FetchDataFromApi(apiEndpoint)
    End Function

    Public Function UserEvents(username As String) As Task(Of JArray)
        Dim apiEndpoint As String = $"https://api.github.com/users/{username}/events/public?per_page=100"
        Return FetchDataFromApi(apiEndpoint)
    End Function

    Public Function OrgProfile(username As String) As Task(Of JObject)
        Dim apiEndpoint As String = $"https://api.github.com/orgs/{username}"
        Return FetchObjectFromApi(apiEndpoint)
    End Function

    Public Function UserProfile(username As String) As Task(Of JObject)
        Dim apiEndpoint As String = $"https://api.github.com/users/{username}"
        Return FetchObjectFromApi(apiEndpoint)
    End Function

    Public Function OrgRepos(organisation As String) As Task(Of JArray)
        Dim apiEndpoint As String = $"https://api.github.com/orgs/{organisation}/repos?per_page=100"
        Return FetchDataFromApi(apiEndpoint)
    End Function

    ''' <summary>
    ''' Writes an exception to the log file and shows a message box.
    ''' </summary>
    ''' <param name="ex">The exception to log and show.</param>
    Private Sub WriteToLog(ex As Exception)
        My.Computer.FileSystem.WriteAllText(Logfile, $"{DateTime.Now}: {ex}{Environment.NewLine}", True)
        MessageBox.Show($"{ex.Message}. Please see the debug log '{Logfile}' for more information.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
    End Sub
End Class
