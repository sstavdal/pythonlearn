import requests

# Creating a payload rather than having a really long url that looks messy
payload = {'username':'john','password':'doe'}

# Get the URI with the actual payload
r = requests.post('https://httpbin.org/post',data=payload)

# Load the results from json into a python dictionary
r_dict = r.json()

print(type(r_dict)) # confirm python dict type

# Access the object form from the dictionary
print(r_dict['form'])


# Testing http error codes if timeout > delay or timeout < delay should produce different http error codes
r = requests.get('https://httpbin.org/delay/6',timeout=7)

print(r)