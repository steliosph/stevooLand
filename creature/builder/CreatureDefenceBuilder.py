from creature.creatures.creatures import CREATURE_TYPES
from random import uniform

import decimal


class CreatureDefenceBuilder:
    __creature = None

    def __init__(self, creature):
        self.__creature = creature

    def build(self):
        # TODO According to each type of attack
        stat = self.__calculate_according_to_creature_type(self.__creature)
        base_defence = decimal.Decimal((stat ** 2) / 48)
        base_defence = base_defence + (base_defence * decimal.Decimal(uniform(0.0, 5.0) / 100))

        return decimal.Decimal(round(base_defence, 10))

    def __calculate_according_to_creature_type(self, creature):
        if creature.type == CREATURE_TYPES[0][0]:  # Fighter
            return (creature.defence * 3) + (creature.range_defence / 3) + (creature.magic_defence / 4)
        elif creature.type == CREATURE_TYPES[1][0]:  # Magician
            return (creature.magic_defence * 3) + (creature.defence / 3) + (creature.range_defence / 4)
        elif creature.type == CREATURE_TYPES[2][0]:  # Ranger
            return (creature.range_defence * 3) + (creature.defence / 3) + (creature.magic_defence / 4)
