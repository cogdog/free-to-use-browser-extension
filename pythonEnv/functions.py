import requests
import json
import csv
import math


def check_dimensions(imageURL):
  '''
  true when the picture is horizontal and at least 1024 pixels wide
  '''
  print(imageURL)
  indexOfHeight = imageURL.find('#h=') + 3
  endOfHeight = imageURL.find('&', indexOfHeight)
  height = int(imageURL[indexOfHeight:endOfHeight])
  indexOfWidth = endOfHeight + 3
  width = int(imageURL[indexOfWidth:])
  if width >= height and width >= 1024 and float(width) / float(height) < 2.5:
    return True
  else:
    return False


def parseImageURL(imageURL):
  '''
  converts image url from metadata to a url that works in a browser
  '''
  i = imageURL.find('#h=')
  if i != -1:
    return imageURL[2:i]
  else:
    return -1


def getJSON(url):
  '''
  returns the metadata associated with the image in json
  '''
  suffix = '/?fo=json'
  r = requests.get(url + suffix)
  if str(r) != '<Response [200]>':
    # print(r.json())
    return None
  r_data = r.json()
  print(url)
  parsedJSON = json.loads(json.dumps(r_data['item'], indent=2))
  return parsedJSON


def getImageURL(JSobject):
  '''
  returns the largest image url from metadata in json (including the dimensions of the photo)
  '''
  if JSobject['image_url']:
    if check_dimensions(JSobject['image_url'][-1]):
      return parseImageURL(JSobject['image_url'][-1])
  return -1


def getYear(JSobject):
  '''
  returns of publication from metadata in json
  '''
  if 'date' in JSobject:
    return JSobject['date']
  elif 'sort_date' in JSobject:
    return JSobject['sort_date']
  elif 'created_published_date' in JSobject:
    return JSobject['created_published_date']

  return -1


def getTitle(JSobject):
  '''
  returns title from metadata in json
  '''
  if 'title' in JSobject:
    return cutTitle(JSobject['title'])
  elif 'title_translation' in JSobject:
    return cutTitle(JSobject['title_translation'])
  elif 'other_title' in JSobject:
    return cutTitle(JSobject['other_title'])
  else:
    return -1


def cutTitle(longTitle):
  '''
  if a title's length exceeds 100 characters, finds the first space after the 100th character and replaces everything past that point with elipses
  '''
  temp = removeExtras(longTitle)
  title = checkPeriods(temp)
  if len(title) > 50 and title.find(' ', 50) != -1:
    return title[0:title.find(' ', 50)] + '...'
  else:
    return title


def removeExtras(title):
  '''
  gets rid of the brackets around many titles and the parentheses with which many end
  '''
  temp = title.replace('[', '')
  newTitle = temp.replace(']', '')
  if newTitle.find(')') == len(newTitle) - 1:
    return (newTitle[0:newTitle.find('(') - 1])
  else:
    return newTitle


def checkPeriods(title):
  '''
  if a title is several sentences long, returns the first sentence only
  '''
  if title.find('. ') == -1:
    return title
  elif title[title.rfind(' ', 0, title.find('. ')) + 1].isupper() or not title.find(' ') < title.find('. '):
    return title[0:title.find('. ') + 1] + ' ' + checkPeriods(title[title.find('. ') + 2:])
  else:
    return title[0:title.find('. ') + 1]


def makeListItem(url):
  '''
  takes a url and returns the corresponding json object
  '''
  jsonOb = getJSON(url)
  if jsonOb != None:
    imageURL = getImageURL(jsonOb)
    if imageURL != -1:
      return {'url': url, 'imageURL': 'https://' + imageURL,
              'title': getTitle(jsonOb), 'year': getYear(jsonOb)}


def appendToList(url, existingJson):
  item = makeListItem(url)
  if item != None and item not in existingJson:
    existingJson.append(item)
