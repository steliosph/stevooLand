class Healer:
    __user = None
    __user_characters = None

    def __init__(self, user):
        self.__user = user
        self.__user_characters = self.__user.get_characters()

    def heal_characters(self):
        self.__subtract_gold()
        self.__heal_characters()

    def has_sufficient_gold(self):
        if self.__user.resources.gold >= self.calculate_gold_cost():
            return True
        return False

    def __subtract_gold(self):
        self.__user.resources.gold -= self.calculate_gold_cost()
        self.__user.resources.save()

    def calculate_gold_cost(self):
        gold_cost = 0
        for character in self.__user_characters:
            gold_cost += self.cost_for_character(character)
        return gold_cost

    def cost_for_character(self, character):
        health = (character.remaining_health - character.max_health) / 3
        # TODO  better formula to handle character.charisma
        gold_cost = health
        return int(abs(gold_cost))

    def __heal_characters(self):
        for character in self.__user_characters:
            character.remaining_health = character.max_health
            character.save()

    def create_characters_cost_matrix(self):
        print (self.__user_characters)
        w, h = len(self.__user_characters), 2;
        matrix = [['foo' for x in range(w) for y in range(h)]]
        count = 0
        for character in self.__user_characters:
            matrix[count][0] = character
            matrix[count][1] = self.cost_for_character(character)
            count += 1

        return matrix
