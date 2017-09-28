from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from city.builder.healer import Healer
from city.builder.PrayingBuilder import PrayingBuilder


# Create your views here.
@login_required
def index(request):
    return render(request, 'city/index.html')


@login_required
def revive(request, heal_all=None):
    healer = Healer(request.user)

    not_enough_gold_error = False
    if heal_all is not None:
        if healer.has_sufficient_gold():
            healer.heal_characters()
            return HttpResponseRedirect('/city/reviving_fruits')
        else:
            not_enough_gold_error = True

    return render(request, 'city/reviving_fruits.html', {'characters': healer.create_characters_cost_matrix(),
                                                         'total_cost': healer.calculate_gold_cost(),
                                                         'not_enough_gold_error':not_enough_gold_error})

@login_required
def praying_temple(request, character=None, pray=None):
    print(pray)
    sequence = None
    if character is not None and pray is not None:
        builder = PrayingBuilder(request.user, character, pray)
        builder.build()
        sequence= builder.get_sequence()
    # redirect('praying_temple')

    return render(request, 'city/praying_temple.html', {'praying_sequence':sequence})
