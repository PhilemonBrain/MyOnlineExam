from rest_framework import serializers
from django.contrib.auth import get_user_model as User
from .models import Exam

class UserSerializer(serializers.ModelSerializer):
    exams = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User()
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['email', 'password', 'first_name', 'exams']


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        extra_kwargs = {'user': {'read_only': True}}
        fields = '__all__'