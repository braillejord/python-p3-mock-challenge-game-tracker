class Game:
    all = []

    def __init__(self, title):
        if type(title) is str and len(title) > 0:
            self._title = title
        else:
            raise Exception("Title must be a string.")

        Game.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self):
        raise Exception("Title cannot be changed.")

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return [game.player for game in Result.all if game.game == self]

    def average_score(self, player):
        search = [game.score for game in Result.all if game.game == self and game.player == player]

        return sum(search) / len(search)


from classes.result import Result
