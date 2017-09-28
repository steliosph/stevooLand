class FightSequenceBuilder:

    __fight_sequence = None

    def __init__(self):
        self.__fight_sequence = []

    def get_fight_sequence(self):
        #print('get')
        #print(self.__fight_sequence)
        return self.__fight_sequence

    def clear_fight_sequence(self):
        #print('clearing')
        #print(self.__fight_sequence)
        del self.__fight_sequence[:]
        #print('cleared')
        #print(self.__fight_sequence)

    def append(self, append):
        self.__fight_sequence.append(append)
