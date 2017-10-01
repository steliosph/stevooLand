from django.db import models
from creature.creatures.creatures import CREATURE_TYPES
from creature.creatures.creature_position import CREATURE_POSITION_CHOICES


# Create your models here.
class Creature(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150,
                            choices=CREATURE_TYPES
                            )
    health = models.IntegerField()
    strength = models.IntegerField()
    defence = models.IntegerField()
    range_attack = models.IntegerField()
    range_defence = models.IntegerField()
    magic_attack = models.IntegerField()
    magic_defence = models.IntegerField()
    fight_description = models.CharField(max_length=750)

    drop_experience_minimum = models.SmallIntegerField()
    drop_experience_maximum = models.SmallIntegerField()
    drop_gold_minimum = models.SmallIntegerField()
    drop_gold_maximum = models.SmallIntegerField()
    drop_item_rate = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return "Creature[%s]  - %s - %s " % (str(self.id), self.name, self.type)


class CreatureGroups(models.Model):
    group = models.PositiveSmallIntegerField(blank=False)
    creature = models.ForeignKey('creature.Creature', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    fighting_position = models.CharField(max_length=5, choices=CREATURE_POSITION_CHOICES)

    class Meta:
        db_table = 'creature_group'
