#najprostrze zapytanie API - losowy fakt o kotach :)

import requests
import json

adres_api = "https://catfact.ninja/fact"

odpowiedz = requests.get(adres_api)
dane = json.loads(odpowiedz._content)

print(f"Random fact about cats: {dane['fact']}")