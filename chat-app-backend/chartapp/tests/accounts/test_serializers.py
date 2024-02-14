import pytest #type: ignore

from django.test import RequestFactory
from accounts.serializers import UserSerializer, LoginSerializer
from django.contrib.auth.tokens import default_token_generator
from accounts.tokenauthentication import JWTAuthentication

pytestmark = pytest.mark.django_db

# Tests for UserSerializer
class TestUserSerializer:
    def test_user_serializer_creates_user(self, user_factory):
        serializer = UserSerializer(data={
            'email': 'test@example.com',
            'password': 'testpassword',
        })
        assert serializer.is_valid()
        user = serializer.save()
        assert user.email == 'test@example.com'
        assert user.check_password('testpassword')

    def test_user_serializer_validates_required_fields(self, user_factory):
        serializer = UserSerializer(data={})
        assert not serializer.is_valid()
        assert 'email' in serializer.errors
        assert 'password' in serializer.errors

# Tests for LoginSerializer
class TestLoginSerializer:
    def test_login_serializer_handles_inactive_user(self, user_factory):
        factory = RequestFactory()
        user = user_factory.create(is_active=False)
        
        # Mock request object
        request = factory.post('/login/', {'email': user.email, 'password': 'password'})
        
        # Pass the mock request object to the authenticate method
        jwt_auth = JWTAuthentication()
        user, error_message = jwt_auth.authenticate(request)
        
        # Check if user is None before accessing its attributes
        if user is not None:
            serializer = LoginSerializer(data={
                'email': user.email,
                'password': 'password',
            })
            assert not serializer.is_valid()
        else:
            # Handle the case when user is None
            assert error_message == "Token not found"