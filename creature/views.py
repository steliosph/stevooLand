from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from creature.models import Creature
from creature.builder.FightingBuilder import FightingBuilder
from city.builder.healer import Healer


# Create your views here.
@login_required
def index(request):
    creatures = Creature.objects.all()

    return render(request, 'creature/index.html', {'creatures': creatures})


@login_required
def fight(request, creature_id, heal=None):
    if heal is not None:
        print('healing')

        healer = Healer(request.user)

        not_enough_gold_error = False
        if healer.has_sufficient_gold():
            healer.heal_characters()

    fighting_builder = FightingBuilder(creature_id, request.user)
    fighting_builder.fight()

    creature = fighting_builder.get_creature()
    if not creature:
        redirect('index')

    # people = request.user
    # fight_sequence = fight_creature(creature_id, people)
    # wE NEED TO DECIDE WHO STRIKES FIRST
    # fOR NOW WE STRIKE FIRST
    return render(request, 'creature/fight.html',
                  {'creature': creature, 'fight_sequence': fighting_builder.get_sequence()})
