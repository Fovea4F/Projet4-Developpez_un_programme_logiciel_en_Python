""" User interactions """

import os
from view.view_tools import user_input, is_valid_date, valid_id


class View:
    """View: manage every interface with human
    Manages Input and Output
    """

    def show_main_menu(self, _tournament='', _message=''):
        """Main menu User Interface"""

        choice = 'a'
        if _message == '':
            if (_tournament.name == ''):
                _message = "Aucun tournoi sélectionné, faites votre choix !"
            elif len(_tournament.player_list) == 0:
                _message = "Vous devez maintenant sélectionner des joueurs"
        os.system("cls")
        print("="*80)
        print("===                              Menu principal                              ===")
        print("="*80)
        if _tournament == '':
            print("=== Tournoi :  ")
        else:
            print(f"=== Tournoi : {_tournament.name} ")
        print("="*80)
        print("===                   Gestion d'un tournoi de Jeu d'échecs                   ===")
        print("="*80)
        print("===  1.   TOURNOI : Sélection ou Création                                    ===")
        print("===  2.   JOUEURS : Sélection ou Enregistrement                              ===")
        print("===  3.   JEU :     Lancement du tournoi / rounds                            ===")
        print("="*80)
        print("===  4.   Rapports                                                           ===")
        print("="*80)
        print("===  Q.   Quitter l'application                                              ===")
        print("="*80)
        print()
        if _message != '':
            print(f" Message : {_message} ")
        print()
        match _message:
            case " Vous souhaitez quitter le programme ? O/n ":
                print()
                while choice not in ('O', 'o', 'N', 'n'):
                    user_input(" Choix : ")
                    choice = input()
                if choice in ('N', 'n'):
                    choice = 'n'
                else:
                    choice = 'o'
                return choice
            case "Aucun tournoi sélectionné, faites votre choix !":
                print()
                while choice not in ('1', '3', '4', 'q', 'Q'):
                    user_input(_msg=" Choix : ")
                    choice = input()
                return choice
            case _:
                while choice not in ('1', '2', '3', '4', 'q', 'Q'):
                    user_input(_msg=" Choix : ")
                    choice = input()
                return choice

    def show_menu_1(self, _tournament=''):
        """menu_1 : Mainly Selection or add tournament"""
        # Select or create Tournament

        os.system("cls")
        print("="*80)
        print("===                             Menu 1 (TOURNOI)                             ===")
        print("="*80)
        print(f"===          Tournoi :  {_tournament.name}")
        print("="*80)
        print("===  1. : Sélectionner un tournoi depuis la liste                            ===")
        print("===  2. : Enregistrer un nouveau tournoi                                     ===")
        print("="*80)
        print("===  x. : Revenir au menu principal                                          ===")
        print("="*80)
        print()
        choice = 'a'
        while choice not in ('1', '2', 'x'):
            user_input(" Choix :  ")
            choice = input()
        return choice

    def show_menu_1_1(self, _tournament='', _tournament_list=''):
        """Sub menu 1.1 Show Tournament list for selection"""

        os.system("cls")
        if len(_tournament_list) == 0:
            print("="*80)
            print("===                            Menu 1.1 (TOURNOI)                            ===")
            print("="*80)
            print("===                                                                          ===")
            print("="*80)
            print("===                    Il n'y a pas de tournoi enregistré                    ===")
            print("="*80)
            print("===  x. : Retour au menu principal                                           ===")
            print("="*80)
            print()
            choice = 'a'
            while choice != 'x':
                user_input(_msg=" Choix : ")
            return choice

        else:
            print("="*80)
            print("===                            Menu 1.1 (TOURNOI)                            ===")
            print("="*80)
            print(f"=== Tournoi :     {_tournament.name}")
            print("="*80)
            print("===                          Sélectionner un tournoi                         ===")
            print("="*80)
            print("=== {:<5}{:<20}{:<15}{:<40}".format("Rang", "Date de début", "État", "Nom"))
            print("="*80)
            for _ in enumerate(_tournament_list, start=1):
                status = _[1].status
                match status:
                    case "registered":
                        status = "enregistré"
                    case "selected":
                        status = "sélectionné"
                    case "started":
                        status = "en cours"
                    case "ended":
                        status = "terminé"
                print("=== {:<5}{:<20}{:<15}{:<40}".format(_[0], _[1].begin_date, status, _[1].name))
                """print(f"=== {_[0]}.{'':<2} {'Nom           : ':<15}{_[1].name}")
                print(f"=== {'':<5}{'Lieu          : ':<15}{_[1].location}")
                print(f"=== {'':<5}{'Date de début : ':<15}{_[1].begin_date}")
                print(f"=== {'':<5}{'Date de fin   : ':<15}{_[1].begin_date}")"""
                if not (_[1] == _tournament_list[-1]):
                    print("-"*80)
            print("="*80)
            print("===  x. Retour au menu précédent                                             ===")
            print("="*80)
            print()
            tournament_number_list = []
            for _ in enumerate(_tournament_list, start=1):
                tournament_number_list.append(str(_[0]))
            tournament_number_list.append('x')
            tournament_number_list.append('X')
            choice = 'a'
            while choice not in (tournament_number_list):
                user_input(_msg=" Choix : ")
                choice = input()
            return choice

    def show_menu_1_2(self, _tournament='', _tournament_form='', _message=''):
        """Sub menu 1.2 Show Menu for
        New Tournament registration"""

        name = _tournament_form.get('name', '')
        location = _tournament_form.get('location', '')
        begin_date = _tournament_form.get('begin_date', '')
        end_date = _tournament_form.get('end_date', '')
        description = _tournament_form.get('description', '')
        round_number = _tournament_form.get('round_number', '')

        os.system("cls")
        print("="*80)
        print("===                            Menu 1.2 (TOURNOI)                            ===")
        print("="*80)
        print(f"=== Tournoi :   {name}")
        print("="*80)
        print("===                    Création d'un tournoi : Formulaire                    ===")
        print("="*80)
        if name != '':
            print(f"=== {'':<5}{'Nom               : ':<20}{name}")
        else:
            print(f"=== {'':<5}Nom               : ")
        if location != '':
            print(f"=== {'':<5}{'Lieu              : ':<20}{location}")
        else:
            print(f"=== {'':<5}Lieu              : ")
        if description != '':
            print(f"=== {'':<5}{'Description       : ':<20}{description}")
        else:
            print(f"=== {'':<5}Description       : ")
        if begin_date != '':
            print(f"=== {'':<5}{'Date de début     : ':<20}{begin_date}")
        else:
            print(f"=== {'':<5}Date de début     : ")
        if end_date != '':
            print(f"=== {'':<5}{'Date de fin       : ':<20}{end_date}")
        else:
            print(f"=== {'':<5}Date de fin       : ")
        if round_number != '':
            print(f"=== {'':<5}{'Nombre de tours   : ':<20}{round_number}")
        else:
            print(f"=== {'':<5}Nombre de tours   : ")
        print("="*80)
        print("===  x. : Retour au menu précédent                                           ===")
        print("="*80)
        print()
        begin_date = "29/02/2023"
        end_date = "29/02/2023"
        match _message:

            case 'name':
                while not ((name != '') | (name in ('x', 'X'))):
                    user_input(_msg=" Nom du tournoi : ")
                    name = input()
                return name

            case 'location':
                while not ((location != '') | (location in ('x', 'X'))):
                    user_input(_msg=" Lieu du déroulement du tournoi : ")
                    location = input()
                return location

            case 'description':
                while not ((description != '') | (description in ('x', 'X'))):
                    user_input(_msg="Description du tournoi : ")
                    description = input()
                return description

            case 'begin_date':
                while not (is_valid_date(begin_date) | (begin_date in ('x', 'X'))):
                    user_input(_msg="Date de début du tournoi : ")
                    begin_date = input()
                if begin_date in ('x', 'X'):
                    begin_date = 'x'
                return begin_date

            case 'end_date':
                while not (is_valid_date(end_date) | (end_date in ('x', 'X'))):
                    user_input(_msg="Date de début du tournoi : ")
                    end_date = input()
                if end_date in ('x', 'X'):
                    end_date = 'x'
                return end_date

            case 'round_number':
                round_number = 'a'
                while not (round_number.isdigit() | (round_number in ('', 'x', 'X'))):
                    user_input(_msg=" Nombre de tours : ")
                    round_number = input()
                match round_number:
                    case 'X' | 'x':
                        round_number = 'x'
                    case '':
                        round_number = ''
                    case _:
                        if not round_number.isdigit():
                            round_number = 'a'
                        elif int(round_number) <= 0:
                            round_number = ''
                        else:
                            round_number = int(round_number)
                return round_number

            case 'validation':
                choice = 'a'
                while choice not in ('O', 'o', 'N', 'n'):
                    user_input(_msg=" Souhaitez-vous valider les données  (O/n) ? : ")
                    choice = input()
                match choice:
                    case 'N' | 'n':
                        choice = 'n'
                    case 'O' | 'o':
                        choice = 'o'
                return choice

    def show_menu_2(self, _tournament='', _message=''):
        """Sub menu 2 User interface
        Select or register player"""

        os.system("cls")
        if len(_tournament.player_list) == 0:
            registered_players = "Actuellement, aucun joueur n'est inscrit"
        else:
            registered_players = f" {len(_tournament.player_list)} joueurs sont inscrits"
        print("="*80)
        print("===                             Menu 2 (JOUEURS)                             ===")
        print("="*80)
        print(f"=== Tournoi : {_tournament.name}")
        print("="*80)
        print("===           Selection / Enregistrement des joueurs                         ===")
        print("="*80)
        print("=== 1. : Selection de joueurs dans le répertoire                             ===")
        print("=== 2. : Enregistrement de nouveaux joueurs                                  ===")
        print("="*80)
        print("=== 3. : Affichage Liste de joueurs du tournoi                               ===")
        print("="*80)
        print(f" Message : {_message}")
        print(f" Nombre de joueurs inscrits : {registered_players}")
        print("="*80)
        print("=== x. : Revenir au menu principal                                           ===")
        print("="*80)
        print()
        choice = 'a'
        while choice not in ('1', '2', '3', 'x'):
            user_input(" Choix : ")
            choice = input()
        return choice

    def show_menu_2_1(self, _tournament='', _message=''):
        """ Sub menu 2.1.0 Screen
            Root Player selection and creation
            User Interface """

        os.system("cls")
        print("="*80)
        print("===                           Menu 2.1.0 (JOUEURS)                           ===")
        print("="*80)
        print(f"=== Tournoi : {_tournament.name}")
        print("="*80)
        print("===   Vous devez enregistrer manuellement les joueurs.                       ===")
        print("="*80)
        print("=== x.  : Revenir au menu précédent                                          ===")
        print("="*80)
        print()
        choice = 'a'
        while choice != 'x':
            user_input(" Choix : ")
            choice = input()
        return choice

    def show_menu_2_1_1(self, _tournament='', _message=''):
        """Sub menu 2.1.1 Screen
         Root Player selection
         User Interface """

        os.system("cls")
        print("="*80)
        print("===                           Menu 2.1.1 (JOUEURS)                           ===")
        print("="*80)
        print(f"=== Tournoi : {_tournament.name}")
        print("="*80)
        print("=== 1. Sélection dans la liste, trié par nom    :                            ===")
        print("=== 2. Sélection dans la liste, trié par prénom :                            ===")
        print("="*80)
        if _message != '':
            print(f"=== Message :  {_message}")
            print("="*80)
        print("=== x.  : Revenir au menu précédent                                          ===")
        print("="*80)
        print()
        choice = 'a'
        while choice not in ('1', '2', 'x'):
            user_input(" Choix : ")
            choice = input()
        return choice

    def show_menu_2_1_1_1(self, _tournament=''):
        """Sub menu 2.1.1.1 Screen
        Player selection filtered by name"""

        os.system("cls")
        print("="*80)
        print("===                          Menu 2.1.1.1 (JOUEURS)                          ===")
        print("="*80)
        print(f"=== Tournoi : {_tournament.name}")
        print("="*80)
        print("===  Sélection dans la liste, trié par nom :                                 ===")
        print("="*80)
        print("=== x.  : Revenir au menu précédent                                          ===")
        print("="*80)
        print()
        name = ''
        while not name.isalpha():
            user_input(_msg="Veuillez saisir le nom (même partiel) :")
            name = input()
        return name

    def show_menu_2_1_1_2(self, _tournament=''):
        """Sub menu 2.1.1.1 Screen
        Player selection filtered by firstname"""

        os.system("cls")
        print("="*80)
        print("===                           Menu 2.1.1.2 (JOUEURS)                         ===")
        print(f"=== Tournoi : {_tournament.name}")
        print("="*80)
        print("===  Sélection dans la liste, par prénom :                                   ===")
        print("="*80)
        print("=== x.  : Revenir au menu précédent                                          ===")
        print("="*80)
        print()
        firstname = ''
        while not firstname.isalpha():
            user_input(_msg="Veuillez saisir le prénom (même partiel) :")
            firstname = input()
        return firstname

    def show_menu_2_1_2(self, _tournament='', _selected_player_list=''):
        """Player selection sub menu"""

        os.system("cls")

        print("="*80)
        print("===                           Menu 2.1.2 (JOUEURS)                           ===")
        print("="*80)
        print(f"=== Tournoi : {_tournament.name}")
        print("="*80)
        choice_list = []
        print("=== {:<4}{:<10}{:<14}{:<12}{:<19}{:<10}".format("", "ID Unique",
                                                               "Nom",
                                                               "Prénom",
                                                               "Date de naissance",
                                                               "Score"))
        print()
        for _ in enumerate(_selected_player_list, start=1):
            print("=== {:<4}{:<10}{:<14}{:<12}{:<19}{:<10}".format(_[0], _[1].player_id,
                                                                   _[1].name,
                                                                   _[1].firstname,
                                                                   _[1].birthday,
                                                                   _[1].total_score))
            choice_list.append(str(_[0]))
        choice_list.append('x')
        print("="*80)
        print("=== x.  : Revenir au menu précédant                                          ===")
        print("="*80)
        print()
        print("  Choisissez le n° du joueur pour l'ajouter au tournoi :")
        print()
        choice = 'a'
        while choice not in choice_list:
            user_input(" Choix : ")
            choice = input()
        return choice

    def show_menu_2_2(self, _tournament='', _player_form='', _main_player_list='', _message=''):
        """New player registration
        to main players list"""

        player_id = _player_form.get('player_id', '')
        name = _player_form.get('name', '')
        firstname = _player_form.get('firstname', '')
        birthday = _player_form.get('birthday', '')

        os.system("cls")
        print("="*80)
        print("===                            Menu 2.2 (JOUEURS)                            ===")
        print("="*80)
        print(f"=== Tournoi :   {_tournament.name}")
        print("="*80)
        print("===             Enregistrement d'un nouveau joueur :  Formulaire             ===")
        print("="*80)
        if player_id != '':
            print(f"=== {'':<5}{'Identifiant unique  : ':<20}{player_id}")
        else:
            print(f"=== {'':<5}Identifiant unique  : ")
        if name != '':
            print(f"=== {'':<5}{'Nom                 : ':<20}{name}")
        else:
            print(f"=== {'':<5}Nom                 : ")
        if firstname != '':
            print(f"=== {'':<5}{'Prénom              : ':<20}{firstname}")
        else:
            print(f"=== {'':<5}Prénom              : ")
        if birthday != '':
            print(f"=== {'':<5}{'Date de naissance   : ':<20}{birthday}")
        else:
            print(f"=== {'':<5}Date de naissance   : ")
        print("="*80)
        print("===  x. : Retour au menu précédent                                           ===")
        print("="*80)
        print()
        # ---------------------------------------------------------------------------------------

        match _message:
            case 'player_id':
                player_id = ''
                while not (len(player_id) != 0) | (player_id in ('X', 'x')):
                    user_input(_msg="Identifiant unique (ex : AA12345): ")
                    player_id = input()
                if player_id in ('X', 'x'):
                    return player_id
                else:
                    return valid_id(player_id)

            case 'name':
                while not ((name != '') | (name in ('x', 'X'))):
                    user_input(_msg=" Nom du joueur : ")
                    name = input()
                return name

            case 'firstname':
                while not ((firstname != '') | (firstname in ('x', 'X'))):
                    user_input(_msg=" Prénom du joueur : ")
                    firstname = input()
                return firstname

            case 'birthday':
                birthday = '29/02/2023'
                while not (is_valid_date(birthday, date_format="%d/%m/%Y") | (birthday in ('x', 'X'))):
                    user_input(_msg="Date de naissance: ")
                    birthday = input()
                if birthday in ('x', 'X'):
                    birthday = 'x'
                return birthday

            case 'validate_data':
                choice = 'a'
                while choice not in ('O', 'o', 'N', 'n'):
                    user_input(_msg=" Souhaitez-vous valider les données  (O/n) ? : ")
                    choice = input()
                match choice:
                    case 'N' | 'n':
                        choice = 'n'
                    case 'O' | 'o':
                        choice = 'o'
                return choice

            case 'another_player':
                choice = 'a'
                while choice not in ('O', 'o', 'N', 'n'):
                    user_input(_msg=" Souhaitez-vous enregistrer un autre joueur  (O/n) ? : ")
                    choice = input()
                match choice:
                    case 'N' | 'n':
                        choice = 'n'
                    case 'O' | 'o':
                        choice = 'o'
                return choice

    def show_menu_2_3(self, _player_list='', _message=''):
        """Sub menu 2.3
        Tournament player screen display"""

        os.system("cls")
        print("="*80)
        print("===                2.3 : Affichage des joueurs sur ce tournoi                ===")
        print("="*80)
        print("==={:<29}{:>17}".format('', 'Joueurs inscrits'))
        print("=== {:<4}{:<10}{:<14}{:<12}{:<19}{:<10}".format("", "ID Unique",
                                                               "Nom",
                                                               "Prénom",
                                                               "Date de naissance",
                                                               "Score"))
        print()
        if not _player_list == '':
            sorted_list = sorted(_player_list, key=lambda player: (player.name, player.birthday))
            for _ in enumerate(sorted_list, start=1):
                print("=== {:<4}{:<10}{:<14}{:<12}{:<19}{:<10}".format(_[0],
                                                                       _[1].player_id,
                                                                       _[1].name,
                                                                       _[1].firstname,
                                                                       _[1].birthday,
                                                                       _[1].total_score))
        print("="*80)
        print("===   x. : Retour au menu précédent                                ===")
        print("="*80)
        print()
        if _message == "player_list vide":
            print(_message)
        choice = 'a'
        while choice not in ('X', 'x'):
            user_input(_msg=" Choix : ")
            choice = input()
        choice = True
        return choice

    def show_menu_3(self, _tournament='', _message=''):
        """    Root Round management Screen
            Launch Closure and Scores updates"""

        os.system("cls")
        print("="*80)
        print("===                               Menu 3 (JEU)                               ===")
        print("="*80)
        print(f"=== Tournoi     : {_tournament.name:<5}")
        print(f"=== Lieu        : {_tournament.location}")
        print(f"=== Description : {_tournament.description}")
        print(f"=== Début       : {_tournament.begin_date:<3}  Fin :{_tournament.end_date:<3}")
        print(f"=== Nombre de tours : {_tournament.round_number}          ")
        print(f"=== Avancement de la partie : {len(_tournament.round_list)} / {_tournament.round_number}")
        print("="*80)
        print("==={:<29}{:>17}".format('', 'Joueurs inscrits'))
        print("-"*80)
        print("=== {:<4}{:<10}{:<14}{:<12}{:<19}{:<10}".format("Rang", "ID Unique",
                                                               "Nom",
                                                               "Prénom",
                                                               "Date de naissance",
                                                               "Score"))
        print()
        if not _tournament.player_list == '':
            # Display sorted by score

            sorted_player_list = sorted(_tournament.player_list,
                                        key=lambda player: (player.total_score, player.name, player.birthday))
            score = sorted_player_list[1].total_score
            ranking = 1
            for _ in enumerate(sorted_player_list, start=1):
                if _[1].total_score != score:
                    ranking = _[0]
                    score = _[1].total_score
                print("=== {:<4}{:<10}{:<14}{:<12}{:<19}{:<10}".format(ranking,
                                                                       _[1].player_id,
                                                                       _[1].name,
                                                                       _[1].firstname,
                                                                       _[1].birthday,
                                                                       _[1].total_score))
        print("="*80)
        print("="*80)
        print(f"=== Message : {_message}")
        print("="*80)
        print("=== 1. Lancer un round                                                       ===")
        print("=== 2. Clore le round et Saisir les scores                                   ===")
        print("="*80)
        print("=== 3. Afficher du round actuel                                              ===")
        print("="*80)
        print("===  x. : Retour au menu précédent                                           ===")
        print("="*80)
        choice = 'a'
        print()
        while choice not in ('1', '2', '3', 'x', 'X'):
            user_input(" Choix : ")
            choice = input()
            if choice == 'X':
                return 'X'
        return choice

    def show_menu_3_1(self, _tournament='', _message='', _player=''):
        """ Display Menu 3.1
        Tournament Game informations """

        os.system("cls")
        print("="*80)
        print("===                              Menu 3.1 (JEU)                              ===")
        print("="*80)
        print(f"=== Tournoi     : {_tournament.name:<5}")
        print(f"=== Lieu        : {_tournament.location}")
        print(f"=== Description : {_tournament.description}")
        print(f"=== Début       : {_tournament.begin_date:<3}  Fin :{_tournament.end_date:<3}")
        print(f"=== Nombre de tours : {_tournament.round_number}          ")
        print(f"=== Avancement de la partie : {len(_tournament.round_list)} / {_tournament.round_number}")
        print("-"*80)
        print("==={:<29}{:>17}".format('', 'Joueurs inscrits'))
        print("-"*80)
        if not _tournament.player_list == '':
            print("=== {:<4}{:<10}{:<14}{:<12}{:<19}{:<10}".format("Rang",
                                                                   "ID Unique",
                                                                   "Nom",
                                                                   "Prénom",
                                                                   "Date de naissance",
                                                                   "Score"))
            print("=== ")
            # Display sorted by score
            sorted_player_list = sorted(_tournament.player_list,
                                        key=lambda player:
                                        (player.total_score, player.name, player.birthday))
            score = sorted_player_list[1].total_score
            ranking = 1
            for _ in enumerate(sorted_player_list, start=1):
                if _[1].total_score != score:
                    ranking = _[0]
                    score = _[1].total_score
                print("=== {:<4}{:<10}{:<14}{:<12}{:<19}{:<10}".format(ranking,
                                                                       _[1].player_id,
                                                                       _[1].name,
                                                                       _[1].firstname,
                                                                       _[1].birthday,
                                                                       _[1].total_score))
        print("-"*80)
        print("==={:<33}".format(_tournament.round_list[-1].name))
        print("-"*80)
        print("=== {:<10}{:<10} contre  {:<12}{:<7} / {:<7}".format("Match n°",
                                                                    "Joueur A",
                                                                    "Joueur B",
                                                                    "Score A",
                                                                    "Score B"))
        for _ in enumerate(_tournament.round_list[-1].match_list, start=1):
            current_match = _[1]
            print("=== {:<10}{:<10}         {:<12}{:<7} / {:<7}".format(_[0],
                                                                        current_match.player_a,
                                                                        current_match.player_b,
                                                                        current_match.score_a,
                                                                        current_match.score_b))
        print("="*80)
        print(f"Message : {_message}")
        print("-"*80)
        print()
        print("="*80)
        print("===   x. : Retour au menu précédent                                          ===")
        choice = 'a'
        print("="*80)
        print()
        while choice not in ('x', 'X'):
            user_input(_msg=" Choix : ")
            choice = input()

        return choice

    def show_menu_3_2(self, _tournament='', _message='', _player=''):
        """ Display sub_menu for round close
                and match score set         """

        os.system("cls")
        if _tournament == "":
            choice = 'x'
            return choice
        print("="*80)
        print("----------------     Menu 3.2       ----------------------")
        print("="*80)
        print(f"=== Tournoi     : {_tournament.name:<5}")
        print(f" Nombre de tours : {_tournament.round_number}          ")
        print(f" Avancement de la partie : {len(_tournament.round_list)} / {_tournament.round_number}")
        print("="*80)
        print("="*80)
        print("==={:<29}{:>17}".format('', 'Joueurs inscrits'))
        print("-"*80)
        print("=== {:<4}{:<10}{:<14}{:<12}{:<19}{:<10}".format("", "ID Unique",
                                                               "Nom",
                                                               "Prénom",
                                                               "Date de naissance",
                                                               "Score"))
        print()
        # Display sorted by score
        sorted_player_list = sorted(_tournament.player_list,
                                    key=lambda player:
                                    player.total_score,
                                    reverse=True)
        score = sorted_player_list[1].total_score
        ranking = 1
        for _ in enumerate(sorted_player_list, start=1):
            if _[1].total_score != score:
                ranking = _[0]
                score = _[1].total_score
            print("=== {:<4}{:<10}{:<14}{:<12}{:<19}{:<10}".format(ranking,
                                                                   _[1].player_id,
                                                                   _[1].name,
                                                                   _[1].firstname,
                                                                   _[1].birthday,
                                                                   _[1].total_score))
        print("==={:<29}{:>17}".format('', 'Joueurs inscrits'))
        print("="*80)
        print("==={:<33}{:<33}".format('', _tournament.round_list[-1].name))
        print("-"*80)
        print(" Liste des matches : ")
        print()
        if _tournament.round_list[-1].name != '':
            current_round = _tournament.round_list[-1]
            for game in (enumerate(current_round.match_list, start=1)):
                index = 0
                while _tournament.player_list[index].player_id != game[1].player_a:
                    index += 1
                _player_A = _tournament.player_list[index]

                index = 0
                while _tournament.player_list[index].player_id != game[1].player_b:
                    index += 1
                _player_B = _tournament.player_list[index]

                print("=== {:<8}{:<12}{:<12}{:<12}{:<19}{:<10}".format("Match",
                                                                       "ID Unique",
                                                                       "Nom",
                                                                       "Prénom",
                                                                       "Date de naissance",
                                                                       "Score"))
                print("===   {:<6}{:<12}{:<12}{:<12}{:<19}{:<10}".format(game[0],
                                                                         _player_A.player_id,
                                                                         _player_A.name,
                                                                         _player_A.firstname,
                                                                         _player_A.birthday,
                                                                         game[1].score_a))
                print("===   {:<6}{:<12}{:<12}{:<12}{:<19}{:<10}".format('',
                                                                         _player_B.player_id,
                                                                         _player_B.name,
                                                                         _player_B.firstname,
                                                                         _player_B.birthday,
                                                                         game[1].score_b))
                print("="*80)
                # print(f" Match {a_0} Joueur_A {a_1:<3}/{a_2:<4} {a_3:<7} contre {b_1:<3}/{b_2:<4} {b_3}")
        print("===  Commandes clavier :")
        print("-"*80)
        print("=== x. : Revenir au menu                                                     ===")
        print("="*80)
        choice = 'a'
        print()

        match _message:
            case "Êtes-vous sûr de vouloir clore ce Round ? (O/n) ":
                # Close the round ?
                print(_message)
                print()
                while choice not in ('O', 'o', 'N', 'n', 'X', 'x'):
                    user_input(_msg=" Choix : ")
                    choice = input()
                match choice:
                    case ('O', 'o'):
                        choice = 'o'
                    case ('N', 'n'):
                        choice = 'n'
                    case ('X', 'x'):
                        choice = 'x'
                return choice

            case "Saisie du score":
                # We have to set score to every round player
                print()
                print(f"Veuillez saisir le score du joueur ID: {_player.player_id}")
                print()
                print(f" Nom: {_player.name} Prénom: {_player.firstname} ")
                score = 'a'
                print()
                while score not in ('G', 'g', 'N', 'n', 'P', 'p', 'X', 'x'):
                    user_input(_msg=" Score G(agné) | N(ul) | P(erdu) :  ")
                    score = input()
                return score

            case "Ce round est clos":
                # Round is closed !
                print(f"*** {_message} ")
                while choice != ('3', 'X' | 'x'):
                    user_input(" Choix : ")
                    choice = input()
                match choice:
                    case ('X', 'x'):
                        choice = 'x'
                return choice

            case "La partie est terminée !":
                # All round are closed ... Game Over !
                print()
                print("La partie est terminée ! ")
                print()
                while score not in ('3', 'X', 'x'):
                    user_input(_msg=" Choix :  ")
                    choice = input()
                    match choice:
                        case 'X', 'x':
                            choice = 'x'
                return choice

            case _:
                choice = 'a'
                while choice not in ('X', 'x'):
                    user_input(_msg=" Choix :  ")
                    choice = input()
                    match choice:
                        case 'X', 'x':
                            choice = 'x'
                return choice

    def show_menu_3_3(self, _tournament='', _message='', _player=''):
        """ Display sub_menu for round close
                and match score set         """

        os.system("cls")
        choice = 'a'
        if _tournament.status == "ended":
            message = "Le tournoi est clos !"
        elif _tournament.round_list[-1].end_time == "Round en cours de jeu !":
            message = f"Le {_tournament.round_list[-1].name} est en cours !"
        else:
            message = f"Le {_tournament.round_list[-1].name} est achevé"

        print("="*80)
        print("===                       Menu 3.3 : (ROUND Stats.)                          ===")
        print("="*80)
        print(f"=== Tournoi     : {_tournament.name:<5}")
        print(f"=== Nombre de tours : {_tournament.round_number}          ")
        print(f"=== Avancement de la partie : {message}")
        print("="*80)
        print("==={:<29}{:>17}".format('', 'Joueurs inscrits'))
        print("-"*80)
        if len(_tournament.round_list) == 0:
            print("          Aucun round n'est programmé")
        else:
            print()
            if _tournament.round_list[-1].name != '':
                current_round = _tournament.round_list[-1]
                print("=== {:<8}{:<12}{:<12}{:<12}{:<19}{:<10}".format("Match",
                                                                       "ID Unique",
                                                                       "Nom",
                                                                       "Prénom",
                                                                       "Date de naissance",
                                                                       "Score"))
                for game in (enumerate(current_round.match_list, start=1)):
                    index = 0
                    while _tournament.player_list[index].player_id != game[1].player_a:
                        index += 1
                    _player_A = _tournament.player_list[index]

                    index = 0
                    while _tournament.player_list[index].player_id != game[1].player_b:
                        index += 1
                    _player_B = _tournament.player_list[index]

                    print("===   {:<6}{:<12}{:<12}{:<12}{:<19}{:<10}".format(game[0],
                                                                             _player_A.player_id,
                                                                             _player_A.name,
                                                                             _player_A.firstname,
                                                                             _player_A.birthday,
                                                                             game[1].score_a))
                    print("===   {:<6}{:<12}{:<12}{:<12}{:<19}{:<10}".format('',
                                                                             _player_B.player_id,
                                                                             _player_B.name,
                                                                             _player_B.firstname,
                                                                             _player_B.birthday,
                                                                             game[1].score_b))
                    print("-"*80)
        print("="*80)
        print("=== x. Retour au menu précédent                                              ===")
        print("="*80)
        print()
        while choice not in ('X', 'x'):
            user_input(_msg=" Choix : ")
            choice = input()
        return 'x'

    def show_menu_4(self):
        """Reports display"""

        os.system("cls")
        print("="*80)
        print("===                            Menu 4 (RAPPORTS)                             ===")
        print("="*80)
        print("=== 1.   Affichage Liste des joueurs du tournoi                              ===")
        print("=== 2.   Affichage des données actualisées du tournoi                        ===")
        print("=== 3.   Affichage des résultats                                             ===")
        print("="*80)
        print("=== x.   Retour au menu précédent                                            ===")
        print("="*80)
        choice = 'a'
        print()
        while choice not in ('1', '2', '3', 'x'):
            user_input(" Choix : ")
            choice = input()
        return choice

    def show_menu_4_1(self, _tournament='', _main_player_list=''):
        """    Round Players List """

        os.system("cls")
        print("="*80)
        print("===                            Menu 4.1 (RAPPORTS)                           ===")
        print("="*80)
        print("===            Liste des joueurs Inscrits sur ce tournoi                     ===")
        print("="*80)
        print(f"=== Tournoi     : {_tournament.name:<5}")
        print(f"=== Lieu        : {_tournament.location}")
        print(f"=== Description : {_tournament.description}")
        print(f"=== Début       : {_tournament.begin_date:<3}  Fin :{_tournament.end_date:<3}")
        print(f"=== Nombre de tours : {_tournament.round_number}          ")
        print(f"=== Avancement de la partie : {len(_tournament.round_list)} / {_tournament.round_number}")
        print("="*80)
        print("==={:<29}{:>17}".format('', 'Joueurs inscrits'))
        print("-"*80)
        print("=== {:<4}{:<10}{:<14}{:<12}{:<19}".format("",
                                                         "ID Unique",
                                                         "Nom",
                                                         "Prénom",
                                                         "Date de naissance"))
        print()
        if not _tournament.player_list == '':
            for _ in enumerate(_tournament.player_list, start=1):
                print("=== {:<4}{:<10}{:<14}{:<12}{:<19}".format(_[0],
                                                                 _[1].player_id,
                                                                 _[1].name,
                                                                 _[1].firstname,
                                                                 _[1].birthday))
        print("="*80)
        print("=== x. Retour au menu précédent                                              ===")
        print("="*80)
        choice = 'a'
        print()
        while choice not in ('X', 'x'):
            user_input(" Choix : ")
            choice = input()
        return choice

    def show_menu_4_2(self, _tournament=''):
        """    Tournament Display
        Displays Rounds results
        Permit to follow tournament """

        os.system("cls")
        print("="*80)
        print("===                            Menu 4.2 (RAPPORTS)                           ===")
        print("="*80)
        print("===                            Résultats des Rounds                          ===")
        print("="*80)
        print(f"=== Tournoi     : {_tournament.name:<5}")
        print(f"=== Lieu        : {_tournament.location}")
        print(f"=== Description : {_tournament.description}")
        print(f"=== Début       : {_tournament.begin_date:<3}  Fin :{_tournament.end_date:<3}")
        print(f"=== Nombre de tours : {_tournament.round_number}          ")
        print(f"=== Avancement de la partie : {len(_tournament.round_list)} / {_tournament.round_number}")
        print("="*80)
        print("==={:<29}{:>17}".format('', 'Joueurs inscrits'))
        print("-"*80)
        if not _tournament.player_list == '':
            print("=== {:<4}{:<10}{:<14}{:<12}{:<19}".format("",
                                                             "ID Unique",
                                                             "Nom",
                                                             "Prénom",
                                                             "Date de naissance"))
            print()
            for _ in enumerate(_tournament.player_list, start=1):
                print("=== {:<4}{:<10}{:<14}{:<12}{:<19}".format(_[0],
                                                                 _[1].player_id,
                                                                 _[1].name,
                                                                 _[1].firstname,
                                                                 _[1].birthday))
        print("="*80)
        # enumerate round_list
        for _ in enumerate(_tournament.round_list, start=1):
            current_round = _[1]
            print("==={:<33}{:<10}".format('', current_round.name))
            print("-"*80)
            print("=== {:<10}{:<10} contre  {:<12}{:<7} / {:<7}".format("Match n°",
                                                                        "Joueur A",
                                                                        "Joueur B",
                                                                        "Score A",
                                                                        "Score B"))
            print("===")
            # enumerate match
            for _ in enumerate(current_round.match_list, start=1):
                current_match = _[1]
                print("=== {:<10}{:<10}         {:<12}{:<7} / {:<7}".format(_[0],
                                                                            current_match.player_a,
                                                                            current_match.player_b,
                                                                            current_match.score_a,
                                                                            current_match.score_b))
            print("-"*80)
        print("=== x. Retour au menu précédent                                              ===")
        print("="*80)
        choice = 'a'
        print()
        while choice not in ('X', 'x'):
            user_input(" Choix : ")
            choice = input()
        return choice

    def show_menu_4_3(self, _tournament=''):
        """    Displayed Players Scores """

        displayed_score = 'Score cumulé temporaire'
        if len(_tournament.round_list) == _tournament.round_number:
            if _tournament.round_list[-1].ended:
                displayed_score = "Score Total Final"
        else:
            displayed_score = "Score cumulé Temporaire"

        # print(f"Tournament : {tournament.round_list}")
        choice = 'a'
        os.system("cls")
        print("="*90)
        print("===                                 Menu 4.3 (RAPPORTS)                                ===")
        print("="*90)
        print("===                                      Classement                                    ===")
        print("="*90)
        print(f"=== Tournoi                 : {_tournament.name:<5}")
        print(f"=== Lieu                    : {_tournament.location}")
        print(f"=== Description             : {_tournament.description}")
        print(f"=== Début                   : {_tournament.begin_date:<3}  Fin :{_tournament.end_date:<3}")
        print(f"=== Nombre de tours         : {_tournament.round_number}          ")
        print(f"=== Avancement de la partie : {len(_tournament.round_list)} / {_tournament.round_number}")
        print("-"*90)
        if len(_tournament.round_list) != 0:
            if (len(_tournament.round_list) == _tournament.round_number) & _tournament.round_list[-1].ended:
                print("===                           La partie est terminée....... ")
            else:
                print("===                           La partie est en cours...")
        else:
            print("===                           La partie n'est pas commencée.....")
        print("="*90)
        print("==={:<28}{:<56}===".format('', 'Classement des joueurs'))
        print("-"*90)
        if (not _tournament.player_list == '') & (not len(_tournament.round_list) == 0):
            print("=== {:<6}{:<12}{:<14}{:<12}{:<19}{:<10}".format("Rang",
                                                                   "ID Unique",
                                                                   "Nom",
                                                                   "Prénom",
                                                                   "Date de naissance",
                                                                   str(displayed_score)))
            print()
            # cumulative_total(tournament)
            sorted_player_list = sorted(_tournament.player_list,
                                        key=lambda player:
                                        player.total_score,
                                        reverse=True)

            score = sorted_player_list[1].total_score
            ranking = 1
            for _ in enumerate(sorted_player_list, start=1):

                if _[1].total_score != score:
                    ranking = _[0]
                    score = _[1].total_score
                print("=== {:<6}{:<12}{:<14}{:<12}{:<19}{:<10}".format(str(ranking),
                                                                       _[1].player_id,
                                                                       _[1].name,
                                                                       _[1].firstname,
                                                                       _[1].birthday,
                                                                       _[1].total_score))
        print("="*90)
        print("===     Commandes :")
        print("-"*90)
        print("=== x. Retour au menu précédent                                                        ===")
        print("="*90)
        choice = 'a'

        print()
        while choice not in ('X', 'x'):
            user_input(" Choix : ")
            choice = input()
        return choice
