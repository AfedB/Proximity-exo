from contextlib import closing
from urllib.request import urlopen
import json

with closing(urlopen('https://api.meteo-concept.com/api/location/cities?token=392504ecea5cec18daf14faf8c1e50957fd29a6e6090f840dbdb5d1a44bc0a75&search=Osny')) as f:
     cities = json.loads(f.read())['cities']
     print(u'Il y a {} villes correspondant à la recherche'.format(len(cities)))
     for city in cities:
         print(u'\t{} ({})'.format(city['name'], city['insee'][:2]))