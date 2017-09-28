from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class PeopleManager(BaseUserManager):
    def create_people(self, email, username, nickname, password):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        people = self.model(username=username, nickname=nickname, email=email,
                            is_staff=False, is_active=True,
                            is_superuser=False,
                            date_joined=now)
        people.set_password(password)
        from people.models import Resources

        people.resources = Resources.objects.create()
        people.save(using=self._db)

        return people
