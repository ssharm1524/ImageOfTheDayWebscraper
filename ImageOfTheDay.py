import requests
import json
from datetime import datetime
import os

FILENAME = 'nasa_pic.png'

print(datetime.today().strftime('%Y-%m-%d'))

params = {
    "api_key": "DEMO_KEY",
    "hd": "True",
    "date": datetime.today().strftime('%Y-%m-%d'),
}

response = requests.get("https://api.nasa.gov/planetary/apod", params)

if response and response.status_code == 200:
    print("Successful Response")

assert (response and response.ok), "NASA API failed to respond with the image."


resObj = response.json()

if resObj["media_type"] == "image":
    url = resObj["hdurl"] if resObj["hdurl"] else resObj["url"]
else:
    url = resObj["thumbnail_url"]

path = os.path.expanduser('~')+"/Desktop/nasaimg.jpg"

try:
    open(path, "xb").write(requests.get(url, allow_redirects=True).content)
except FileExistsError:
    print('file extist')
    open(path, "wb").write(requests.get(url, allow_redirects=True).content)
