from _helpers import MORSE_CODE_DICT
from itertools import combinations

key_list = list(MORSE_CODE_DICT.keys())
value_list = list(MORSE_CODE_DICT.values())


def is_morse_code(string):
    for c in string:
        if c not in [".", "-", " ", "_", "/"]:
            return False
    return True


def decode_morse_code(splitted_string):
    message = ""
    for part in splitted_string:
        try:
            message += key_list[value_list.index(part)]
        except:
            message += " "
    return message


def decode_with_space_inject(string, num_of_spaces):
    all_messages = []
    locations = list(range(1, len(string)))
    all_combinations = combinations(locations, num_of_spaces)
    for state in all_combinations:
        splitted_string = []
        last_location = 0
        for i in range(len(state)):
            splitted_string.append(string[last_location : state[i]])
            last_location = state[i]
        splitted_string.append(string[last_location:])
        message = decode_morse_code(splitted_string)
        if len(message) > 0:
            all_messages.append(message)
    return all_messages


# ..-.-...--
