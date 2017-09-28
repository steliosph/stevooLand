"""
A sequence creator inorder to pass a list of execution so we can print them on the list
TODO make this in an ordered list

"""


class AbstractListMessage:
    __fight_sequence = None

    def __init__(self):
        self.__fight_sequence = []

    def clear_sequence(self):
        del self.__fight_sequence[:]

    def append(self, append):
        self.__fight_sequence.append(append)

    def get_sequence(self):
        return self.__fight_sequence

    class Meta:
        abstract = True
