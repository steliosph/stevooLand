import random

CHARACTER_TYPES = [
    ('Fighter', 'The Fighter Class'),
    ('Magician', 'The Magician Class'),
    ('Rogue', 'The Rogue Class'),
    ('Cleric', 'The Cleric Class'),
    ('Ranger', 'The Ranger Class'),
]


class AbstractCharacter(object):
    class_id = None
    character_type = None;
    health = None

    strength = None
    dexterity = None
    constitution = None
    intelligence = None
    wisdom = None
    charisma = None

    praying_strength = None
    praying_dexterity = None
    praying_constitution = None
    praying_intelligence = None
    praying_wisdom = None
    praying_charisma = None

    strong_against = None
    weak_against = None

    passive_skils = None
    in_fight_skills = None

    description = ''

    class Meta:
        abstract = True


class ran():
    def dom(start, end):
        return random.randint(start, end)


class Paladin(AbstractCharacter):
    class_id = 1
    character_type = 'Fighter'
    health = ran.dom(40, 50)

    strength = ran.dom(10, 20)
    dexterity = ran.dom(10, 20)
    constitution = ran.dom(10, 20)
    intelligence = ran.dom(3, 13)
    wisdom = ran.dom(2, 12)
    charisma = ran.dom(2, 12)

    praying_strength = 1
    praying_dexterity = 1.2
    praying_constitution = 1
    praying_intelligence = 0.65
    praying_wisdom = 0.5
    praying_charisma = 0.6

    strong_against = []
    weak_against = []

    passive_skills = []
    in_fight_skills = []

    description = 'This is a Paladin.'

    def __str__(self):
        return "Paladin %s" % self.class_id


class Barbarian(AbstractCharacter):
    class_id = 2
    character_type = 'Fighter'
    health = ran.dom(45, 55)

    strength = ran.dom(12, 22)
    dexterity = ran.dom(10, 20)
    constitution = ran.dom(10, 20)
    intelligence = ran.dom(2, 12)
    wisdom = ran.dom(2, 12)
    charisma = ran.dom(2, 12)

    praying_strength = 1.2
    praying_dexterity = 1
    praying_constitution = 1
    praying_intelligence = 0.7
    praying_wisdom = 0.5
    praying_charisma = 0.5

    strong_against = []
    weak_against = []

    passive_skills = []
    in_fight_skills = []

    description = 'This is a barbarian'

    image = '<img src="%(media_url)/question_mark.gif" alt="undecided" title="undecided">'

    def find_type(self):
        t = find_character_type(self.character_type)
        print(t)
        return t

    def __str__(self):
        return "Barbarian %s" % self.class_id


CHARACTER_CLASSES = [
    (Paladin.class_id, Paladin),
    (Barbarian.class_id, Barbarian),
]

def find_class(character_class):
    for class_id, type in CHARACTER_CLASSES:
        if character_class == class_id:
            return type
    return None


def find_character_type(character_type):
    for type_id, type in CHARACTER_TYPES:
        if character_type == type_id:
            return type
    return None
