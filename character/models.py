from django.db import models
from character.characters import characters
from character import managers
from character.builder.experienceBuilder import ExperienceBuilder
from character.characters.characters import find_class
from character.characters.characters import find_character_type


# Create your models here.
class CharacterMana(models.Model):
    max_mana = models.PositiveSmallIntegerField(default=50)
    remaining_mana = models.PositiveSmallIntegerField(default=50)
    max_pvp_mana = models.PositiveSmallIntegerField(default=10)
    remaining_pvp_mana = models.PositiveSmallIntegerField(default=10)
    mana_reloads = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'character_character_mana'

    def __str__(self):
        return "Mana (%d/%d) - PVP (%d/%d) - Reload %d" % (
            self.remaining_mana, self.max_mana,
            self.max_pvp_mana, self.remaining_pvp_mana, self.mana_reloads)


class CharacterStatistic(models.Model):
    attacks_made = models.IntegerField(default=0)
    attacks_won = models.IntegerField(default=0)
    harvests_made = models.IntegerField(default=0)
    prayers_made = models.IntegerField(default=0)

    class Meta:
        db_table = 'character_statistic'


class Character(models.Model):
    people = models.ForeignKey('people.People', on_delete=models.CASCADE)
    character_class = models.IntegerField(choices=characters.CHARACTER_CLASSES)
    name = models.CharField(max_length=150)
    strength = models.DecimalField(max_digits=19, decimal_places=2)
    dexterity = models.DecimalField(max_digits=19, decimal_places=2)
    constitution = models.DecimalField(max_digits=19, decimal_places=2)
    intelligence = models.DecimalField(max_digits=19, decimal_places=2)
    wisdom = models.DecimalField(max_digits=19, decimal_places=2)
    charisma = models.DecimalField(max_digits=19, decimal_places=2)
    level = models.IntegerField(default=1)
    experience = models.DecimalField(max_digits=22, decimal_places=2)
    max_health = models.IntegerField()
    remaining_health = models.IntegerField()
    points_to_allocate = models.IntegerField(default=5)

    character_mana = models.OneToOneField(
        CharacterMana,
        on_delete=models.CASCADE
    )

    character_statistic = models.OneToOneField(
        CharacterStatistic,
        on_delete=models.CASCADE
    )

    objects = managers.CharacterManager()

    def find_character(self):
        return find_class(self.character_class)

    def find_character_type(self):
        character = self.find_character()
        return find_character_type(character.character_type)

    def experience_needed_next_level(self):
        builder = ExperienceBuilder(self, None, None)
        return builder.calculate_experience_needed()

    def __str__(self):
        return "%s - %s - %s - %s %s/%s" % (
            str(self.id), self.people.nickname, str(self.name), str(self.character_class), str(self.remaining_health),
            str(self.max_health))
