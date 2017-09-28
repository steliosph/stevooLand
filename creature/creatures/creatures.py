from creature.creatures.creature_position import CREATURE_POSITION_CHOICES

class AbstractCreature(object):
    creature_id = None
    name = None
    type = None
    position = None

    strength = None
    defence = None
    range_attack = None
    range_defence = None
    magic_attack = None
    magic_defence = None
    experience = None
    gold = None
    drop_rate = None


CREATURE_TYPES = [
    ('Fighter', 'The Fighter Class'),
    ('Magician', 'The Magician Class'),
    ('Ranger', 'The Ranger Class'),
]

class Bug(AbstractCreature):
    creature_id = 1
    name = 'Bug'
    type = 'Fighter'
    position = CREATURE_POSITION_CHOICES[0]

    strength = 10
    defence = 10
    range_attack = 0
    range_defence = 10
    magic_attack = 0
    magic_defence = 7
    experience = 10
    gold_minumum = 3
    gold_maximum = 5
    drop_rate = 0.01

    description = 'You have approached a rather small bug. Since you though you were all powerful you try to squash it but it fights back. You did not see that coming.'


CREATURE_ENEMIES = (
    (Bug.creature_id, Bug)

)


def find_creature_type(creature_id):
    for type_id, type in CREATURE_TYPES:
        if creature_id == type_id:
            return type
    return None