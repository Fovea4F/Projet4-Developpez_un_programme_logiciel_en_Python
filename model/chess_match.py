# ---------------------------
# Tournament Match
# ---------------------------

class Match():
    """Add a match instance
    IN  :   [player_a, player_b]
    OUT : Tuple ([player_id_a, score_a], [player_id_b, score_b])
    """

    def __init__(self, player_a='', player_b='', score_a=0.0, score_b=0.0):
        """ Instance init"""
        self._player_a = player_a
        self._player_b = player_b
        self._score_a = score_a
        self._score_b = score_b
        self._match_tuple = ([self._player_a, self.score_a],
                             [self._player_b, self.score_b])

    @property
    def player_a(self):
        """direct access to player_a element in the tuple Match"""
        return self._player_a

    @player_a.setter
    def player_a(self, player_a):
        """direct access to player_a element in the tuple Match"""
        self._player_a = player_a

    @property
    def player_b(self):
        """direct access to player_b element in the tuple Match"""
        return self._player_b

    @player_b.setter
    def player_b(self, player_b):
        """direct access to player_b element in the tuple Match"""
        self._player_b = player_b

    @property
    def score_a(self):
        """direct access to score_a element in the tuple Match"""
        return self._score_a

    @score_a.setter
    def score_a(self, score_a):
        """direct access to score_a element in the tuple Match"""
        self._score_a = score_a

    @property
    def score_b(self):
        """direct access to score_b element in the tuple Match"""
        return self._score_b

    @score_b.setter
    def score_b(self, score_b):
        """direct access to score_b element in the tuple Match"""
        self._score_b = score_b

    def display(self):
        """display a match content
        IN : ()
        """
        print(f"{self._player_a:<5} contre {self._player_b:<5}\
              {self._score_a:<5} / {self._score_b:<5}")

    def display_players(self):
        """display a   match content
        IN : ()
        """
        print(f"{self._player_a:<5} contre {self._player_b:<5}")

    def score_update(self, score_a):
        """update score for every player of the match"""
        score_a = float(score_a)
        self._score_a = score_a
        match score_a:
            case 0.0:
                self._score_b = 1.0
            case 0.5:
                self._score_b = 0.5
            case 1.0:
                self._score_b = 0.0
        new_match_tuple = [[self.player_a, self.score_a], [self.player_b, self.score_b]]
        self._match_tuple = tuple(new_match_tuple)
        print()

    def set_tuple(self, player_a='', player_b='', score_a='', score_b=''):
        """ Set new values in match tuple"""

        match_new_value = [[player_a, score_a], [player_b, score_b]]
        self._match_tuple = tuple(match_new_value)

    def __str__(self):
        """Print purpose"""
        return f"{self._player_a},{self._score_a} {self._player_b},\
                 {self._score_b}"

    def __repr__(self):
        """Print purpose"""
        return f"Match : player_id_a: {self._player_a}\
                         player_id_b: {self._player_b}\
                         score_a: {self._score_a}\
                         score_b: {self._score_b}"
