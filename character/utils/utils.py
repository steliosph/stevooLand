def add_extra_character(people):
    # Find all person character
    from character.models import Character

    characters = Character.objects.filter(people=people.id)

    if len(characters) == 0:
        return True

    if len(characters) == 1:
        print(characters[0].level)
        if characters[0].level >= 10:
            return True

    return False
