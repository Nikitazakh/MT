class Tape:

    def __init__(self, tape_string = '_', blank_symbol = '_'):
        self.__tape = dict(enumerate(tape_string))
        self.blank_symbol = blank_symbol

    def __getitem__(self, item): #возвращает значение по индексу
        if item in self.__tape:
            return self.__tape[item]
        else:
            return self.blank_symbol

    def __setitem__(self, key, value):#присваивает на позицию
        self.__tape[key] = value



    def __str__(self):#возращает tape как строку
        s = ''
        a = min(self.__tape.keys())
        b = max(self.__tape.keys())
        for i in range(a, b+1):
            if i not in self.__tape.keys():
                s += self.blank_symbol
            else:
                s += self.__tape[i]
        return s


class TuringMachine(object):

    def __init__(self,
                 tape,
                 d_function,
                 final_states,
                 initial_state=0,
                 blank_symbol='_'):

        self.__tape = Tape(tape)
        self.__d_function = d_function
        self.__final_states = final_states
        self.__current_state = initial_state
        self.__blank_symbol = blank_symbol
        self.__head_position = 0

    def get_tape(self):
        return str(self.__tape)

    def step(self):
        elem_head = self.__tape[self.__head_position]
        a = (self.__current_state, elem_head)
        b = self.__d_function[a]
        self.__tape[self.__head_position] = b[1]
        if b[2] == 'R':
            self.__head_position += 1
        elif b[2] == 'L':
            self.__head_position -= 1
        self.__current_state = b[0]

    def final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False


d_function_1 = {(0, '0'): (0, '0', 'R'), (0, '1'):(0, '1', 'R'), (0, '_'):(1, '0','N')} #final - set([1])
d_function_2 = {(0, 'a'): (1, '_', 'R'), (0, 'b'): (2, '_', 'R'), (0, 'c'): (3, '_', 'R'), (0, 'd'): (4, 'd', 'R'),
                (0, '_'): (5, '_', 'N'),
                (1, 'a'): (1, 'a', 'R'), (1, 'b'): (1, 'b', 'R'), (1, 'c'): (1, 'c', 'R'), (1, 'd'): (1, 'd', 'R'),
                (1, '_'): (5, 'a', 'N'),
                (2, 'a'): (2, 'a', 'R'), (2, 'b'): (2, 'b', 'R'), (2, 'c'): (2, 'c', 'R'), (2, 'd'): (2, 'd', 'R'),
                (2, '_'): (5, 'b', 'N'),
                (3, 'a'): (3, 'a', 'R'), (3, 'b'): (3, 'b', 'R'), (3, 'c'): (3, 'c', 'R'), (3, 'd'): (3, 'd', 'R'),
                (3, '_'): (5, 'c', 'N'),
                (4, 'a'): (4, 'a', 'R'), (4, 'b'): (4, 'b', 'R'), (4, 'c'): (4, 'c', 'R'), (4, 'd'): (4, 'd', 'R'),
                (4, '_'): (5, 'd', 'N')} #final - set([5])
d_function_3 = {(0, 'a'): (1, 'a', 'N'), (0, 'b'): (2, 'b', 'N'), (0, 'c'): (3, 'c', 'N'), (0, 'd'): (4, 'd', 'N'),
                (0, '_'): (10, 'a', 'N'),
                (1, 'a'): (1, 'a', 'R'), (1, 'b'): (1, 'b', 'R'), (1, 'c'): (1, 'c', 'R'), (1, 'd'): (1, 'd', 'R'),
                (1, '_'): (2, '_', 'L'),
                (2, 'a'): (9, 'a', 'N'), (2, 'b'): (10, 'b', 'N'), (2, 'c'): (10, 'c', 'N'), (2, 'd'): (10, 'd', 'N'),
                (3, 'a'): (3, 'a', 'R'), (3, 'b'): (3, 'b', 'R'), (3, 'c'): (3, 'c', 'R'), (3, 'd'): (3, 'd', 'R'),
                (3, '_'): (4, '_', 'L'),
                (4, 'a'): (10, 'a', 'N'), (4, 'b'): (9, 'b', 'N'), (4, 'c'): (10, 'c', 'N'), (4, 'd'): (10, 'd', 'N'),
                (5, 'a'): (5, 'a', 'R'), (5, 'b'): (5, 'b', 'R'), (5, 'c'): (5, 'c', 'R'), (5, 'd'): (5, 'd', 'R'),
                (5, '_'): (6, '_', 'L'),
                (6, 'a'): (10, 'a', 'N'), (6, 'b'): (10, 'b', 'N'), (6, 'c'): (9, 'c', 'N'), (6, 'd'): (10, 'd', 'N'),
                (7, 'a'): (7, 'a', 'R'), (7, 'b'): (7, 'b', 'R'), (7, 'c'): (7, 'c', 'R'), (7, 'd'): (7, 'd', 'R'),
                (7, '_'): (8, '_', 'L'),
                (8, 'a'): (10, 'a', 'N'), (8, 'b'): (10, 'b', 'N'), (8, 'c'): (10, 'c', 'N'), (8, 'd'): (9, 'd', 'N'),
                (9, 'a'): (9, '_', 'L'), (9, 'b'): (9, '_', 'L'), (9, 'c'): (9, '_', 'L'), (9, 'd'): (9, '_', 'L'),
                (9, '_'): (10, '_', 'N')}#final - set([10])
d_function_4 = {(0, 'a'): (1, '_', 'R'), (0, 'b'): (2, '_', 'R'), (0, 'c'): (3, '_', 'R'), (0, 'd'): (4, '_', 'R'),
                (0, 'd'): (5, '_', 'N'),
                (1, 'a'): (5, 'a', 'N'), (1, 'b'): (5, 'a', 'N'), (1, 'c'): (5, 'a', 'N'), (1, 'd'): (5, 'a', 'N'),
                (1, '_'): (5, 'a', 'N'),
                (2, 'a'): (5, 'b', 'N'), (2, 'b'): (5, 'b', 'N'), (2, 'c'): (5, 'b', 'N'), (2, 'd'): (5, 'b', 'N'),
                (2, '_'): (5, 'b', 'N'),
                (3, 'a'): (5, 'c', 'N'), (3, 'b'): (5, 'c', 'N'), (3, 'c'): (5, 'c', 'N'), (3, 'd'): (5, 'c', 'N'),
                (3, '_'): (5, 'c', 'N'),
                (4, 'a'): (5, 'd', 'N'), (4, 'b'): (5, 'd', 'N'), (4, 'c'): (5, 'd', 'N'), (4, 'd'): (5, 'd', 'N'),
                (4, '_'): (5, 'd', 'N')} #final - set([4])
d_function_5 = {(0, 'a'): (3, '_', 'R'), (0, 'b'): (1, '_', 'R'), (0, 'c'): (2, '_', 'R'), (0, '_'): (3, '_', 'N'),
                (1, 'a'): (3, 'b', 'N'), (1, 'b'): (1, 'b', 'R'), (1, 'c'): (2, 'b', 'R'), (1, '_'): (3, 'b', 'N'),
                (2, 'a'): (3, 'c', 'N'), (2, 'b'): (1, 'c', 'R'), (2, 'c'): (2, 'c', 'R'), (2, '_'): (3, 'c', 'N')}
#final - set([3])
TM = TuringMachine('bbbbacaba',d_function_5, set([3]))
while not TM.final():
    TM.step()
print(TM.get_tape())