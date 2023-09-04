""" Round Class """


from datetime import datetime


class Round:
    """Init a Round instance
    IN : Nothing
    The tournament begin, all needed information was early set
    in tournament instance
    """

    def __init__(self):
        """ Instance init"""
        self.name = ''
        self.start_time = str
        self.end_time = str
        self.match_list = []
        self.reported_score = False
        self.ended = False

    def add(self, name, match_list):
        """ Instance init"""
        self.name = name
        self.match_list = match_list

        current_date_time = datetime.now()
        self.start_time = current_date_time.strftime("%d-%m-%Y %H:%M:%S")
        self.end_time = "Round en cours de jeu !"

    def close(self):
        """Close a round
        IN : ()
            - Set round end time        """
        current_date_time = datetime.now()
        self.end_time = current_date_time.strftime("%d-%m-%Y %H:%M:%S")
        self.ended = True

    def __str__(self):
        return f"name={self.name}\
                    match_list={self.match_list}\
                        start_time={self.start_time}\
                            end_time={self.end_time}"

    def __repr__(self):
        return f"name={self.name}\
                    match_list={self.match_list}\
                        start_time={self.start_time}\
                            end_time={self.end_time}"
