import json
import requests

cities_json = requests.get('https://countriesnow.space/api/v0.1/countries/population/cities')

cities_py = json.loads(cities_json)

print(cities_py)