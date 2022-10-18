# Indexing using square brackets.
# Dictionaries and not using indeces.

vehicles = {
    'dream' : 'Honda 250T',
    'roadster' : 'BMW R1100',
    'er5' : 'Kawasaki ER5',
    'can-am' : 'Bombardier Can-Am 250',
    'virago' : 'Yamaha XV250',
    'tenere' : 'Yamaha XT650',
    'jimny' : 'Suzuki Jimny 1.5',
    'fiesta' : 'Ford Fiesta Ghia 1.4',
}


def showme():
    for key,value in vehicles.items():
        print(key, value, sep=", ")


# Key indexing (Throws and error if key does not exist), yet indexing is faster than the get method below.
my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)

# Pass key to get method (Returns None if key does not exist - less error handling)
learner = vehicles.get('er5')
print(learner)

# Adding and removing items to dictionary
vehicles['starfighter'] = 'Lockheed F-104'

# Adding to dictionary
vehicles['toy'] = 'Paper plane'
#showme()

# Changing the value (upgrade the virago)
vehicles["virago"] = "Yamaha VX535"
#showme()

# Removing items from a dictionary
del vehicles['starfighter']
#showme()

# Remove something that does not exist (causes crash) - del faster than pop, but pop does not crash if key does not exist
# del vehicles['f1']
# showme()

#
result = vehicles.pop('f1', "Object not there, could not delete")
print(result)
print()
#showme()

