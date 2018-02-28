import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
y=['GP', 'MPG', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'TOV', 'PF', 'ORB', 'DRB', 'RPG', 'APG', 'SPG', 'BPG', 'PPG']
x = {}

for i in range(1,60):
    context = ssl._create_unverified_context()
    response = urlopen("https://basketball.realgm.com/international/stats/2018/Averages/Qualified/All/points/All/desc/"+str(i), context=context)
    response = response.read().decode()
    soup = BeautifulSoup(response, 'lxml')
    for row in soup.findAll('table')[0].tbody.findAll('tr'):
        for j in range(len(row)):
            if j == 1:
                global v
                v = list(row)[j].string
                x[v]= {}
            if j >=3:
                x[v].update({y[j-3]:list(row)[j].string})
    z = open('playersdata.py','w+')
    z.write('a ='+str(x))
    z.close
    break
