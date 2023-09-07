""" Utilities used in Controller """

import re
import random
import json
import string
from model.chess_round import Round
from model.chess_match import Match
from model.chess_player import Player
from model.chess_tournament import Tournament


def get_random_id(length):
    """create an alphanumeric random length alpha_lowercase word"""
    # A retirer

    random_id = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return random_id


def round_and_match_create(_current_tournament):
    """Add a new round to tournament round list
    if possible
    Also create Match list
    return message
    """
    # Round name calculation
    if _current_tournament.current_round_number < _current_tournament.round_number:
        _current_tournament.current_round_number += 1
        round_name = "ROUND " +\
            str(_current_tournament.current_round_number)

        current_round = Round()
        match_list = []
        round_player_list = []

        # ----------------------------------------------------------
        # Create simplified players list (only player_id)
        # ----------------------------------------------------------
        for _player in enumerate(_current_tournament.player_list):
            round_player_list.append(_player[1].player_id)
        # ----------------------------------------------------------

        # ----------------------------------------------------------
        # If first round, random match player selection,
        # else by sorted score in preference, 
        if len(round_player_list) % 2 != 0:
            message = "Impossible de créer les matches, nombre impair de joueurs"
            return message
        elif _current_tournament.current_round_number == 1:
            # 1st tour : Random
            while len(round_player_list) > 0:
                tmp_match = Match('', '')
                random.shuffle(round_player_list)
                tmp_match.player_a = round_player_list[0]
                tmp_match.player_b = round_player_list[1]
                tmp_match.score_a = '-'
                tmp_match.score_b = '-'
                match_list.append(tmp_match)
                _current_tournament.match_couple.append((tmp_match.player_a,
                                                        tmp_match.player_b))
                _current_tournament.match_couple.append((tmp_match.player_b,
                                                        tmp_match.player_a))
                round_player_list.pop(1)
                round_player_list.pop(0)

        else:
            # For other rounds, selected by score and match history
            round_player_list = []
            sorted_round_player_list = sorted(_current_tournament.player_list,
                                              key=lambda player:
                                              player.total_score,
                                              reverse=True)
            for _player in enumerate(sorted_round_player_list):
                round_player_list.append(_player[1].player_id)

            while len(round_player_list) > 0:
                # Verify if couple not present in tournament history
                index = 1
                while index < len(round_player_list):
                    tmp_match = Match('', '')
                    test_couple = (round_player_list[0], round_player_list[index])
                    if test_couple not in _current_tournament.match_couple:
                        tmp_match.player_a = round_player_list[0]
                        tmp_match.player_b = round_player_list[index]
                        tmp_match.score_a = '-'
                        tmp_match.score_b = '-'
                        round_player_list.pop(index)
                        round_player_list.pop(0)
                        _current_tournament.match_couple.append((tmp_match.player_a,
                                                                tmp_match.player_b))
                        _current_tournament.match_couple.append((tmp_match.player_b,
                                                                tmp_match.player_a))
                        match_list.append(tmp_match)
                        index = 1
                    else:
                        index += 1
                if index == len(round_player_list):
                    index = 1
                    tmp_match.player_a = round_player_list[0]
                    tmp_match.player_b = round_player_list[index]
                    tmp_match.score_a = '-'
                    tmp_match.score_b = '-'
                    round_player_list.pop(index)
                    round_player_list.pop(0)
                    _current_tournament.match_couple.append((tmp_match.player_a,
                                                            tmp_match.player_b))
                    _current_tournament.match_couple.append((tmp_match.player_b,
                                                            tmp_match.player_a))
                    match_list.append(tmp_match)

        current_round.add(name=round_name, match_list=match_list)
        _current_tournament.round_add(current_round)
        message = "Le round est commencé."
        _current_tournament.status = "started"
        return message

    else:
        if _current_tournament.current_round_number == _current_tournament.round_number:
            message = "Le nombre de round dans la partie est atteint"
            return message

    def create_match_list(_current_tournament=''):
        """Permit to generate a match list using players registered in tournament

        Args:
            _current_tournament (str, optional): Tournament class instance as reference. Defaults to ''.

        Returns:
            List: List of matches created for the round
        """

        return match_list


def round_score_update(_current_tournament):
    """To calculate every tournament player total score
    add round score to tournament player score
    Value attached to player
    Condition : Round ended and score not yet updated to global player score
    """

    result = -1
    if _current_tournament.round_list[-1].ended:
        if not _current_tournament.round_list[-1].reported_score:
            for _match_enum in enumerate(_current_tournament.round_list[-1].match_list):
                _match = _match_enum[1]

                player_a_id = _match.player_a
                player_b_id = _match.player_b
                score_a = _match.score_a
                score_b = _match.score_b
                index_a = 0
                index_b = 0
                while _current_tournament.player_list[index_a].player_id != player_a_id:
                    if index_a < len(_current_tournament.player_list):
                        index_a += 1

                while _current_tournament.player_list[index_b].player_id != player_b_id:
                    if index_a < len(_current_tournament.player_list):
                        index_b += 1

                _current_tournament.player_list[index_a].total_score += score_a
                _current_tournament.player_list[index_b].total_score += score_b
            _current_tournament.round_list[-1].reported_score = True
            result = 0
        else:
            result = 1

    return result


