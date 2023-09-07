"""Controller management"""

import os
import sys
from controller.controller_tools import round_score_update
from controller.controller_tools import round_and_match_create
from controller.controller_tools import read_from_json
from controller.controller_tools import find_player_from_json
from controller.controller_tools import update_json_with_player
from controller.controller_tools import save_data_to_json_file
from controller.controller_tools import serialize_tournament_list
from controller.controller_tools import deserialize_tournament
from controller.controller_tools import update_json_tournament_list

from model.chess_player import Player
from model.chess_tournament import Tournament
from model.chess_match import Match
from model.chess_round import Round
from view.chess_view import View


_round = Round()
chess_match = Match()

# data JSON files path
JSON_FILE_PATH = './data'
if not JSON_FILE_PATH:
    os.makedirs(JSON_FILE_PATH)

# JSON Files where data will be written
TOURNAMENT_MAIN_LIST_FILE_NAME = "tournament_main_list.json"
PLAYER_MAIN_LIST_FILE_NAME = "player_main_list.json"
# tournament_current_file_name = "tournament.json"

# JSON Files full names
tournament_main_list_file = f"{JSON_FILE_PATH}/{TOURNAMENT_MAIN_LIST_FILE_NAME}"
player_main_list_file = f"{JSON_FILE_PATH}/{PLAYER_MAIN_LIST_FILE_NAME}"
# tournament_current_file = f"{JSON_FILE_PATH}/{tournament_current_file_name}"


