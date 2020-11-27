from rest_framework import serializers
from django.contrib.auth import get_user_model as User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User()
        fields = ['email', 'first_name', 'password']

class SignUpSerializer(serializers.ModelSerializer):
    # this is intented for login use only

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User()
        fields = '__all__'
