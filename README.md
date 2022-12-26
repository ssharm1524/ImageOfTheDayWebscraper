# ImageOfTheDayWebscraper

Webscraping python script that gets NASA's Image of the Day and sets it as my Desktop Background
DISCLAMER: All work is my own and therefore uses my custom pathnames. To replicate, ensure you use your own paths.

To run this shell script everyday, did the following on the command line in my home directory:
$crontab -e

This opens vim. Hit "i" to enter insert mode. Pasted the following:
0 0 \* \* \* bash "/Users/shivsharma/Local Repos/ImageOfTheDayWebScraper/imageToBackgroundScript.sh"
