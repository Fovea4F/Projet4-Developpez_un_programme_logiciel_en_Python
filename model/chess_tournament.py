# ---------------------------
# Tournament Class
# ---------------------------

class Tournament:
    """Tournament form instance initialisation
    Attributs :
    - name = ''
    - location = ''
    - begin_date = ''
    - end_date = ''
    - description = ''
    - status = ''
    - round_list = []
    - player_list = []
    - current_round_number = 0
    - round_number = 4
    - match_couple = ()
    """

    def __init__(self):
        self.name = ''
        self.location = ''
        self.begin_date = ''
        self.end_date = ''
        self.description = ''
        self.status = ''
        self.current_round_number = 0
        self.round_number = 4
        self.match_couple = []
        self.round_list = []
        self.player_list = []

    def form_fill(self,
                  _name,
                  _location,
                  _begin_date,
                  _end_date,
                  _description,
                  _round_number=4):
        """ fill tournament form mandatory attributs
        IN :    Name, Location, begin date, end date, description,
                round number, player list
        """
        self.name = _name
        self.location = _location
        self.begin_date = _begin_date
        self.end_date = _end_date
        self.description = _description
        self.round_number = _round_number
        self.round_list = []
        self.current_round_number = 0
        self.status = ''

    def add_registered_players_list(self, player_list):
        """Add the list of registered player in the tournament"""

        self.player_list = player_list

    def round_add(self, _round: list):
        """Add a round to round_list"""
        self.round_list.append(_round)

    def get_data(self):
        """get tournament's datas"""
        return [self.name,
                self.location,
                self.begin_date,
                self.end_date,
                self.description,
                self.round_number,
                self.player_list]

    def __str__(self):
        """print usage"""
        return f'{self.name} {self.location}\
            {self.begin_date} {self.end_date}\
                {self.description} {self.round_list}\
                    {self.player_list}\
                        {self.current_round_number}\
                        {self.round_number}'

    def __repr__(self) -> str:
        """Print usage"""
        return f'(name: {self.name}\
                    location: {self.location}\
                    begin_date: {self.begin_date}\
                    end_date: {self.end_date}\
                    description: {self.description}\
                    status: {self.status}\
                    round_list: {self.round_list}\
                    round_number: {self.round_number}\
                    current_round_number: {self.current_round_number}\
                    player_list: {self.player_list})'

    def __dict__(self) -> str:

        return f'({self.name}\
                {self.location}\
                {self.begin_date}\
                {self.end_date}\
                {self.description}\
                {self.status}\
                {self.round_list}\
                {self.round_number}\
                {self.current_round_number}\
                {self.player_list})'
