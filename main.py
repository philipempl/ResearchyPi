from scholarly import scholarly
from PIL import Image 
import requests
from io import BytesIO

author = scholarly.search_author_id('Lu-BjV4AAAAJ')
author = scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])

print("H-Index: "+ str(author['hindex']))
print("Cited by: "+ str(author['citedby']))
print("Cites 2021: "+ str(author['cites_per_year'][2021]))
print("Publications: " + str(len(author['publications'])))

response = requests.get(author['url_picture'])
image_file = Image.open(BytesIO(response.content)) # open colour image
image_file = image_file.convert('L') # convert image to black and white
image_file.save('picture.bmp')
