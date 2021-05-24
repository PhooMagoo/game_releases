# Collect information about upcoming game releases.

import bs4
import os
import requests
import webbrowser
from selenium import webdriver
from pprint import pprint

# Get the site we're gonna take info from.
site_url = "https://gamefaqs.gamespot.com/new"

# Let's open the bad boy.
browser = webdriver.Chrome()
browser.get(start_url)

