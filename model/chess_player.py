"""Player management"""

import random
import string


class Player:
    """Player_form"""

    def __init__(self):
        """Player form creation"""

        self.player_id = ''
        self.name = ''
        self.firstname = ''
        self.birthday = ''
        self.total_score = 0
        self.list = ''

    def create(self, player_id, name, firstname, birthday):
        """Fill a new player instance"""

        self.player_id = player_id
        self.name = name
        self.firstname = firstname
        self.birthday = birthday

    def score_append(self, _score):
        """Add score match to player total score"""

        self.total_score += _score

    def sort(self, _player_list):
        """key sorted list"""

        temp_list = _player_list
        sorted(temp_list, key=lambda player: player.key_value)
        return temp_list

    def __str__(self):

        return f'Chess_ID : {self.player_id}\
                    Nom : {self.name} Prénom : {self.firstname}\
                    Date naissance :{self.birthday}\
                    Score :{self.total_score}'

    def __repr__(self):

        return f'ID: {self.player_id:<6} Nom:{self.name:<5} Prénom:{self.firstname:<3} / {self.birthday:<5}\
            Score:{self.total_score:<1}'


def get_player_id():
    """create a random ID (2CAPletters + 5 digits)"""
    prefix = random.choices(string.ascii_uppercase, k=2)
    number = random.choices(string.digits, k=5)
    return ''.join(prefix + number)
