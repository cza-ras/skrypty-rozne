#test API Eurostat

import requests
import json

api_url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/DEMO_R_D3DENS?lang=EN"

odpowiedz = requests.get(api_url)
dane = json.loads(odpowiedz._content)


print(dane)