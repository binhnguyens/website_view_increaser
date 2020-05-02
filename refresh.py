# -*- coding: utf-8 -*-
"""
File for Thu to refresh pages 
"""

from selenium import webdriver
import time
from tkinter.filedialog import askopenfilename

filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print('Your file is: ',filename)

# Take the websites and place them into lists
f = open(filename, "r")
articles = []
for x in f:
    if x == '\n':
        pass
    else:
        articles.append(x.replace ("\n",""))
    

browser = webdriver.Chrome()

# Open a new window
for i in range (1, len (articles)):
    browser.execute_script("window.open('');")

# Open the browser, wait 10 seconds to refresh, do this every 120 seconds
j=0
while True:
    for i in range (0,len(articles)):
        browser.switch_to.window(browser.window_handles[i])
        browser.get(articles[i])
        time.sleep (5)

    j+=1
    print ('iteration: ',j)
    time.sleep (10)
