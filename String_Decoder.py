from persian_english_keyboardmap import kb_map

class String_Decoder:
    def __init__(self, split_by=' '):
        self.split_by = split_by
    
    def _english_kb_to_persian(self, dupped_input):
        print('\ntrying to translate to persian keyboard map...')
        ofile = open('./keyboard_map_result.txt', 'w')
        for i in dupped_input:
            for j in range(len(i)):
                if (kb_map.get(i[j] , -1) != -1):
                    ofile.write(kb_map[i[j]])
                else:
                    ofile.write(i[j])
            ofile.write(self.split_by)
        ofile.write('\n')
        ofile.close()
        print('translation complete. wrote to "./keyboard_map_result.txt"')

    def decode(self, input_string):
        dupped_input = input_string.split(self.split_by)
        self._english_kb_to_persian(dupped_input)