import json
import requests

cities_json = requests.get('https://countriesnow.space/api/v0.1/countries/population/cities')

#print(cities_json.text)
print(type(cities_json.text))

cities_py = json.loads(cities_json.text)

#print(type(cities_py))

#print(cities_py.city)

x = cities_py.keys()

print(x)