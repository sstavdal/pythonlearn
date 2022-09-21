import pyinputplus as pyip


#>>> response = pyip.inputMenu(['cat', 'dog', 'moose'], numbered=True)
#Please select one of the following:
#1. cat
#2. dog
#3. moose
#1


animal = pyip.inputMenu(['cat','dog','mouse'],numbered=True)

print("You chose " + animal)