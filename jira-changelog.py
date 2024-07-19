#skrypt wyszukujący w historii zgłoszeń ('changelog') w Jira datę dla podanej zmiany statusu ('created/ status')

import requests
import pandas
from requests.auth import HTTPBasicAuth


#plik Excel z listą issues do sprawdzeni
file_path='python/jira_changes/issues.xlsx'

df = pandas.read_excel(file_path)
issues_keys = df["issue_key"]
responses = df["response"]

#jira info
jira_domain = "https://jiradomain.atlassian.net/"
desired_status = "Review"
api_token = "YOUR_API_TOKEN"
auth = HTTPBasicAuth('YOUR@EMAIL.com', api_token)


def read_single_issue(issue_key):
    response = requests.get(f"{jira_domain}/rest/api/3/issue/{issue_key}?expand=changelog", auth=auth)

    issue_data = response.json()
    status_change_date = None

    for history in issue_data['changelog']['histories']:
        for item in history['items']:
            if item['field'] == "status" and item['toString'] == desired_status:
                status_change_date = history['created']
                break

        if status_change_date:
            break
    if status_change_date:
        return(f"{status_change_date}")
    else:
        return("Zmiana statusu nie odnaleziona")

#loop
liczba_wierszy = issues_keys.count()
licznik = 0 

for licznik in range(liczba_wierszy):
    print(issues_keys[licznik])
    responses[licznik]=read_single_issue(issues_keys[licznik])

#save dataframe to excel
df.to_excel("python/jira_changes/issues.xlsx") 