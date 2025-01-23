class Tape(object):

    blank_symbol = " "

    def __init__(self, tape_string=""):
        self.__tape = dict((enumerate(tape_string)))

    def __str__(self):
        s = ""
        min_used_index = min(self.__tape.keys())
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index):
            s += self.__tape[i]
        return s

    def __getitem__(self, index):
        if index in self.__tape:
            print("Read:  " + self.__tape[index] + " at position: " + str(index))
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        print("Write: " + char + " at position: " + str(pos))
        self.__tape[pos] = char
        print("Current tape: ", end="")
        for key, value in self.__tape.items():
            print(value, end="")
