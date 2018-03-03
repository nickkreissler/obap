import ast
class Stats:
    def __init__(self):
        self.stats =['GP', 'MPG', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'TOV', 'PF', 'ORB', 'DRB', 'RPG', 'APG', 'SPG', 'BPG', 'PPG']
        self.players = ast.literal_eval(open('/Users/nicholaskreissler/Desktop/playersdata.txt','r').read())
        self.GP,self.MPG,self.FGM,self.FGA,self.FG,self.PM,self.PA,self.P,self.FTM,self.FTA,self.FT,self.TOV,self.PF,self.ORB,self.DRB,self.RPG,self.APG,self.SPG,self.BPG,self.PPG ={},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}
        self.lst=[self.GP,self.MPG,self.FGM,self.FGA,self.FG,self.PM,self.PA,self.P,self.FTM,self.FTA,self.FT,self.TOV,self.PF,self.ORB,self.DRB,self.RPG,self.APG,self.SPG,self.BPG,self.PPG]
        self.get_stat()
        self.write_stat()
    def get_stat(self):
        for i in self.players:
            for j in range(len(self.lst)):
                if float(self.players[i][self.stats[j]]) not in self.lst[j].keys(): self.lst[j][float(self.players[i][self.stats[j]])] = [i]
                else: self.lst[j][float(self.players[i][self.stats[j]])] += [i]
    def write_stat(self):
        for i in range(20):
            z = open('/Users/nicholaskreissler/Desktop/statsdata{}.txt'.format(self.stats[i]),'w+')
            z.write(str(self.lst[i]))
            z.close()
