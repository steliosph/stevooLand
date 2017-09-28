from django.conf.urls import url

from . import views

app_name = 'creature'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<creature_id>[0-9]+)/(?P<heal>(heal))/$', views.fight, name='fight'),
    url(r'^(?P<creature_id>[0-9]+)/$', views.fight, name='fight'),

]