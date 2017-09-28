from home.abstract.AbstractListMessage import AbstractListMessage
from character.characters.characters import find_character_type


class PrayingBuilder(AbstractListMessage):
    __people = None
    __character = None
    __pray = None

    def __init__(self, people, characterId, pray):
        super(PrayingBuilder, self).__init__()

        self.__people = people
        self.__character = self.__find_character(characterId)
        self.__pray = pray

    def __find_character(self, characterId):
        characters = self.__people.get_characters()
        for character in characters:
            if character.id == characterId:
                return character
        return None

    def build(self):
        if not self.__pray:
            self.append(
                "<b>s1Tevoo is visibly annoyed. It feels that you are trying to cheat him. Doing that again might make him so "
                "angry that will punishd you by removing some of your stats</b>")
            return
        if self.__is_not_allowed_pray_type():
            return
        if (self.__is_character_not_set()):
            return
        self.__pray()

    def __is_not_allowed_pray_type(self):
        if (self.__pray == 'strength') or (self.__pray == 'dexterity') or (self.__pray == 'constitution') or (
                    self.__pray == 'intelligence') or (self.__pray == 'wisdom') or (self.__pray == 'charisma'):
            return False
        self.append(
            "<b>2sTevoo is visibly annoyed. It feels that you are trying to cheat him. Doing that again might make him so "
            "angry that will punishd you by removing some of your stats</b>")
        return True

    def __is_character_not_set(self):
        if self.__character != None:
            return False
        self.append(
            "<b>2sTevoo is visibly annoyed. It feels that you are trying to cheat him. Doing that again might make him so "
            "angry that will punishd you by removing some of your stats</b>")
        return True

    def __pray(self):
        type = find_character_type()
