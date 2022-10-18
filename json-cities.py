import json
import requests
import pprint

cities_json = requests.get('https://countriesnow.space/api/v0.1/countries/population/cities')

# Convert to python dictionary
cities_py = json.loads(cities_json.text)

# Get indeces
# x = cities_py.keys()
# print(cities_py['data']['city'])

#print(cities_py)

# # print objects from index data
#print(cities_py[data][0]['city'])



# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

# print(people[1]['name'])


cities = cities_py.get('data')
print(cities)

# for key, value in cities:
#     print(key, value, sep=", ")

print("City : " + cities.get("data","city"))