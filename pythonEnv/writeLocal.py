import json
from requests import *
from functions import getJSON, getImageURL
urls = ['https://www.loc.gov/item/2016849381/',
        'https://www.loc.gov/item/2016825835/', 'https://www.loc.gov/item/2010648518/']
example = []
i = 0
for url in urls:
  example.append({'imageUrl': '../localBgs/bgImage' + str(i),
                  'title': 'Searching for internet connection'})
  i += 1
with open('local1.json', 'w') as writefile:
  json.dump(example, writefile)
print('finished')
