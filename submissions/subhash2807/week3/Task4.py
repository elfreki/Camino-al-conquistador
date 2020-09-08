import requests
from bs4 import BeautifulSoup
import json

KEY="" # api key is needed to run this code

url = "https://developers.zomato.com/api/v2.1/cities"
api_key = {
        "user-key":KEY,
    }

search_url="https://developers.zomato.com/api/v2.1/search"


city=input("Enter the city name: ")

data = requests.get(url,headers=api_key,params={"q":city})

data = json.loads(data.text)['location_suggestions']
city_id=data[0]['id']

params = {
    "entity_id":city_id,
    "entity_type":"city",
    "count":5,
    "sort":"rating",
    "order":"desc"
}

restraunt_chunks = requests.get(search_url,headers=api_key,params=params)
restraunts = json.loads(restraunt_chunks.text)

i=1
for x in restraunts['restaurants']:
    dat = x['restaurant']
    if (float(dat['user_rating']['aggregate_rating'])>3.9):
        print(i)
        print("Name:",dat['name'])
        print("Aggregate Rating:",dat['user_rating']['aggregate_rating'])
        print("Address",dat['location']['address'])
        print()
        i+=1