from datetime import datetime

class Game:
    def __init__(self, gangs, date=None, results=None):
        self.gangs = gangs
        self.date = date or datetime.now()
        self.results = results or {}

    def set_result(self, gang, result):
        self.results[gang] = result

class Campaign:
    def __init__(self, name, games=None):
        self.name = name
        self.games = games or []

    def add_game(self, game):
        self.games.append(game)

    def remove_game(self, game):
        self.games.remove(game)
