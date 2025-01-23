import json
from requests import *
from functions import makeListItem, appendToList
url = "https://www.loc.gov/item/2016893576/"
existingJson = []

with open('local.json') as json_data:
  existingJson = json.load(json_data)

# for loop would begin here
appendToList(url, existingJson)
# end of part that would go in for loop

with open('local.json', 'w') as writefile:
  json.dump(existingJson, writefile)
print('finished')
