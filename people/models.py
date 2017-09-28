from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils import timesince
from django.db import models
from django.utils.translation import gettext_lazy as _
from people.managers import PeopleManager
from character.models import Character


# Create your models here.
class Resources(models.Model):
    gold = models.PositiveIntegerField(default=1000)
    food = models.PositiveIntegerField(default=100)
    wood = models.PositiveIntegerField(default=100)
    iron = models.PositiveIntegerField(default=100)
    stone = models.PositiveIntegerField(default=100)
    materials = models.PositiveIntegerField(default=0)
    fragments = models.PositiveIntegerField(default=0)
    gemstones = models.PositiveIntegerField(default=0)
    fame = models.PositiveIntegerField(default=1)
    total_fame = models.PositiveIntegerField(default=1)

    def increase_fame(self):
        self.total_fame += self.total_fame + 1

    def __str__(self):
        return str(self.id)


class People(AbstractUser):
    nickname = models.CharField(
        _('nickname'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that nickname already exists."),
        },
    )
    resources = models.OneToOneField(Resources, blank=False)

    objects = PeopleManager()

    def get_age(self):
        return timesince(self.date_joined)

    def __str__(self):
        return "username [" + self.username + "] nickname [" + self.nickname + "] email [" + self.email + "]"

    def get_characters(self):
        characters = Character.objects.filter(people=self.id)
        return characters
