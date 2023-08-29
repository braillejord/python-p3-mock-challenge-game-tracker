class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        if type(new_score) is int and 1 <= new_score <= 5000:
            self._score = new_score
        else:
            raise Exception("Score must be an integer between 1 and 5000.")

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, new_player):
        if isinstance(new_player, Player):
            self._player = new_player
        else:
            raise Exception("Player must be of type Player.")

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, new_game):
        if isinstance(new_game, Game):
            self._game = new_game
        else:
            raise Exception("Game must be of type Game.")


from classes.player import Player
from classes.game import Game
