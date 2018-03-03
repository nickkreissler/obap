from players import Players
from stats import Stats
from team import LeaguesData

class Update:
    def __init__(self):
        self.players = Players()
        self.stats = Stats()
        self.leaguesdata = LeaguesData()
