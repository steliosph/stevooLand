from django.conf.urls import url

from . import views

app_name = 'character'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^character_selection$', views.character_selection, name='Character Selection'),
]