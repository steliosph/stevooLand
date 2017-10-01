class ExperienceBuilder:
    __character = None
    __experience_gained = None
    __fight_sequence_builder = None

    __FIRST_LEVEL = 100
    __POINTS_PER_LEVEL = 5

    def __init__(self, character, experience_gained, __fight_sequence_builder):
        self.__character = character
        self.__experience_gained = experience_gained
        self.__fight_sequence_builder = __fight_sequence_builder

    def add_experience(self):
        self.__character.experience = float(self.__character.experience) + self.__experience_gained
        self.__has_character_gained_level()
        self.__character.save(update_fields=["level", "experience", "remaining_health"])

    def __has_character_gained_level(self):
        experience_needed = self.calculate_experience_needed()
        if self.__character.experience > experience_needed:
            self.__character.level += + 1
            self.__character_set_health()
            self.__character.experience = experience_needed - self.__character.experience
            self.__character.points_to_allocate += self.__POINTS_PER_LEVEL
            self.__fight_sequence_builder.append(
                '{} have gained a level and have an extra {}({}) to spend.'.format(self.__character.name,
                                                                                   self.__POINTS_PER_LEVEL,
                                                                                   self.__character.points_to_allocate))
        else:
            self.__fight_sequence_builder.append(
                '{}(lvl {}) has earned {} experience and requires {} more experience out of {}  to gain a level.'
                    .format(self.__character.name, self.__character.level, round(self.__experience_gained, 2),
                            round(experience_needed - self.__character.experience, 2), experience_needed))

    def calculate_experience_needed(self):
        return self.__get_level_xp(self.__character.level) + (self.__get_level_xp(self.__character.level) * 10) / 100

    def __character_set_health(self):
        self.__character.max_health = (1.0515 ** float(self.__character.level) * 1000 - 1000) + (
            1.0115 ** float(self.__character.constitution) * 100 - 100)
        # Restore health to max
        self.__character.remaining_health = self.__character.max_health

    def __get_level_xp(self, level):
        return level * self.__FIRST_LEVEL
