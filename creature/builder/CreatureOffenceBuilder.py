from creature.creatures.creatures import CREATURE_TYPES
from random import uniform
import decimal


class CreatureOffenceBuilder:
    __creature = None

    def __init__(self, creature):
        self.__creature = creature

    def build(self):
        stat = self.__calculate_creature_offence()
        base_offence = decimal.Decimal((stat ** 2) / 78)
        base_offence = base_offence + (base_offence * decimal.Decimal(uniform(0.0, 5.0) / 100))

        return decimal.Decimal(round(base_offence, 10))

    def __calculate_creature_offence(self):
        if self.__creature.type == CREATURE_TYPES[0][0]:  # Fighter
            return (self.__creature.strength * 3) + (self.__creature.range_attack / 3) + (
            self.__creature.magic_attack / 4)
        elif self.__creature.type == CREATURE_TYPES[1][0]:  # Magician
            return (self.__creature.magic_attack * 3) + (self.__creature.range_attack / 3) + (
            self.__creature.strength / 4)
        elif self.__creature.type == CREATURE_TYPES[2][0]:  # Ranger
            return (self.__creature.range_attack * 3) + (self.__creature.strength / 3) + (
            self.__creature.magic_attack / 4)
