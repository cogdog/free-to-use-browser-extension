import requests
import json
from functions import appendToList


def get_urls(url, items=[]):
  '''
  Retrieves the image URLs for items that have public URLs available.
  Skips over items that are for the colletion as a whole or web pages about the collection.
  Handles pagination.
  '''
  # request pages of 100 results at a time
  params = {"fo": "json", "c": 100, "at": "results,pagination"}
  call = requests.get(url, params=params)
  data = call.json()
  results = data['results']
  for result in results:
    print(result['access_restricted'])
    # don't try to get images from the collection-level result
    if "collection" not in result.get("original_format") and "web page" not in result.get("original_format"):
      # take the last URL listed in the image_url array
      if result.get("url"):
        item = result.get("url")
        if not result['access_restricted']:
          items.append(item)
  if data["pagination"]["next"] is not None:  # make sure we haven't hit the end of the pages
    next_url = data["pagination"]["next"]
    get_image_urls(next_url, items)

  return items


searchURL = input('Enter the url from the search: ')

with open('local.json') as json_data:
  existingJson = json.load(json_data)
for url in get_urls(searchURL):
  appendToList(url, existingJson)

with open('local.json', 'w') as writefile:
  json.dump(existingJson, writefile)
print('finished')
