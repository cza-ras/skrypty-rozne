#Facebook API => pobieranie liczby osób obserwujących stronę

import requests

PAGE_ID = 'PlatformaObywatelska' 
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

#request
url = f"https://graph.facebook.com/v11.0/{PAGE_ID}?fields=followers_count&access_token={ACCESS_TOKEN}"
response = requests.get(url)
data = response.json()

#wyodrębiebie liczby obserwatorów z JSON
followers_count = data.get('followers_count', None)

if followers_count is not None:
    print(f"Stronę obserwuje {followers_count} osób.")
else:
    print("Nie udało się odczytać liczby obserwatorów")
