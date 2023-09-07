# Projet : Développez un programme logiciel en Python

**Description** : Programme de gestion de tournoi de jeu d'échecs en langage Python

**Objectifs** : Introduction à la programmation orientée objet, ce programme utilise l'approche de modélisation architecturale Model-View-Controller.

1.**Déploiement** :

- Télécharger le fichier **Projet4-Developpez_un_programme_logiciel_en_Python-main.zip**
- Décompresser le zip dans un dossier
- Depuis le terminal dans le dossier, recomposer l'environnement virtuel à l'aide de la commande: **pip install -r requirements.txt**

2.**Lancement du programme**

Le lancement du programme se fait par la commande :  **python play_tournament.py**

3.**Rapport Flake8** :

Génération du rapport Flake8 :
    La section **flake8** dans le fichier tox.ini indique les directives pour Flake8, dont le périmètre de tests, en excluant le dossier .env
Lancer la commande : **flake8 --format=html --htmldir=flake8-rapport**
Vous pouvez lire le résultat en ouvrant le fichier flake8-rapport\\**index.html** dans votre navigateur favori.

4.**Comment utiliser le programme**

L'interface utilisateur est constituée d'écrans sur lesquels une ligne intitulée message apporte une aide à l'utilisateur.
Afin de passer d'un écran à l'autre, il est nécessaire de sélectionner la rubrique en validant le n° à gauche de la ligne correspondante (_ex: je souhaite sélectionner un tournoi ou en inscrire un nouveau ?
 -   je sélectionne la rubrique **TOURNOI : Sélection ou Création** en tapant '**1**' suivi de la touche Entrer_)
Tout le déroulement de ce programme est basé sur ce mode de fonctionnement.

3 rubriques principales composent ce programme:

- menu **'1'** : permet d'entrer dans la sélection ou l'inscription des **tournois**
- menu **'2'** : permet d'entrer dans la sélection ou l'inscription des **joueurs**
- menu **'3'** : permet d'entrer dans la gestion des manches ou **Rounds** du tournoi
- menu **'4'** : propose un certain nombre de rapports permettant le suivi du tournoi
  
- Le programme se base sur une liste de joueurs déjà établie, mais permet de rajouter des joueurs. 

- De la même façon, il se base sur une liste de tournois enregistrés, mais permet également d'en inscrire des nouveaux.
- Lorsque le programme est lancé, il n'est plus possible d'ajouter des joueurs.

La sauvegarde des données étant basée sur un format JSON, il est possible de reprendre le suivi d'un tournoi en relançant le programme, si besoin était.
Il sera alors nécessaire de sélectionner de nouveau le tournoi en cours afin de repositionner les informations au plus près du dernier arrêt.

Enfin, la touche 'Q' ou 'q' sur le menu principal vous permet de fermer le programme.
