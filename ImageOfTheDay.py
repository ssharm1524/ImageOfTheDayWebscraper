import requests
import json
from datetime import datetime
import os

# Get the data from NASA's API
params = {
    "api_key": "DEMO_KEY",
    "hd": "True",
    "date": datetime.today().strftime('%Y-%m-%d'),
}
response = requests.get("https://api.nasa.gov/planetary/apod", params)
assert (response and response.ok), "NASA API failed to respond with the image."
resObj = response.json()

# Parse response to determine if APOD is an hd image, regular image, or video. Set url accordingly
if resObj["media_type"] == "image":
    url = resObj["hdurl"] if resObj["hdurl"] else resObj["url"]
else:
    url = resObj["thumbnail_url"]

# Write data from the given image url to a local file for our shell script to use
path = os.path.expanduser(
    '~')+"/Local Repos/ImageOfTheDayWebScraper/nasaimg.jpg"
try:
    open(path, "xb").write(requests.get(url, allow_redirects=True).content)
except FileExistsError:
    print('file extist')
    open(path, "wb").write(requests.get(url, allow_redirects=True).content)
