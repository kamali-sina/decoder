from _helpers import kb_map
from meaning_check import meaning_check
from tqdm import tqdm
from morse_code import decode_with_space_inject, decode_morse_code

class String_Decoder:
    def __init__(self, split_by=' ', words=None):
        self.split_by = split_by
        self.words = words

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
        for key in range (26):
            mini_result = []
            for i in dupped_input:
                word = i.lower()
                new_word = ''
                for j in range(len(word)):
                    new_word = new_word + chr(((ord(word[j]) - ord('a') - key) % 26) + ord('a'))
                mini_result.append(new_word)
            if (meaning_check(mini_result, word_list=self.words)):
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

    def _morse_code(self, input_string):
        splitted_string = input_string.split()
        message = decode_morse_code(splitted_string)
        if (len(message) > 0):
            print(f'decoded morse code: {message}')
            return
        ans = input('\nfailed to decode morse code, do you want to brute force attack(y/n)? ')
        if (ans.strip().lower() == 'n' or ans.strip().lower() == 'no'):
            print('continuing...')
            return
        print('\nstarting brute force attack...')
        ofile = open('./morse_code_result.txt', 'w')
        # '\n'.join(lines) + '\n'
        for num_of_spaces in tqdm(range(len(input_string))):
            decodes = decode_with_space_inject(input_string, num_of_spaces)
            ofile.write(f'decoded with {num_of_spaces} spaces:\n')
            ofile.write('\n'.join(decodes) + '\n')
        ofile.close()
        print('\nall decoded codes can be found in "./morse_code_result.txt"')

    def decode(self, input_string):
        dupped_input = input_string.split(self.split_by)
        self._english_kb_to_persian(dupped_input)
        self._caesar_cipher(dupped_input)
        self._morse_code(input_string)