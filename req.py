import requests

r = requests.get('https://imgs.xkcd.com/comics/python.png')

# Test if page loads ok

print(r.ok)

# Print headers

print(r.headers)
  

# Get help on requests

print(help(r)) 

# Print objects that can be used

print(dir(r))

# Write to file

with open('comic.png','wb') as f:
    f.write(r.content)
    f.close

# Print HTTP return code
print(r.status_code)