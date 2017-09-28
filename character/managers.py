from django.db import models
from character.characters import characters


class CharacterManager(models.Manager):
    def create_character(self, people, name, character_class):
        character = self.model(people=people, name=name, character_class=character_class)
        character_type = character.find_character()
        self.__create_character(character, character_type)
        self.__create_mana(character)
        self.__create_statistic(character)
        self.__save(character)

    @staticmethod
    def __create_character(character, selection):
        setattr(character, 'strength', selection.strength)
        setattr(character, 'dexterity', selection.dexterity)
        setattr(character, 'constitution', selection.constitution)
        setattr(character, 'intelligence', selection.intelligence)
        setattr(character, 'wisdom', selection.wisdom)
        setattr(character, 'charisma', selection.charisma)
        setattr(character, 'level', 1)
        setattr(character, 'max_health', characters.Paladin.health)
        setattr(character, 'remaining_health', characters.Paladin.health)
        setattr(character, 'experience', 0)

    @staticmethod
    def __create_mana(character):
        from character.models import CharacterMana
        mana = CharacterMana.objects.create()
        character.character_mana = mana

    @staticmethod
    def __create_statistic(character):
        from character.models import CharacterStatistic
        statistic = CharacterStatistic.objects.create()
        character.character_statistic = statistic

    def __save(self, character):
        character.save(using=self._db)

