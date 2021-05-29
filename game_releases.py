# Collect information about upcoming game releases.

from tkinter import Tk
import pyautogui
import re
import pandas as pd
from selenium import webdriver
from pprint import pprint

# Set up our variables.
newDates = []
newNames = []
copyText = ""
i = 0

# Get the site we're gonna take info from.
site_url = "https://gamefaqs.gamespot.com/new"

# How we're gonna find the games and releases.
regexName = re.compile('<div class="sr_name"><a href="(.*?)">(.*?)</a>')
regexDate = re.compile('<div class="sr_info">(.*)')

# Let's open the bad boy.
browser = webdriver.Chrome()
browser.get(site_url)

# Copy the HTML from our specified site.
pyautogui.rightClick(870, 480)
pyautogui.click(940, 720)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

# Shove that HTML into an object.
res = Tk().clipboard_get()

# Filter out everything but the names and dates of new / upcoming releases.
names = regexName.findall(res)
dates = regexDate.findall(res)

# We have some straggler HTML, so we strip out just the name. 
for x, y in names:
    newNames.append(y)

# We have some straggler HTML for some of the dates, so we get rid of that.
for date in dates:
    if "</div>" in date:
       newDates.append(date.replace("</div>", ""))
    else:
        newDates.append(date)

# Format the text in a pleasing way, and...
for name in newNames:
    copyText += newNames[i] + " : " + newDates[i] + ", \n"
    i = i + 1

# ...shove it into our game_releases file.
with open("game_releases.txt", "w") as f:
    f.write(copyText)
