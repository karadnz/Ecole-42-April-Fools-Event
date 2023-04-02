import urllib.request
import json
import ssl
from urllib.error import HTTPError

ssl._create_default_https_context = ssl._create_unverified_context

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

name = input("Enter the name of a Pokemon: ")

url = "https://pokeapi.co/api/v2/pokemon/" + name.lower()

req = urllib.request.Request(url, headers=headers)

try:
    response = urllib.request.urlopen(req)
except:
    print("A problem occured. Probably about naming.")
    quit()

data = json.loads(response.read())

abilities = [ability['ability']['name'] for ability in data['abilities']]

print(f"Name: {data['name'].capitalize()}")
print("Abilities:")
for ability in abilities:
    print(f"- {ability.capitalize()}")
