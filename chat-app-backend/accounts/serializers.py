from rest_framework import serializers # type: ignore
from django.contrib.auth import get_user_model
from .tokenauthentication import JWTAuthentication

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validate_data):
        user = get_user_model().objects.create_user(
            email = validate_data['email'],
            password = validate_data['password'],
            first_name = validate_data.get('first_name', ""),
            last_name =validate_data.get('last_name', "")
        )
        return user
    
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password':{'write_only':True}}

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    id = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=255, write_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if email is None:
            raise serializers.ValidationError("An email is required for login")
        if password is None:
            raise serializers.ValidationError("A password is required for login")
        
        jwt_auth = JWTAuthentication()
        user = jwt_auth.authenticate(request=None)  # Pass None since it's not a HTTP request

        if user is None:
            raise serializers.ValidationError("Invalid email or password")
        if not user.is_active:
            raise serializers.ValidationError("User is inactive")
        
        return {
            "email": user.email,
            "id": user.id
        }
