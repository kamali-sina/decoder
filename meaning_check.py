from PyDictionary import PyDictionary

def meaning_check(dupped_input_string):
    threshold = 0.8
    dictionary = PyDictionary()
    i = 0
    for x in dupped_input_string:
        if (dictionary.meaning(x, disable_errors=True) != None):
            i += 1
    if ((i / len(dupped_input_string)) > threshold):
        return True
    else:
        return False