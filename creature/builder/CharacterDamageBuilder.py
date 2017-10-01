from character.characters.characters import CHARACTER_TYPES
from random import uniform

import decimal


class CharacterDamageBuilder:
    __character = None

    def __init__(self, character):
        self.__character = character

    def build(self):
        constant_damage = self.__calculate_constant_damage()
        base_damage = self.__calculate_base_damage(constant_damage)
        return base_damage

    def __calculate_constant_damage(self):
        return 16

    def __calculate_base_damage(self, constant_damage):
        """
        [{(Stat / 32) + 32} x DmCon  / 16]
        if Magician : 'Stat' = Intelligence + (Wisdom/3) + ((strength + dexterity + (Constitution * 2) + Charisma) /10)
        if Roque    : 'Stat' = Dexterity + (Strength/3) + ((Intelligence + Wisdom + (Constitution * 2) + Charisma) /10)
        if Cleric   : 'Stat' = Wisdom + ( Intelligence/3) + ((Intelligence + Wisdom + (Constitution * 2) + Charisma) /10)
        if Ranger   : 'Stat' = Dexterity + (Charisma/3) + ((Intelligence + Wisdom + (Constitution * 2) + Charisma) /10)

        """
        stat = 0
        strength = self.__character.strength
        dexterity = self.__character.dexterity
        intelligence = self.__character.intelligence
        wisdom = self.__character.wisdom
        constitution = self.__character.constitution
        charisma = self.__character.charisma

        if self.__character.find_character_type() == CHARACTER_TYPES[0][1]:  # Fighter
            stat = strength + (dexterity / 3) + ((intelligence + wisdom + (constitution * 2) + charisma) / 10)

        if self.__character.find_character_type() == CHARACTER_TYPES[1][1]:  # Magician
            stat = intelligence + (wisdom / 3) + ((strength + dexterity + (constitution * 2) + charisma) / 10)

        if self.__character.find_character_type() == CHARACTER_TYPES[2][1]:  # Roque
            stat = self.__character.dexterity + (strength / 3) + (
                (intelligence + wisdom + (constitution * 2) + charisma) / 10)

        if self.__character.find_character_type() == CHARACTER_TYPES[3][1]:  # Cleric
            stat = wisdom + (intelligence / 3) + (
                (strength + self.__character.dexterity + (constitution * 2) + charisma) / 10)

        if self.__character.find_character_type() == CHARACTER_TYPES[4][1]:  # Cleric
            stat = dexterity + (charisma / 3) + ((intelligence + wisdom + (constitution * 2) + strength) / 10)
        base_damage = ((stat ** 2 / 32) + 32) * constant_damage / 16
        # Add a variable to not have identical damage each time
        base_damage = base_damage + (base_damage * decimal.Decimal(uniform(0.0, 10.0) / 100))
        return decimal.Decimal(round(base_damage, 2))
