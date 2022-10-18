import re

#target_string = "The price of PINEAPPLE ice cream is 20"
target_string = "The price of APPLE ice cream is 10"


# Goal, create two groups, one containing the ice cream flavour, and the other, the price
# We'll look for uppercase letters inside a word boundry, as well as a number at the end of the string

result = re.search(r"(\b[A-Z]+\b).+(\b\d+)", target_string)

# Extract matching values of all Groups
print(result.groups())

#Group 1
print(result.group(1))

# Group 2
print(result.group(2))

#Make a new result that creates group names

result2 = re.search(r"(?P<FLAVOUR>\b[A-Z]+\b).+(?P<PRICE>\b\d+)", target_string)

print(result2)