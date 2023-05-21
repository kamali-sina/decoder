# pylint: disable=F0401
import periodictable as pt

START_OF_ALPHABET = 97


class Number_Decoder:
    def __init__(self, split_by=" "):
        self.split_by = split_by

    def _ascii_to_string(self, dupped_input):
        print('to ascii string: "', end="")
        for i in dupped_input:
            if int(i) > 255:
                print("this set of numbers can't be ascii")
                return
            print(chr(int(i)), end="")
        print('"')

    def _alphabet_to_string(self, dupped_input):
        print('to alphabet string: "', end="")
        for i in dupped_input:
            print(chr(((int(i) - 1) % 26) + START_OF_ALPHABET), end="")
        print('"')

    def _periodic_table_to_string(self, dupped_input):
        print('to periodic table string: "', end="")
        try:
            for i in dupped_input:
                print(pt.elements[int(i)], end="")
        except:
            print("--this set of numbers cannot be parsed to periodic table elements--")
        print('"')

    def decode(self, input_string):
        dupped_input = input_string.split(self.split_by)
        self._ascii_to_string(dupped_input)
        self._alphabet_to_string(dupped_input)
        self._periodic_table_to_string(dupped_input)
