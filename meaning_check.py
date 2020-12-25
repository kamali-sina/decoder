def meaning_check(dupped_input_string, word_list=None, threshold=0.6):
    if (word_list == None):
        from nltk.corpus import words
        word_list = words.words()
    i = 0
    for x in dupped_input_string:
        if (x in word_list):
            i += 1
    if ((i / len(dupped_input_string)) > threshold):
        return True
    else:
        return False