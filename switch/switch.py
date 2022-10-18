import pyinputplus as pyip
from pathlib import Path
import pyautogui as gui


settings = {
    "asia": {"dns1": "3.3.3.1","dns2": "3.3.3.2","ntp1": "3.3.3.3","ntp2": "3.3.3.4"},
    "amer": {"dns1": "2.2.2.1","dns2": "2.2.2.2","ntp1": "2.2.2.3","ntp2": "2.2.2.4"},
    "eur": {"dns1": "1.1.1.1","dns2": "1.1.1.2","ntp1": "1.1.1.3","ntp2": "1.1.1.4"} 
}

def getRegionSettings(region) : 
    return settings[region]

# Definitions
home = str(Path.home())

# Script to configure switches of different types
cc = pyip.inputStr("Please enter [three] letter COUNTRY code : ")
ap = pyip.inputStr("Please enter [three] letter CITY code : ")
sid = pyip.inputNum("Please enter Site ID value : ",min=1,max=9999)
switchnum = pyip.inputNum("Please enter switch number : ",min=1,max=100)

if switchnum < 10:
    switchnum = ("0"+str(switchnum))

# Setting hostname based on input
hostname = (cc + "-" + ap + str(sid)+"-sw"+str(switchnum))

# Next, collect regional information
region = pyip.inputMenu(['eur','amer','asia'],numbered=True)

# print("You chose " + region)
settings = getRegionSettings(region)

# print("Hostname " + hostname)
# print("DNS1 : " + settings.get("dns1"))
# print("DNS2 : " + settings.get("dns2"))
# print("NTP1 : " + settings.get("ntp1"))
# print("NTP2 : " + settings.get("ntp2"))

# Next, collect regional information
type = pyip.inputMenu(['hp','aruba','cisco'],numbered=True)
print(type)

# Set the name of the template based on chosen type as f
path = r"template.{}"

# open template file and replace the text into the data variable
with open(path.format(type), 'r') as template:
    data = template.read()
    data = data.replace("_dns1_", settings.get("dns1"))
    data = data.replace("_dns2_", settings.get("dns2"))
    data = data.replace("_ntp1_", settings.get("ntp1"))
    data = data.replace("_ntp2_", settings.get("ntp2"))
    data = data.replace("_hostname_", hostname)
    template.close()
  
# Writing config file as hostname.txt
with open('{0}.txt'.format(hostname),"w") as config:
    config.write(data)
    config.close()