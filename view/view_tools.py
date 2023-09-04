"""Tools to help for view"""

import re
from datetime import datetime


def user_input(_msg="", _lines=1):
    """ Allow cursor management, without needs
    to manage relative cursor position """

    up = ''
    for _ in range(_lines):
        up = up + "\033[F"
    CLEAR_LINE = "\033[K"
    print(up + CLEAR_LINE, end=_msg)
    return


def is_valid_date(date_string, date_format="%d/%m/%Y"):
    """ Date format and value validation """
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


def valid_id(id):
    """ Verify if passed id is usable
        OUT : ID if good ID else False"""
    # Pattern 2 Capital letters followed by 5 digits

    pattern = r'^[A-Z]{2}[0-9]{5}$'

    if re.match(pattern, id) is not None:
        return id
    return False
