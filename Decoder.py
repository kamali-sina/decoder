import sys
from Number_Decoder import Number_Decoder

argv = sys.argv
if (len(argv) < 2):
    print('state the type of decoding please, you can use -help for more information')
    exit()
if (argv[1] == '-help'):
    print('the modes currently supported are:\n\n1- decoding a string of numbers. keyword: number\n')
    exit()
if (len(argv) < 3):
    print('*no split_by specified, using space\n')
    split_by = ' '
else:
    split_by = argv[2]

class Decoder:
    def __init__(self, mode, split_by=' '):
        self.split_by = split_by
        self.decoder = None
        if (mode == 'number'):
            print('*setting mode to "string of numbers to string"\n')
            self.decoder = Number_Decoder(split_by=self.split_by)
        else:
            print('no mode recognized')
            exit()
    
    def decode(self, input_string):
        self.decoder.decode(input_string)


decoder = Decoder(argv[1], split_by)
input_string = input('please input the string to decode: ')
decoder.decode(input_string)