"""
Use the countries API https://restcountries.eu/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

"""
import requests

url = 'https://restcountries.eu/rest/v2/name/'
url_home = url + 'Russia'
url_stay = url + 'gb'
body_home = requests.get(url_home).json()
body_stay = requests.get(url_stay).json()
body_home = body_home[0]
body_stay = body_stay[0]
print(f"{body_stay['capital']} is the capital of {body_stay['name']}")
print(f"{body_home['capital']} is the capital of {body_home['name']}")

if body_stay['population'] > body_home ['population']:
    print(f"The population of {body_stay['name']} is larger than that of {body_home['name']}")
elif body_stay['population'] < body_home ['population']:
    print(f"The population of {body_stay['name']} is smaller than that of{body_home['name']}")
else:
    print(f"The population of {body_stay['name']} and {body_home['name']} are the same")

print(f"The difference in their areas is {body_home['area'] - body_stay['area']} km")