import json
from json.encoder import py_encode_basestring
import requests
import pyinputplus as pyip
import os
import pprint

API_KEY = os.environ.get("API_KEY")
headers = {"Authorization": "Api-Key " + API_KEY}
baseurl = "https://www.peeringdb.com/api/"

def byasn(getasn):
    asnurl = (baseurl + "net/" + str(getasn))
    byasnjson = requests.get(asnurl,headers=headers)
    print(byasnjson.text)
    py_asn = json.loads(byasnjson.text)
    pprint.pprint(py_asn)
    print(type(py_asn))
    return py_asn

# Main
getasn = pyip.inputInt("Please enter ASN number you want to query : ")
byasn(getasn)

pprint.pprint(getasn)