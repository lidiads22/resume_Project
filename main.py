from urllib import request
import requests
from requests import Session 
from urllib.request import urlretrieve
from pprint import PrettyPrinter
import csv
import json 

pp = PrettyPrinter()
pp = PrettyPrinter()

api_key = '083RQn1KYzavgZC5uIoOIhNv0OYYwW9T29Bopzs7'

# path of the asteroids and their probability of impact with other near earth objects.

def fetchAsteroidFeed():
  URL_NeoFeed = "https://api.nasa.gov/neo/rest/v1/feed"
  params = {
      'api_key':api_key,
      'start_date':'2020-01-22',
      'end_date':'2020-01-23'
  }
  response = requests.get(URL_NeoFeed,params=params).json()
  pp.pprint(response)
fetchAsteroidFeed()





