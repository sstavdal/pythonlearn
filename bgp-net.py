import json
from json.encoder import py_encode_basestring
import requests
import pyinputplus as pyip
import os
import pprint

newHeaders = {'Content-type': 'application/json'} # Specifically request json data in the header
baseurl = "https://bgpstuff.net/sourced/"

def byasn(getasn):
    asnurl = (baseurl + str(getasn))
    print(asnurl)


    byasnjson = requests.get(asnurl,headers=newHeaders)
    print(byasnjson.text)
    py_asn = json.loads(byasnjson.text)
    pprint.pprint(py_asn)
    print(type(py_asn))
    return py_asn

# Main
getasn = pyip.inputInt("Please enter ASN number you want to query : ")
byasn(getasn)

pprint.pprint(getasn)
print()