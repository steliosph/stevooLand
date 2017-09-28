from django.shortcuts import get_object_or_404, render, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import People
# Create your views here.


@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the people listing.")


@login_required
def detail(request, people_id):
    people = get_object_or_404(People, pk=people_id)
    return render(request, 'people/detail.html', {'people': people})