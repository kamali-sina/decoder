from PyDictionary import PyDictionary

helper = ['i', 'a']

def meaning_check(dupped_input_string):
    threshold = 0.6
    dictionary = PyDictionary()
    i = 0
    for x in dupped_input_string:
        if (dictionary.meaning(x, disable_errors=True) != None or x in helper):
            i += 1
    if ((i / len(dupped_input_string)) > threshold):
        return True
    else:
        return False