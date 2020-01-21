# -*- coding: utf-8 -*-
"""
Created on Jan 13 15:13:16 2019

@author: michael.martinez
"""

#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
import requests
import browser_cookie3 as browser_cookie
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd



names = []
ranks = []
times = []
dates = []

#options = webdriver.ChromeOptions()
#options.add_argument(r"user-data-dir=C:\Users\michael.b.martinez\AppData\Local\Google\Chrome\User Data")
#fp = webdriver.FirefoxProfile(r'C:\Users\michael.b.martinez\AppData\Roaming\Mozilla\Firefox\Profiles\scc3c5xn.Michael')

#browser = webdriver.Chrome(chrome_options=options)
#url = "https://www.nytimes.com/puzzles/leaderboards"
#browser.get(url) #navigate to the page
def get_sec(time_str):
    """Get Seconds from time."""
    if time_str in ['--']:
        return 0
    else:
        m, s = time_str.split(':')
        #print(m)
        #print(s)
        return int(m) * 60 + int(s)


cj = browser_cookie.load()
r = requests.get('https://www.nytimes.com/puzzles/leaderboards', cookies=cj)
soup = BeautifulSoup(r.text, 'html.parser')
list_scores = soup.find_all('div', class_ = 'lbd-score')

#print(list_scores)
for item in list_scores:
        
    name = item.find('p', class_ = 'lbd-score__name').text
    names.append(name)
    
    #print(names)
    
    rank = item.find('p', class_ = 'lbd-score__rank').text
    ranks.append(rank)
    
    #print(ranks)
    
    time = item.find('p', class_ = 'lbd-score__time')
    
    if time is not None:
        time = get_sec(time.text)
        times.append(time)
        
    else:
        time = '0'
        times.append(time)
        
    date1 = date.today()
    #print(date1)
    dates.append(date1)
    #print(dates)
    #print(names, ranks, times, dates)
    

scoreboard = pd.DataFrame({'name': names, 'time': times, 'date': dates})
print(scoreboard)

scoreboard.to_csv('Scoreboard.csv', sep=',', mode='a', index=False, header=False)

