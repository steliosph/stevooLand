from django.conf.urls import url

from . import views

app_name = 'city'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reviving_fruits$', views.revive, name='reviving_frutis'),
    url(r'^reviving_fruits/(heal_all)/$', views.revive, name='reviving_frutis'),
    url(r'^reviving_fruits/([\d]+)/$', views.revive, name='reviving_frutis'),
    url(r'^praying_temple$', views.praying_temple, name='praying_temple'),
    url(r'^praying_temple/(?P<character>(\d+))/(?P<pray>(\w+))/$', views.praying_temple, name='praying_temple'),
]