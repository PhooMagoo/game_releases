# Collect information about upcoming game releases.

import pyautogui
import re
import pandas as pd
from selenium import webdriver
from pprint import pprint

# Get the site we're gonna take info from.
site_url = "https://gamefaqs.gamespot.com/new"

# How we're gonna find the games and releases.
regexName = re.compile('<div class="sr_name"><a href="(.*?)">(.*?)</a>')
regexDate = re.compile('<div class="sr_info">(.*)')

### Let's open the bad boy.
##browser = webdriver.Chrome()
##browser.get(site_url)
##
##pyautogui.rightClick(870, 480)
##pyautogui.click(940, 720)
##pyautogui.hotkey('ctrl', 'a')
##pyautogui.hotkey('ctrl', 'c')

# Open our text file, because apparently this is how we're going to handle it.
text_file = open("game_releases.txt", "r")

res = text_file.read()

names = regexName.findall(res)
dates = regexDate.findall(res)

newDates = []
newNames = []

newList = dict()

for x, y in names:
    newNames.append(y)

for date in dates:
    if "</div>" in date:
       newDates.append(date.replace("</div>", ""))
    else:
        newDates.append(date)

for name in newNames:
    for date in newDates:
        newList[name] = date

pprint(newList)
