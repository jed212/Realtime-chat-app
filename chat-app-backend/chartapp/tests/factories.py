import factory
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

from accounts.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True

    date_joined = factory.Faker('date_time_this_decade')
    password = factory.Faker('password')