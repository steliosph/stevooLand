from django.shortcuts import render
from django.contrib.auth import login
from home.forms import UserCreationForm
from people.models import People
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse


# Create your views here.
@login_required
def index(request):
    return render(request, 'home/index.html')



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = People.objects.create_people(**form.cleaned_data)
            login(request,new_user)
            # redirect to our main page
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'home/register.html', {'form': form})