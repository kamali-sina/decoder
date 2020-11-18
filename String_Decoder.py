from persian_english_keyboardmap import kb_map
from meaning_check import meaning_check
from tqdm import tqdm

class String_Decoder:
    def __init__(self, split_by=' '):
        self.split_by = split_by
    
    def _print_list_of_duppeds(self, list_of_duppeds):
        for i in range(len(list_of_duppeds)):
            print(f'{i}: ', end='')
            self._print_dupped_string(list_of_duppeds[i])

    def _print_dupped_string(self, dupped_input):
        for i in dupped_input:
            print(i + ' ', end = '')
        print()
    
    def _english_kb_to_persian(self, dupped_input):
        print('\ntrying to translate to persian keyboard map...')
        ofile = open('./keyboard_map_result.txt', 'w')
        for i in dupped_input:
            word = i.lower()
            for j in range(len(word)):
                if (kb_map.get(word[j] , -1) != -1):
                    ofile.write(kb_map[word[j]])
                else:
                    ofile.write(word[j])
            ofile.write(self.split_by)
        ofile.write('\n')
        ofile.close()
        print('translation complete. wrote to "./keyboard_map_result.txt"')

    def _caesar_cipher(self , dupped_input):
        print('\ntrying ceasar cipher decode...')
        found = False
        result = []
        for key in tqdm(range (26)):
            mini_result = []
            for i in dupped_input:
                word = i.lower()
                new_word = ''
                for j in range(len(word)):
                    new_word = new_word + chr(((ord(word[j]) - ord('a') - key) % 26) + ord('a'))
                mini_result.append(new_word)
            if (meaning_check(mini_result)):
                found = True
                print('\ndecoded with ceasar cipher key ' + str(key) + ':')
                self._print_dupped_string(mini_result)
            result.append(mini_result)
        if (not found):
            print('\ncould not decode anything with meaning with ceasar cipher')
        else:
            print('done.')
        ans = input('do you want me to print all the results(y/n)? ')
        if (ans.strip().lower() == 'y' or ans.strip().lower() == 'yes'):
            print('printing all: \n')
            self._print_list_of_duppeds(result)

    def decode(self, input_string):
        dupped_input = input_string.split(self.split_by)
        self._english_kb_to_persian(dupped_input)
        self._caesar_cipher(dupped_input)