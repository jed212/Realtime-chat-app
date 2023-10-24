from rest_framework import serializers
from django.contrib.auth import get_user_model

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
