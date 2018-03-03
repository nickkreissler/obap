import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Players(object):
    def  __init__(self):
        self.stats=['GP', 'MPG', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'TOV', 'PF', 'ORB', 'DRB', 'RPG', 'APG', 'SPG', 'BPG', 'PPG']
        self.players = {}
        self.getplayer()
        self.writeplayers()
    def getplayer(self):
        for i in range(1,60):
            context = ssl._create_unverified_context()
            response = urlopen("https://basketball.realgm.com/international/stats/2018/Averages/Qualified/All/points/All/desc/"+str(i), context=context)
            response = response.read().decode()
            soup = BeautifulSoup(response, 'html.parser')
            for row in soup.findAll('table')[0].tbody.findAll('tr'):
                for j in range(len(row)):
                    if j == 1:
                        global v
                        v = list(row)[j].string
                        self.players[v]= {}
                    if j >=3:
                        self.players[v].update({self.stats[j-3]:list(row)[j].string})
    def writeplayers(self):
        z = open('/Users/nicholaskreissler/Desktop/playersdata.txt','w+')
        z.write(str(self.players))
        z.close()