def conform_id(_id):
    """ Verify if passed id respect pattern"""
    # Pattern 2 Capital letters followed by 5 digits
    # A retirer

    pattern = r'^[A-Z]{2}[0-9]{5}$'
    valid_id = False
    if re.match(pattern, _id) is not None:
        valid_id = True
    return valid_id


def find_player_from_json(key='', value='', file=''):
    """Return player_data for a player name or firstname passed in argument
     -  key: selector (firstname or name)
     -  value: case insensitive beginning or whole word to find """

    list_out = []
    with open(file, 'r') as json_file:
        data_load = json.load(json_file)

    value = value.casefold()
    for _ in enumerate(data_load):
        value_read = _[1][key].casefold()
        if value_read.startswith(value):
            player_instance = Player()
            player_instance.player_id = _[1]['player_id']
            player_instance.name = _[1]['name']
            player_instance.firstname = _[1]['firstname']
            player_instance.birthday = _[1]['birthday']
            list_out.append(player_instance)
    return list_out


def read_from_json(file=''):
    """Return instances list from json formatted file"""

    class Container:
        """Generic class"""

    with open(file, 'r', encoding="UTF-8") as json_file:
        loaded_data = json.load(json_file)
        data_out = []
        if len(loaded_data) != 0:
            instance_keys = loaded_data[0].keys()
            # print(instance_keys)
            if len(instance_keys) != 0:
                attribute_list = list(instance_keys)
                # print(f"Liste des attributs : {attribute_list}")

                for data in loaded_data:
                    instance = Container()
                    for attrib in range(len(attribute_list)):
                        # print(f"Attribut : {attribute_list[attrib]}")
                        # print(f"Data : {data[attribute_list[attrib]]}")
                        setattr(instance, attribute_list[attrib], data[attribute_list[attrib]])
                    data_out.append(instance)
    return data_out


def write_to_json(object='', file=''):
    """ Write serialized object to JSON file
        Return instances list from json formatted file"""
    # A retirer
    class Container:
        """Generic Class"""

    with open(file, 'w', encoding="UTF-8") as json_file:
        loaded_data = json.load(json_file)
        data_out = []
        if len(loaded_data) != 0:
            instance_keys = loaded_data[0].keys()
            # print(instance_keys)
            if len(instance_keys) != 0:
                attribute_list = list(instance_keys)
                # print(f"Liste des attributs : {attribute_list}")

                for data in loaded_data:
                    instance = Container()
                    for attrib in range(len(attribute_list)):
                        # print(f"Attribut : {attribute_list[attrib]}")
                        # print(f"Data : {data[attribute_list[attrib]]}")
                        setattr(instance, attribute_list[attrib], data[attribute_list[attrib]])
                    data_out.append(instance)
    return data_out

    # with open(file, 'w') as json_file:
    #     json.dump(object, json_file, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)


def update_json_with_player(player='', file=''):
    """Update JSON file :
    -   get player instance and update file with data.
    if player doesn't exist yet, add it, else update values"""

    with open(file, 'r') as json_file:
        loaded_data = json.load(json_file)
        player_list = []
        for _ in enumerate(loaded_data):
            load_player = Player()
            load_player.player_id = _[1]['player_id']
            load_player.name = _[1]['name']
            load_player.firstname = _[1]['firstname']
            load_player.birthday = _[1]['birthday']
            if hasattr(_[1], 'total_score'):
                load_player.total_score = _[1]['total_score']
            player_list.append(load_player)
        if player != '':
            player_to_backup = Player()
            for _ in enumerate(player_list):
                if _[1].player_id == player.player_id:
                    player_to_backup.player_id = player.player_id
                    player_to_backup.name = player.name
                    player_to_backup.firstname = player.firstname
                    player_to_backup.birthday = player.birthday
                    player_list.pop(_[1])
                    player_list.append(player_to_backup)
                    break
                else:
                    player_to_backup.player_id = player.player_id
                    player_to_backup.name = player.name
                    player_to_backup.firstname = player.firstname
                    player_to_backup.birthday = player.birthday
                    player_list.append(player_to_backup)
                    break

    data_to_save = [{"player_id": player.player_id,
                     "name": player.name,
                     "firstname": player.firstname,
                     "birthday": player.birthday}
                    for player in player_list]
    with open(file, 'w') as json_file:
        json.dump(data_to_save, json_file, indent=4)


def save_data_to_json_file(objet='', file=''):
    """ backup data to file in JSON format"""

    # IN data is a class instance with multiple types of data.

    # serialized_data = json.dump(object, default=lambda o: o.__dict__, ensure_ascii=False, indent=4)
    with open(file, 'w') as json_file:
        json.dump(objet, json_file, ensure_ascii=False, indent=4)


