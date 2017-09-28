from character.models import Character


class CharactersToUse:
    __sequence_builder = None
    __people = None
    __characters = None
    __characters_to_use = None

    def __init__(self, __fight_sequence_builder, people):
        self.__people = people
        self.__sequence_builder = __fight_sequence_builder
        self.__characters_to_use = []

    def build(self):
        self.__retrieve_people_characters()
        self.__find_usable_characters()
        self.__check_characters()
        return self.__characters_to_use

    def __retrieve_people_characters(self):
        self.__characters = Character.objects.filter(people=self.__people.id).exclude(remaining_health__lte=0)

    def __find_usable_characters(self):
        characters = []
        for character in self.__characters:
            mana = character.character_mana
            # Retrieve all characters with remaining fighting mana
            if mana.remaining_mana > 0:
                self.__characters_to_use.append(character)
            else:
                self.__sequence_builder.append(
                    "{} does not have any fighting mana remaining ...".format(character.name))

    def __check_characters(self):
        if not self.__characters_to_use:
            self.__sequence_builder.append('You don\'t seem to have any able fighters today. Come back tomorrow')
        else:
            self.__deduct_mana_from_characters()

    def __deduct_mana_from_characters(self):
        for character in self.__characters_to_use:
            mana = character.character_mana
            mana.remaining_mana -= 1
            mana.save()
            self.__sequence_builder.append("{} has joined the party ... <br/><br/>".format(character.name))
