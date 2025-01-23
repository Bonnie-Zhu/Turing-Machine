import time
from Tape import Tape


class TuringMachine(object):

    def __init__(
        self,
        tape="",
        blank_symbol=" ",
        initial_state="",
        final_states=None,
        transition_function=None,
    ):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)

    def get_tape(self):
        return str(self.__tape)

    def step(self):
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == "R":
                self.__head_position += 1
                print("  ↣ Move head 1 right")
            elif y[2] == "L":
                self.__head_position -= 1
                print("  ↢ Move head 1 left")
            self.__current_state = y[0]
            print("             ", end="")
            for head_position_counter in range(self.__head_position):
                print(" ", end="")
            print("▲\n")
            time.sleep(1.0)

    def final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False
