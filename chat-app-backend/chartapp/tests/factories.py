import factory #type: ignore

from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import default_token_generator

from accounts.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True

    date_joined = factory.Faker('date_time_this_decade')
    
    @classmethod
    def create(cls, **kwargs):
        kwargs['password'] = make_password(kwargs.get('password', 'password'))  # Hash the password
        return super().create(**kwargs)
    
    @classmethod
    def _generate(cls, create, attrs):
        user = super()._generate(create, attrs)
        if create:
            cls._create_token(user)
        return user

    @classmethod
    def _create_token(cls, user):
        token = default_token_generator.make_token(user)