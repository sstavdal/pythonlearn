import json

# Takes json input, 

# define a list to work with

people_string = '''
{
    "people": [
        {
            "name" : "John Smith",
            "phone" : "555-6677",
            "email" : "john.smith@home.com",
            "is_cool" : false
        },
        {
            "name" : "Jane Doe",
            "phone" : "555-8899",
            "email" : "jane.doe@get.com",
            "is_cool" : true
        }
    ]
}
'''

# Next, play with contents, first convert into python dictionary
data = json.loads(people_string)
print(data)

# Print objects from dict
for person in data['people']:
    print(person['name'],person['email'])


# Make changes to dictionary
# Delete email
for person in data['people']:
    del(person['email'])
print(data)


# Dump back into json from python dict
new_string = json.dumps(data, indent=2)
print(new_string)