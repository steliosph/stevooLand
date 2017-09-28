from character.builder.ExperienceBuilder import ExperienceBuilder
from random import randint
import decimal


class LootBuilder:
    __characters = None
    __creature = None
    __people = None

    def __init__(self, characters, creature, people, fight_sequence_builder):
        self.__characters = characters
        self.__creature = creature
        self.__creature.refresh_from_db()
        self.__people = people
        self.__fight_sequence_builder = fight_sequence_builder

    def build(self):
        self.__calculate_drop_gold_winnings()
        self.__calculate_experience_gained()
        self.__calculate_drop_resource()
        self.__calculate_extra_attribute()

    def __calculate_drop_gold_winnings(self):
        charisma = 0
        for character in self.__characters:
            charisma += character.charisma

        gold = randint(self.__creature.drop_gold_minimum, self.__creature.drop_gold_maximum)

        multiplier = 1 + (charisma / (decimal.Decimal(self.__creature.health) / 30))
        if multiplier > 4:  # We cap the multiplier at 4
            multiplier = 4
        # print("1 + ({} / ({} / 30))".format(charisma,decimal.Decimal(creature.health)))
        # print("min:{} max:{} mul:{} gold:{}".format(creature.drop_gold_minimum, creature.drop_gold_maximum, multiplier, gold))
        gold = round(gold * multiplier)

        self.__people.resources.gold += gold
        self.__people.resources.save()
        self.__fight_sequence_builder.append(
            "<br/>For some weird reason the {} was holding {} gold. You pick it up and carry on".format(
                self.__creature.name, gold))

    # PREVIOUS Level Xp + PREVIOUS Level Xp * 10%
    def __calculate_experience_gained(self):
        for character in self.__characters:
            experience = randint(self.__creature.drop_experience_minimum, self.__creature.drop_experience_maximum)
            multiplier = 1 + (float(character.intelligence) / (float(self.__creature.health) / 1.2))
            if multiplier > 3:  # Cap the multiplier at 3
                multiplier = 3
            experience_gained = experience * multiplier

            experience_builder = ExperienceBuilder(character, experience_gained,self.__fight_sequence_builder)
            experience_builder.add_experience()

            # self.__fight_sequence_builder.append(experience_builder.get_fight_sequence())

    def __calculate_drop_resource(self):
        None

    def __calculate_extra_attribute(self):
        None
