from django.test import TestCase
from people.models import People


# Create your tests here.
class CreateUserTests(TestCase):


    def test_create_user_etc(self):
        new_user = People.objects.create_people('username','email@email.com','pasd')
        print(new_user)

