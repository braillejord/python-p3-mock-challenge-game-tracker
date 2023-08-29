class Player:
    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if type(new_username) is str and 2 <= len(new_username) <= 16:
            self._username = new_username
        else:
            raise Exception("Username must be a string between 2 and 16 characters.")

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return [result.game for result in Result.all if result.player == self]

    def played_game(self, game):
        if [result for result in Result.all if result.player == self and result.game == game]:
            return True
        else:
            return False

    def num_times_played(self, game):
        return len(
            [result for result in Result.all if result.player == self and result.game == game]
        )

    @classmethod
    def highest_scored(cls, game):
        pass


from classes.result import Result
