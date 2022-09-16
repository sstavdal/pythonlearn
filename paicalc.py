import pyinputplus as pyip
from datetime import date


# Calculator for PAI (Personal Activity Intelligence) index
# By entering your year of birth, the calculator will give you the pulse required for 1 hour per week to stay healthy.

today= date.today()
curryear = today.year

byear = pyip.inputNum("Please enter the year of your birth [YYYY] : ")
age = curryear - byear
maxpulse = 211 - (age * 0.64)
pai = maxpulse * 0.8


print("You were born in the year " + str(byear))
print("This year : " + str(curryear) + " you are turning, or have turned " + str(age) + " years old")
print("Your max pulse is : " + str(maxpulse))
print("To avoid lifestyle deseases, you should exercise with a minimum pulse of " + str(pai) + " for a minimum of 1 hour per week")
