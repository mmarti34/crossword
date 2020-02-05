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
import numpy as np
import matplotlib.pyplot as plt
import six



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

def int_test(x):
    if x in ['•']:
        return 0
    else:
        int(x)
        return int(x)


def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in  six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax


cj = browser_cookie.load()
r = requests.get('https://www.nytimes.com/puzzles/leaderboards', cookies=cj)
soup = BeautifulSoup(r.text, 'html.parser')
list_scores = soup.find_all('div', class_ = 'lbd-score')

#print(list_scores)
for item in list_scores:
        
    name = item.find('p', class_ = 'lbd-score__name').text
    if name == 'Michael Martinez (you)':
        name = 'Michael'
        names.append(name)
    elif name == 'liz ':
        name = 'Liz'
        names.append(name)
    elif name == 'Erin ':
        name = 'Erin'
        names.append(name)
    elif name == 'Joe ':
        name = 'Joe'
        names.append(name)
    elif name == 'Emilyshira ':
        name = 'Emilyshira'
        names.append(name)
    else:    
        names.append(name)
    
    #print(names)
    '''rank = item.find('p', class_ = 'lbd-score__rank')
    rank = int_test(rank.text)
    ranks.append(rank)
    '''
    
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
scoreboard = scoreboard.sort_values(by=['name'])


#scoreboard.to_csv('Scoreboard.csv', sep=',', mode='a', index=False, header=False)

average = pd.read_csv('Scoreboard.csv')
average = average[(average != 0).all(1)]
average = average.groupby(['Name']).mean()
average = average.sort_values(by='Time')
print(average)
#average.to_csv('average_time.csv', sep=',', index=True,header=True)

avg = pd.read_csv("average_time.csv")
avg = avg.round(2)
avg1 = avg[['Name','Time']]
x = render_mpl_table(avg1, header_columns=0, col_width=2.0).get_figure()
x.savefig("test.png")

avg2 = avg[['Name','Time']]
dates.pop(0)
avg2['Date'] = dates
avg2 = avg2.sort_values(by='Name')
#avg2.to_csv('Scoreboard_average.csv', sep=',', mode='a', index=False, header=False)

window = pd.read_csv("Scoreboard.csv")
start_date = datetime.datetime.now() + datetime.timedelta(-30)
window['Date'] = pd.to_datetime(window['Date'])
window = window[(window['Date'] >= start_date)]
window = window[(window != 0).all(1)]
window = window.groupby(['Name']).mean()
window['Date'] = dates
window2 = window[['Time', 'Date']]
window2 = window2.sort_values(by='Name')
#window2.to_csv('window_average.csv', sep=',', mode='a', index=False, header=False)