def get_data_from_json_file(file=''):
    """ get data from file in JSON format to a list"""

    # IN data is a json file
    # out is a list of un serialized JSON data

    with open(file, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def serialize_tournament_list(object=""):
    """IN : Tournament list
    return serialized Tournament list in dictionary"""

    if len(object) > 0:
        serialized_data = []
        for tournament in enumerate(object):
            serialized_tournament = serialize_tournament(object=tournament[1])
            serialized_data.append(serialized_tournament)
    return serialized_data


def serialize_tournament(object=''):
    """IN: Tournament instance
    return serialized Tournament instance in a dictionary"""

    if (object == '') | (not isinstance(object, Tournament)):
        return None
    else:
        serialized = {}
        serialized["name"] = object.name
        serialized["location"] = object.location
        serialized["begin_date"] = object.begin_date
        serialized["end_date"] = object.end_date
        serialized["description"] = object.description
        serialized["current_round_number"] = object.current_round_number
        serialized["round_number"] = object.round_number
        serialized["status"] = object.status
        serialized["match_couple"] = object.match_couple
        if len(object.round_list) == 0:
            serialized["round_list"] = []
        else:
            serialized["round_list"] = []
            for round in enumerate(object.round_list, start=1):
                serialized_round = {}
                round_name = "ROUND_" + str(round[0])
                serialized_round["name"] = round_name
                serialized_round["start_time"] = round[1].start_time
                serialized_round["end_time"] = round[1].end_time
                serialized_round["reported_score"] = round[1].reported_score
                serialized_round["ended"] = round[1].ended
                match_list = []
                for match in round[1].match_list:
                    serialized_match = ([match.player_a, match.score_a], [match.player_b, match.score_b])
                    match_list.append(serialized_match)
                serialized_round["match_list"] = match_list
                serialized["round_list"].append(serialized_round)
        if len(object.player_list) == 0:
            serialized["player_list"] = []
        else:
            serialized_player_list = []
            for player in object.player_list:
                serialized_player = {}
                serialized_player["player_id"] = player.player_id
                serialized_player["name"] = player.name
                serialized_player["firstname"] = player.firstname
                serialized_player["birthday"] = player.birthday
                serialized_player["total_score"] = player.total_score
                serialized_player_list.append(serialized_player)
            serialized["player_list"] = serialized_player_list
    return serialized


def deserialize_tournament(file=''):
    """ the given file will return a list file of tournaments to
    a list of Tournament class instances"""

    deserialized_file = get_data_from_json_file(file=file)
    tournament_list = []
    for json_tournament in enumerate(deserialized_file):
        tournament = Tournament()
        match_couple = []
        round_list = []
        player_list = []
        tournament.name = json_tournament[1]["name"]
        tournament.location = json_tournament[1]["location"]
        tournament.begin_date = json_tournament[1]["begin_date"]
        tournament.end_date = json_tournament[1]["end_date"]
        tournament.description = json_tournament[1]["description"]
        tournament.status = json_tournament[1]["status"]
        tournament.current_round_number = json_tournament[1]["current_round_number"]
        tournament.round_number = json_tournament[1]["round_number"]
        for couple in enumerate(json_tournament[1]["match_couple"]):
            match_couple.append(couple[1])
        tournament.match_couple = match_couple
        for json_round in enumerate(json_tournament[1]["round_list"]):
            round_instance = Round()
            round_instance.name = json_round[1]["name"]
            round_instance.start_time = json_round[1]["start_time"]
            round_instance.end_time = json_round[1]["end_time"]
            round_instance.reported_score = json_round[1]["reported_score"]
            round_instance.ended = json_round[1]["ended"]
            round_instance.match_list = []
            for json_match in enumerate(json_round[1]["match_list"]):
                match = Match()
                match.player_a = json_match[1][0][0]
                match.score_a = json_match[1][0][1]
                match.player_b = json_match[1][1][0]
                match.score_b = json_match[1][1][1]
                match.match_tuple = ([match._player_a, match.score_a],
                                     [match._player_b, match.score_b])
                round_instance.match_list.append(match)
            round_list.append(round_instance)
        tournament.round_list = round_list
        for json_player in enumerate(json_tournament[1]["player_list"]):
            player = Player()
            player.name = json_player[1]["name"]
            player.firstname = json_player[1]["firstname"]
            player.birthday = json_player[1]["birthday"]
            player.total_score = json_player[1]["total_score"]
            player.player_id = json_player[1]["player_id"]
            player_list.append(player)
        tournament.player_list = player_list
        tournament_list.append(tournament)
    return tournament_list


def update_json_tournament_list(_tournament='', _file=''):
    """ Used to give up to date tournament list JSON file
    """

    # 1- deserialize tournament list
    tournament_list = deserialize_tournament(_file)
    for tournament in (enumerate(tournament_list)):
        if ((_tournament.name == tournament[1].name) and (_tournament.location == tournament[1].location) and
                (_tournament.begin_date == tournament[1].begin_date)):
            tournament_list.pop(tournament[0])
            tournament_list.append(_tournament)
    serialized_data = serialize_tournament_list(object=tournament_list)
    save_data_to_json_file(objet=serialized_data, file=_file)
