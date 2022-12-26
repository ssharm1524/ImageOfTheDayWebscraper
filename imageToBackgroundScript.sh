#!/bin/bash

# Run our python script to get today's image onto local machine
python "/Users/shivsharma/Local Repos/ImageOfTheDayWebScraper/ImageOfTheDay.py"

# Set background
path="/Users/shivsharma/Local Repos/ImageOfTheDayWebScraper/nasaimg.jpg" 
osascript -e 'tell application "Finder" to set desktop picture to POSIX file "'"$path"'"'

# Check success
ret=$? 
if [ $ret == "0" ]; then 
echo "Wallpaper set successfully " 
else 
echo "Operation failed." 
fi

# Remove the file
rm "/Users/shivsharma/Local Repos/ImageOfTheDayWebScraper/nasaimg.jpg"
