import requests
import json

query = input('Enter the IP address that you would like to locate: ')

url = f'https://get.geojs.io/v1/ip/geo/{query}.json'
r = requests.get(url)

result = r.json()

#print(result)

organization = result ['organization']
longitude = result['longitude']
latitude = result['latitude']
country = result['country']

print(f'Organization: {organization} \nLongitude: {longitude} \nLatitude: {latitude} \nCountry: {country}')