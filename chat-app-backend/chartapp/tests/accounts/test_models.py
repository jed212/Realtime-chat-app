import pytest

pytestmark = pytest.mark.django_db

class TestUserModel:
    def test_create_user(self, user_factory):
        """Test create_user function"""
        user = user_factory()
        assert user.check_password("password")

    def test_create_superuser(self, user_factory):
        """Test create_super_user function"""
        superuser = user_factory(is_superuser=True)
        assert superuser.check_password("password")

    def test_get_full_name(self, user_factory):
        """Test custom get_full_name method"""
        user = user_factory(first_name='John', last_name='Doe')
        assert user.get_full_name() == 'John Doe'

    def test_str_return(self, user_factory):
        """Test __str__ method of User model"""
        user = user_factory(email="test-user")
        assert user.__str__() == "test-user"
    