class Controller:
    """Chess Game Controller"""

    def __init__(self, _main_player_list='', _tournament_list=''):
        self.main_player_list = _main_player_list
        self.tournament_list = _tournament_list
        self.tournament = Tournament()
        self.view = View()
        self.tournament_current_file = ''

    def run(self):
        """Launcher program"""
        self.manage_main_menu()

    def manage_main_menu(self, _message='', choice=False):
        """The main menu management
        Root Menu"""

        message = _message
        choice = 'a'
        while choice not in ('1', '2', '3', '4', 'X', 'x', 'Q', 'q', 'O', 'o', 'N', 'n'):
            choice = self.view.show_main_menu(
                _tournament=self.tournament, _message=message)
        match choice:
            case "1":
                self.manage_tournament_menu_1()
            case "2":
                if self.tournament.name == '':
                    message = " Vous devez sélectionner un Tournoi "
                    self.manage_main_menu(_message=message)
                elif self.tournament.status == "started":
                    message = " Le tournoi est en cours, vous ne pouvez pas modifier ce tournoi"
                    self.manage_main_menu(_message=message)
                else:
                    self.manage_player_menu_2()
            case "3":
                self.manage_tournament_run_menu_3()
            case "4":
                self.manage_report_menu_4()
                # Reports
            case ('q' | 'Q'):
                message = " Vous souhaitez quitter le programme ? O/n "
                choice = self.view.show_main_menu(
                    _tournament=self.tournament, _message=message)
                message = ''
                match choice:
                    case 'o':
                        os.system("cls")
                        sys.exit(0)
                    case 'n':
                        self.manage_main_menu()
            case _:
                self.manage_main_menu()

    def manage_tournament_menu_1(self):
        """manage_menu1 management"""
        # ===  1. : Sélection / Création d'un tournoi     ===

        choice = False
        message = ''
        if (self.tournament.name != '') & (len(self.tournament.round_list) != 0):
            if not (self.tournament.round_list[-1].ended &
                    (self.tournament.round_number == len(self.tournament.round_list))):
                message = " Le tournoi est en cours, vous ne pouvez pas modifier ce tournoi"
                self.manage_main_menu(_message=message)
        while not choice:
            choice = self.view.show_menu_1(_tournament=self.tournament)
            match choice:
                case "1":
                    # ===  1.1 : Sélection d'un tournoi   ===
                    self.manage_tournament_selection_menu_1_1()
                case "2":
                    # ===  1.2 : Création d'un tournoi    ===
                    self.manage_tournament_registration_menu_1_2()
                case "x":
                    self.manage_main_menu()

    def manage_tournament_selection_menu_1_1(self):
        """manage_menu 1.1 management"""
        # Select Tournament in Registered Tournament List

        # chargement de la liste des tournois depuis le fichier json
        if not os.path.exists(tournament_main_list_file):
            message = "Aucun tournoi ne semble être présent dans la liste.\n Vous devez créer un tournoi"
            self.manage_main_menu(_message=message)
        else:
            self.tournament_list = deserialize_tournament(file=tournament_main_list_file)
            list_length = len(self.tournament_list)
            choice = False
            while not choice:
                choice = self.view.show_menu_1_1(
                    _tournament=self.tournament, _tournament_list=self.tournament_list)
                match choice:
                    case 'x':
                        self.manage_tournament_menu_1()
                    case _:
                        if (int(choice) > 0) & (int(choice) <= list_length):
                            # tournament_current_file_name = f"{file_id}_tournament.json"
                            # self.tournament_current_file = f"{JSON_FILE_PATH}/{tournament_current_file_name}"
                            for _ in enumerate(self.tournament_list, start=1):
                                match _[1].status:
                                    case "selected":
                                        if _[0] != choice:
                                            _[1].status = "registered"
                                        # self.manage_main_menu(_message=message)
                            self.tournament = Tournament()
                            self.tournament = self.tournament_list[int(choice) - 1]
                            if _[1].status == "registered":
                                self.tournament.status = "selected"
                            serialized_data = serialize_tournament_list(object=self.tournament_list)
                            save_data_to_json_file(objet=serialized_data, file=tournament_main_list_file)
                            # update_json_tournament_list(_tournament=self.tournament, _file=tournament_main_list_file)
                        else:
                            choice = False
                            self.manage_tournament_selection_menu_1_1()
            self.manage_main_menu()

    def manage_tournament_registration_menu_1_2(self):
        """manage_menu 1.2 management"""
        # Register a new tournament in tournament list

        tournament_form = {"name": "",
                           "location": "",
                           "description": "",
                           "begin_date": "",
                           "end_date": "",
                           "round_number": ""}
        choice = 'a'
        while True:
            name = self.view.show_menu_1_2(
                _message='name', _tournament_form=tournament_form)
            # name = input(" Nom du tournoi : ")
            if name in ('x', 'X'):
                self.manage_tournament_menu_1()
            else:
                tournament_form["name"] = name

            location = self.view.show_menu_1_2(
                _message='location', _tournament_form=tournament_form)
            # name = input(" Nom du tournoi : ")
            if location in ('x', 'X'):
                self.manage_tournament_menu_1()
            else:
                tournament_form["location"] = location

            description = self.view.show_menu_1_2(
                _message='description', _tournament_form=tournament_form)
            # name = input(" Nom du tournoi : ")
            if description in ('x', 'X'):
                self.manage_tournament_menu_1()
            else:
                tournament_form["description"] = description

            begin_date = self.view.show_menu_1_2(
                _message='begin_date', _tournament_form=tournament_form)
            if begin_date == 'x':
                self.manage_tournament_menu_1()
            else:
                tournament_form["begin_date"] = begin_date

            end_date = self.view.show_menu_1_2(
                _message='end_date', _tournament_form=tournament_form)
            if end_date == 'x':
                self.manage_tournament_menu_1()
            else:
                tournament_form["end_date"] = end_date

            round_number = self.view.show_menu_1_2(
                _message='round_number', _tournament_form=tournament_form)
            if round_number == 'x':
                self.manage_tournament_menu_1()
            elif round_number == '':
                round_number = 4
            tournament_form["round_number"] = round_number

            choice = self.view.show_menu_1_2(
                _message='validation', _tournament_form=tournament_form)
            match choice:
                case 'n':
                    self.manage_tournament_registration_menu_1_2()
                case 'o':
                    tournament = Tournament()
                    tournament.name = name
                    tournament.location = location
                    tournament.begin_date = begin_date
                    tournament.end_date = end_date
                    tournament.description = description
                    tournament.status = "registered"
                    tournament.round_number = round_number
                    tournament.round_list = []
                    tournament.player_list = []
                    tournament.match_couple = []
                    self.tournament_list = deserialize_tournament(
                        file=tournament_main_list_file)
                    self.tournament_list.append(tournament)
                    data_to_save = serialize_tournament_list(
                        object=self.tournament_list)
                    save_data_to_json_file(
                        objet=data_to_save, file=tournament_main_list_file)
            self.manage_tournament_menu_1()

    def manage_player_menu_2(self):
        """manage_menu 2 management"""
        # Players management

        choice = 'a'
        message = ''
        if (self.tournament.name != '') & (len(self.tournament.round_list) != 0):
            # if not (self.tournament.round_list[-1].ended &
            #         (self.tournament.round_number == len(self.tournament.round_list))):
            if self.tournament.status == "started":
                message = " Le tournoi est en cours, vous ne pouvez pas modifier ce tournoi"
                self.manage_main_menu(_message=message)
            elif self.tournament.status == "ended":
                message = " Le tournoi est terminé, vous ne pouvez plus modifier ce tournoi"
                self.manage_main_menu(_message=message)

        if self.tournament.name == '':
            message = "Vous devez sélectionner un tournoi"
            choice = self.view.show_main_menu(
                _tournament=self.tournament, _message=message)
        else:
            choice = self.view.show_menu_2(_tournament=self.tournament)
        match choice:
            case "1":
                # select players by name
                self.manage_player_selection_menu_2_1()
            case "2":
                # select players by firstname
                self.manage_player_register_menu_2_2()
            case "3":
                # view players list
                self.manage_player_list_menu_2_3()
            case "X" | "x":
                update_json_tournament_list(
                    _tournament=self.tournament, _file=tournament_main_list_file)
                self.manage_main_menu()
            case _:
                self.manage_main_menu()

    def manage_player_selection_menu_2_1(self, _message=''):
        """manage_menu 2.1 management"""
        # Selection d'un joueur parmi la liste des joueurs

        # load players from main players file
        main_player_list = read_from_json(player_main_list_file)
        self.main_player_list = sorted(main_player_list, key=lambda player: (player.name,
                                                                             player.firstname,
                                                                             player.birthday))
        message = _message
        choice = 'a'
        if len(self.main_player_list) == 0:
            # menu 2_1_0
            choice = self.view.show_menu_2_1(_tournament=self.tournament)
            if choice == 'x':
                self.manage_player_menu_2()
        else:
            # menu 2_1_1
            choice = self.view.show_menu_2_1_1(
                _tournament=self.tournament, _message=message)
            match choice:
                case '1':
                    # construction de la liste de nom en rapport avec la saisie de nom
                    selected_list = self.manage_player_name_selection_menu_2_1_1_1()
                case '2':
                    # construction de la liste de nom en rapport avec la saisie de prénom
                    selected_list = self.manage_player_firstname_selection_menu_2_1_1_2()
                case "X" | "x":
                    self.manage_player_menu_2()
                case _:
                    self.manage_player_menu_2()

            choice = 'a'
            while len(selected_list) > 0:
                choice = self.view.show_menu_2_1_2(_tournament=self.tournament,
                                                   _selected_player_list=selected_list)
                if choice == 'x':
                    self.manage_player_selection_menu_2_1()
                else:
                    choice = int(choice)-1
                    player = selected_list[choice]
                    if player in self.tournament.player_list:
                        selected_list.pop(choice)
                    else:
                        self.tournament.player_list.append(player)
                        selected_list.pop(choice)
                    choice = 'a'
        if self.tournament.status == "registered":
            self.tournament.status = "selected"
        update_json_tournament_list(
            _tournament=self.tournament, _file=tournament_main_list_file)
        self.manage_player_selection_menu_2_1()

    def manage_player_name_selection_menu_2_1_1_1(self):
        """Get player_list with player name filter"""

        name = self.view.show_menu_2_1_1_1(_tournament=self.tournament)
        if name in ('x', 'X'):
            self.manage_player_selection_menu_2_1()
        select_list = []
        select_list = find_player_from_json(
            file=player_main_list_file, key='name', value=name)
        selected_list = sorted(select_list, key=lambda player: (player.name,
                                                                player.firstname,
                                                                player.birthday))
        return selected_list

    def manage_player_firstname_selection_menu_2_1_1_2(self):
        """Get player_list with player firstname filter"""

        firstname = self.view.show_menu_2_1_1_2(_tournament=self.tournament)
        if firstname in ('x', 'X'):
            self.manage_player_selection_menu_2_1()
        select_list = []
        select_list = find_player_from_json(
            file=player_main_list_file, key='firstname', value=firstname)
        selected_list = sorted(select_list, key=lambda player: (player.name,
                                                                player.firstname,
                                                                player.birthday))
        return selected_list

    def manage_player_register_menu_2_2(self, _message='', _player_form=''):
        """manage_menu 2.2 management"""
        # Register new player in global players list

        if _player_form == '':
            player_form = {"player_id": "",
                           "name": "",
                           "firstname": "",
                           "birthday": ""}
        else:
            player_form = _player_form
        _player = Player()
        while True:

            player_id = self.view.show_menu_2_2(_tournament=self.tournament,
                                                _message='player_id',
                                                _player_form=player_form)
            match player_id:
                case 'X' | 'x':
                    self.manage_player_menu_2()
                case False:
                    player_form["player_id"] = "Le format de l'ID n'est pas respecté"
                    self.manage_player_register_menu_2_2(_message='player_id', _player_form=player_form)
                case _:
                    for _ in enumerate(self.main_player_list):
                        if _[1].player_id == player_id:
                            player_form["player_id"] = "Cet identifiant est déjà connu"
                            self.manage_player_register_menu_2_2(_message='player_id', _player_form=player_form)
                    player_form["player_id"] = player_id

            name = self.view.show_menu_2_2(_tournament=self.tournament,
                                           _message="name",
                                           _player_form=player_form)
            if name in ('x', 'X'):
                self.manage_player_menu_2()
            else:
                player_form['name'] = name

            firstname = self.view.show_menu_2_2(_tournament=self.tournament,
                                                _message="firstname",
                                                _player_form=player_form)
            if firstname in ('x', 'X'):
                self.manage_player_menu_2()
            else:
                player_form['firstname'] = firstname

            birthday = self.view.show_menu_2_2(_tournament=self.tournament,
                                               _message="birthday",
                                               _player_form=player_form)
            if birthday in ('x', 'X'):
                self.manage_player_menu_2()
            else:
                player_form['birthday'] = birthday

            validate_data = self.view.show_menu_2_2(_tournament=self.tournament,
                                                    _message='validate_data',
                                                    _player_form=player_form)
            if validate_data in ('N', 'n'):
                self.manage_player_register_menu_2_2()
            else:
                _player.player_id = player_id
                _player.name = name
                _player.firstname = firstname
                _player.birthday = birthday
                update_json_with_player(player=_player, file=player_main_list_file)

            choice = 'a'
            choice = self.view.show_menu_2_2(_tournament=self.tournament,
                                             _message='new_player',
                                             _player_form=player_form)
            match choice:
                case 'n':
                    self.manage_player_menu_2()
                case 'o':
                    self.manage_player_register_menu_2_2()

    def manage_player_list_menu_2_3(self):
        """ Sub menu 2.3 """
        # Show registered tournament list?  (O/n)

        _message = ''
        if len(self.tournament.player_list) == 0:
            _message = "player_list vide"
        self.view.show_menu_2_3(self.tournament.player_list, _message=_message)
        self.manage_player_menu_2()

    def manage_tournament_run_menu_3(self):
        """ Sub menu 3 """
        # Tournament Management Menu

        choice = 'a'
        if self.tournament.name == '':
            # tournament not valid, informations to fill
            message = "Le tournoi n'a pas été sélectionné"
            self.manage_main_menu(_message=message)
        elif len(self.tournament.player_list) < 2:
            message = " Vous devez compléter l'inscription des joueurs à ce tournoi "
            self.manage_main_menu(_message=message)
        elif len(self.tournament.player_list) % 2 != 0:
            message = " Le nombre de joueurs sélectionnés n'est pas pair ..."
            self.manage_main_menu(_message=message)

        if (len(self.tournament.round_list) == self.tournament.round_number):
            if self.tournament.round_list[-1].ended:
                # Game Over !
                message = "  Game OVER !  "
                self.tournament.status = "ended"
                while choice not in ('3', 'X', 'x'):
                    choice = self.view.show_menu_3(
                        _tournament=self.tournament, _message=message)
                match choice:
                    case '3':
                        self.manage_round_stats_menu_3_3()
                    case 'x':
                        update_json_tournament_list(
                            _tournament=self.tournament, _file=tournament_main_list_file)
                        self.manage_main_menu()

        if len(self.tournament.player_list) == 0:
            while choice != 'x':
                message = "Aucun joueur n'est inscrit à ce tournoi"
                choice = self.view.show_menu_3(
                    _tournament=self.tournament, _message=message)
            match choice:
                case '3':
                    self.manage_round_stats_menu_3_3()
                case 'x':
                    self.manage_main_menu()

        if len(self.tournament.round_list) == 0:
            choice = 'a'
            while choice not in ('1', '3', 'x'):
                message = "Le tournoi n'est pas encore démarré !"
                choice = self.view.show_menu_3(
                    _tournament=self.tournament, _message=message)
                message = ''
            match choice:
                case '1':
                    self.manage_round_run_menu_3_1()
                case '3':
                    self.manage_round_stats_menu_3_3()
                case 'x':
                    self.manage_main_menu()
        else:
            _round = self.tournament.round_list[-1]
            if _round.ended:
                choice = 'a'
                while choice not in ('1', '3', 'x'):
                    message = f"Le {_round.name} est clos"
                    choice = self.view.show_menu_3(
                        _tournament=self.tournament, _message=message)
                    message = ''
                match choice:
                    case '1':
                        self.manage_round_run_menu_3_1()
                    case '3':
                        self.manage_round_stats_menu_3_3()
                    case 'x':
                        self.manage_main_menu()

            else:
                choice = 'a'
                while choice not in ('2', '3', 'x'):
                    message = f"{self.tournament.round_list[-1].name} en cours de jeu."
                    choice = self.view.show_menu_3(
                        _tournament=self.tournament, _message=message)
                    message = ''
                match choice:
                    case '2':
                        self.manage_round_closure_menu_3_2()
                        # Round close management
                    case '3':
                        self.manage_round_stats_menu_3_3()
                        # Round Display
                    case 'x':
                        self.manage_main_menu()

    def manage_round_run_menu_3_1(self):
        """Tournament Round play: go..go..go....!"""

        choice = 'a'
        if self.tournament.round_number != 0:
            # test if last round is close and no more round is addable
            if len(self.tournament.round_list) == self.tournament.round_number:
                if self.tournament.round_list[-1].ended:
                    message = "La partie est terminée !"
                    self.tournament.status = "ended"
                    choice = self.view.show_menu_3_1(
                        _tournament=self.tournament, _message=message)

                else:
                    if len(self.tournament.round_list) != 0:
                        _round = self.tournament.round_list[-1]
                        if not _round.ended:
                            # last round in list still open
                            message = "Round actuellement en cours !"
                            choice = self.view.show_menu_3_1(
                                _tournament=self.tournament, _message=message)

                        else:
                            # Another round than first to create and launch
                            round_and_match_create(
                                _current_tournament=self.tournament)
                            _match = self.tournament.round_list[-1]
                            message = f"{_match.name} commencé"
                            choice = self.view.show_menu_3_1(
                                _tournament=self.tournament, _message=message)
                            message = ''
                            update_json_tournament_list(
                                _tournament=self.tournament, _file=tournament_main_list_file)
            else:
                # First round to create and launch
                round_and_match_create(_current_tournament=self.tournament)
                _match = self.tournament.round_list[-1]
                message = f"{_match.name} commencé"
                update_json_tournament_list(
                    _tournament=self.tournament, _file=tournament_main_list_file)
                choice = self.view.show_menu_3_1(
                    _tournament=self.tournament, _message=message)
                if choice != 'x':
                    choice = 'x'

        self.manage_tournament_run_menu_3()

    def manage_round_closure_menu_3_2(self):
        """Round closure
        Tournament matches scores set"""

        MESSAGE_1 = "Êtes-vous sûr de vouloir clore ce Round ? (O/n) "
        MESSAGE_2 = "Ce round est clos"
        MESSAGE_3 = "Saisie du score"
        # MESSAGE_4 = "La partie est terminée !"

        choice = 'a'
        if len(self.tournament.round_list) == 0:
            self.manage_round_run_menu_3_1()
        else:
            if not self.tournament.round_list[-1].ended:
                message = "Êtes-vous sûr de vouloir clore ce Round ? (O/n) "
                choice = self.view.show_menu_3_2(_tournament=self.tournament, _message=message)
                message = ''
                match choice:
                    case 'n':
                        self.manage_tournament_run_menu_3()
                    case 'x':
                        self.manage_tournament_run_menu_3()
                    case 'o':
                        _current_round = self.tournament.round_list[-1]
                        if _current_round.ended:
                            message = MESSAGE_2
                            choice = self.view.show_menu_3_2(
                                _tournament=self.tournament, _message=message)
                            message = ''
                            if choice == 'x':
                                self.manage_round_run_menu_3_1()
                        else:
                            for game in enumerate(_current_round.match_list, start=1):
                                player_A_id = game[1].player_a
                                index = 0
                                while self.tournament.player_list[index].player_id != player_A_id:
                                    index += 1
                                player_A = self.tournament.player_list[index]
                                message = MESSAGE_3
                                score_A = self.view.show_menu_3_2(_tournament=self.tournament,
                                                                  _message=message,
                                                                  _player=player_A)
                                message = ''
                                match score_A:
                                    # Only player_a score is mentioned, the other player score is calculated
                                    case 'P' | 'p':
                                        game[1].score_update(score_a=0.0)
                                    case 'N' | 'n':
                                        game[1].score_update(score_a=0.5)
                                    case 'G' | 'g':
                                        game[1].score_update(score_a=1.0)
                                    case 'X' | 'x':
                                        self.manage_round_closure_menu_3_2()
                            # Set ended and end_time round flags, report score to player in tournament
                            self.tournament.round_list[-1].close()
                            if self.tournament.round_number == len(self.tournament.round_list):
                                self.tournament.status = "ended"
                            result = round_score_update(self.tournament)
                            if result == 0:
                                update_json_tournament_list(_tournament=self.tournament,
                                                            _file=tournament_main_list_file)
                                message = []
                                for _ in enumerate(self.tournament.player_list, start=1):
                                    in_message = f"{_[0]} : {_[1]}"
                                    message.append(in_message)
                                choice = self.view.show_menu_3_2(
                                    _tournament=self.tournament, _message=message)
                                message = ''
                        self.manage_round_closure_menu_3_2()

        if choice in ('x', 'n'):
            choice = 'a'
        self.manage_tournament_run_menu_3()

    def manage_round_stats_menu_3_3(self):
        """Display Rounds stats"""

        choice = 'a'
        MESSAGE_1 = "Il n'y a pas de round sur ce tournoi.\n Le tournoi n'est pas commencé"
        if len(self.tournament.round_list) == 0:
            choice = self.view.show_menu_3_3(
                _tournament=self.tournament, _message=MESSAGE_1)
        else:
            choice = self.view.show_menu_3_3(_tournament=self.tournament)

        match choice:
            case 'x':
                self.manage_tournament_run_menu_3()
            case _:
                self.manage_tournament_run_menu_3()

    def manage_report_menu_4(self):
        """ Report main menu  """

        choice = 'a'
        if self.tournament.name == '':
            # tournament not valid, informations to fill
            self.manage_main_menu()

        choice = self.view.show_menu_4()
        match choice:
            case '1':
                if len(self.tournament.player_list) == 0:
                    self.manage_main_menu()
                else:
                    self.manage_report_menu_4_1()
            case '2':
                if self.tournament == '':
                    self.manage_main_menu()
                else:
                    self.manage_player_list_report_menu_4_2()
            case '3':
                if self.tournament.player_list == 0:
                    self.manage_main_menu()
                else:
                    self.manage_score_report_menu_4_3()
            case _:
                self.manage_main_menu()

    def manage_report_menu_4_1(self):
        """ manage general tournament information menu """

        choice = False
        while not choice:
            choice = self.view.show_menu_4_1(_tournament=self.tournament)
        self.manage_report_menu_4()

    def manage_player_list_report_menu_4_2(self):
        """ manage tournament player and round list menu """

        choice = False
        while not choice:
            choice = self.view.show_menu_4_2(_tournament=self.tournament)
        self.manage_report_menu_4()

    def manage_score_report_menu_4_3(self):
        """ manage score ranking menu"""

        choice = False
        while not choice:
            choice = self.view.show_menu_4_3(_tournament=self.tournament)
        self.manage_report_menu_4()
