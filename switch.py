import pyinputplus as pyip
from pathlib import Path
import pyautogui as gui

def eur ():
    settings = {
        "dns1": "1.1.1.1",
        "dns2": "2.2.2.2",
        "ntp1": "1.2.3.4",
        "ntp2": "4.3.2.1"
    }
    return settings

def amer ():
    settings = {
        "dns1": "1.1.1.1",
        "dns2": "2.2.2.2",
        "ntp1": "1.2.3.4",
        "ntp2": "4.3.2.1"
    }
    return settings

def asia ():
    settings = {
        "dns1": "1.1.1.1",
        "dns2": "2.2.2.2",
        "ntp1": "1.2.3.4",
        "ntp2": "4.3.2.1"
    }
    return settings

# Definitions
home = str(Path.home())

# Script to configure switches of different types
cc = pyip.inputStr("Please enter [three] letter COUNTRY code : ")
ap = pyip.inputStr("Please enter [three] letter AIRPORT code : ")
fid = pyip.inputNum("Please enter FID value : ",min=1,max=9999)
switchnum = pyip.inputNum("Please enter switch number : ",min=1,max=100)

if switchnum < 9:
    switchnum = ("0"+str(switchnum))

# Setting hostname based on input
hostname = ("Hostname : " + cc + "-" + ap + str(fid)+"-sw"+str(switchnum))
print(hostname)

# Next, collect regional information
region = pyip.inputMenu(['eur','amer','asia'],numbered=True)

print("You chose " + region)

settings = region()
print(settings)