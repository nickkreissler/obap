import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
class LeaguesData:
    def __init__(self):
        self.context = ssl._create_unverified_context()
        response = urlopen("https://basketball.realgm.com/international/teams",context=self.context)
        response = response.read().decode()
        soup = BeautifulSoup(response, 'html.parser')
        x = soup.findAll('td')
        a=0
        c=0
        b={}
        for i in x:
            if a % 4!=0:
                b[c]+=[i.string]
                a+=1
            else:
                c+=1
                b[c]=[i.string]
                a+=1
        self.c = {}
        for i in b:
            self.c[i]=[]
            for j in b[i]:
                if j != None and j != '\xa0':
                    self.c[i]+=[j]

        d=[]
        y = soup.findAll('a',href = True,text='Roster')
        for link in y:
            d+=[link['href']]
        f = 0
        for i in self.c:
            self.c[i]+=[d[f]]
            f+=1
        self.team={}
        self.players={}
        self.League={}
        self.teamL={}
        self.teams()
        self.player()
        self.league()
        self.teaml()
        self.write()
    def teams(self):
        for i in self.c:
            response = urlopen("https://basketball.realgm.com/{}".format(self.c[i][len(self.c[i])-1]),context=self.context)
            response = response.read().decode()
            soup = BeautifulSoup(response, 'lxml')
            for row in soup.findAll('table')[0].tbody.findAll('tr'):
                second_column = row.findAll('td')[1].contents
                for W in second_column:
                    if self.c[i][0] not in self.team.keys(): self.team[self.c[i][0]] = [W.string]
                    else: self.team[self.c[i][0]] += [W.string]
    def player(self):
        for i in self.team:
            for j in self.team[i]:
                self.players[j] = i

    def league(self):
        for i in self.c:
            if self.c[i][len(self.c[i])-2] not in self.League.keys(): self.League[self.c[i][len(self.c[i])-2]] = [self.c[i][0]]
            else: self.League[self.c[i][len(self.c[i])-2]] += [self.c[i][0]]
    def teaml(self):
        for i in self.c: self.teamL[self.c[i][0]] = self.c[i][len(self.c[i])-2]

    def write(self):
        x = [self.team,self.players,self.League,self.teamL]
        y = ['team.txt','players.txt','League.txt','teamleague.txt']
        for i in range(len(x)):
            c = open('/Users/nicholaskreissler/Desktop/{}'.format(y[i]),'w+')
            c.write(str(x[i]))
            c.close()
