from django.conf.urls import url
from . import views


# We are adding a URL called /home
app_name = 'home'
urlpatterns = [
    url(r'register$', views.register, name='register'),
    url(r'^$', views.index, name='index'),

]