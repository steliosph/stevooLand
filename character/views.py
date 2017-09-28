from django.contrib.auth.decorators import login_required
from character.models import Character
from character.forms import UserCharacterSelectionForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from character.utils.utils import add_extra_character


# Create your views here.
@login_required
def index(request):
    people = request.user
    display_add_character = add_extra_character(people)
    characters = Character.objects.filter(people=people.id)
    return render(request, 'character/index.html',
                  {'characters': characters, 'display_add_character': display_add_character})


@login_required
def character_selection(request):
    people = request.user
    if not add_extra_character(people):
        return redirect('/character/')

    if request.method == "POST":
        form = UserCharacterSelectionForm(request.POST)
        if form.is_valid():
            people = request.user
            Character.objects.create_character(people, **form.cleaned_data)
            return HttpResponseRedirect('/character')

    else:
        form = UserCharacterSelectionForm()

    return render(request, 'character/character_selection.html', {"form": form})
