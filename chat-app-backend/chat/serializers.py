from rest_framework import serializers # type: ignore
from django.contrib.auth import get_user_model

class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name','id']
        extra_kwargs = {'id': {'read_only': True}}