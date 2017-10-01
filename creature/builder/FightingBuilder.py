from creature.builder.CharactersToUseBuilder import CharactersToUse
from creature.builder.FightSequenceBuilder import FightSequenceBuilder
from creature.builder.CharacterDamageBuilder import CharacterDamageBuilder
from creature.builder.CreatureDefenceBuilder import CreatureDefenceBuilder
from creature.builder.CreatureOffenceBuilder import CreatureOffenceBuilder
from creature.builder.LootBuilder import LootBuilder
from creature.models import Creature
import decimal


class FightingBuilder():
    __creature = None
    __people = None
    __characters = None
    __fight_sequence_builder = None

    __characters = None

    def __init__(self, creature_id, people):
        self.__creature = Creature.objects.get(id=creature_id)
        self.__people = people
        self.__fight_sequence_builder = FightSequenceBuilder()
        self.__characters = []

    def get_creature(self):
        return self.__creature

    def fight(self):
        characters_to_use = CharactersToUse(self.__fight_sequence_builder, self.__people)
        self.__characters = characters_to_use.build()
        if not self.__characters:
            return
        self.__fight_sequence_builder.append(
            'You have started battling against {} <br/><br/>'.format(self.__creature.name))

        while self.__creature.health > 0:
            if not self.__characters:
                self.__fight_sequence_builder.append(
                    "<br/>You have failed to defeat the powerful {}. Better luck next time ...".format(
                        self.__creature.name))
                return

            for character in self.__characters:
                character_base_damage = CharacterDamageBuilder(character).build()
                creature_defence = CreatureDefenceBuilder(self.__creature).build()

                damage_dealt = decimal.Decimal(round(character_base_damage - creature_defence, 2))
                self.__creature.health -= damage_dealt

                self.__fight_sequence_builder.append(
                    "{} have strike the {} with her/his {} dealing <red>{}</red> damage".format(character.name,
                                                                                                self.__creature.name,
                                                                                                'hands',
                                                                                                damage_dealt))
                if self.__creature.health > 0:
                    self.__fight_sequence_builder.append(
                        "The {} is still alive with {} health remaining.".format(self.__creature.name,
                                                                                 self.__creature.health))

                else:
                    self.__fight_sequence_builder.append(
                        "You last strike was deadly. You have taken down the {}.".format(self.__creature.name))
                    LootBuilder(self.__characters, self.__creature, self.__people,
                                self.__fight_sequence_builder).build()
                    # We return as we reset the creatures and the health is restored.
                    return

                # Strike from monster
                creature_offence_builder = CreatureOffenceBuilder(self.__creature)
                creature_attack = creature_offence_builder.build()
                character.remaining_health = character.remaining_health - creature_attack
                d = "The {} has striked you with {} damage".format(self.__creature.name, creature_attack)

                if character.remaining_health > 0:
                    self.__fight_sequence_builder.append(
                        "{} You are still alive with {} health remaining".format(d, character.remaining_health))
                else:
                    self.__fight_sequence_builder.append(
                        "{} The {} has managed to defeat {}. You run away scared.".format(d, self.__creature.name,
                                                                                          character.name))
                    if character.remaining_health < 0:
                        character.remaining_health = 0
                    character.save(update_fields=["remaining_health"])
                    self.__characters.remove(character)

    def get_sequence(self):
        return self.__fight_sequence_builder.get_fight_sequence()
