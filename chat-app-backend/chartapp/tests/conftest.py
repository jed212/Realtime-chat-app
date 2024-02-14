from pytest_factoryboy import register #type: ignore

from .factories import UserFactory

register(UserFactory)