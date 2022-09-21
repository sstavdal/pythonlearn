import pyinputplus as pyip

response = pyip.inputNum("Please enter integer value : ")
print("You entered : " + str(response))


response = pyip.inputNum("Please enter integer value : ",min=3,max=2929)
print("You entered : " + str(response))

