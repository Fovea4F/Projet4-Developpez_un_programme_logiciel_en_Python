""" User interactions """

import os
from tools import user_input


class View_main:
    """View: manage every interface with human
    Manages Input and Output
    """

    def show_main_menu(self, _tournament_name='', _message=''):
        """Main menu User Interface"""

        choice = 'a'
        os.system("cls")
        print("="*80)
        print("===                         Menu principal                         ===")
        print("="*80)
        print(f"=== Tournoi : {_tournament_name} ")
        print("="*80)
        print("===              Gestion d'un tournoi de Jeu d'échecs              ===")
        print("="*80)
        print("===  1.   TOURNOI : Sélection ou Création                          ===")
        print("===  2.   JOUEURS : Sélection ou Enregistrement                    ===")
        print("===  3.   JEU :     Lancement du tournoi / rounds                  ===")
        print("="*80)
        print("===  4.   Rapports                                                 ===")
        print("="*80)
        print("===  x.   Quitter l'application                                    ===")
        print("="*80)
        print()
        if _message != '':
            print(f" Message : {_message} ")
        print()
        match _message:
            case " Vous souhaitez quitter le programme ? O/n ":
                print()
                choice = 'a'
                while choice not in ('O', 'o', 'N', 'n'):
                    user_input(" Choix  (O/n) : ")
                    choice = input()
                if choice in ('N', 'n'):
                    choice = 'n'
                else:
                    choice = 'o'
                return choice

            case _:
                while choice not in ('1', '2', '3', '4', 'x'):
                    user_input(_msg=" Choix : ")
                    choice = input()
                return choice
