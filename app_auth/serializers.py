from rest_framework import serializers
from django.contrib.auth import get_user_model as User
from .models import Exam, Question

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = "__all__"


class ExamSerializer(serializers.ModelSerializer):
    # questions = serializers.StringRelatedField(many=True, read_only=True)
    questions = QuestionSerializer(many=True, required=False)


    class Meta:
        model = Exam
        extra_kwargs = {'user': {'read_only': True}}
        # fields = '__all__'
        # fields = ["exam_id", "instructions", "title", "exam_time"]
        fields = ["exam_id", "instructions", "title", "exam_time", "questions"]


class UserSerializer(serializers.ModelSerializer):
    # exams = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    exams = ExamSerializer(many=True, required=False)
    class Meta:
        model = User()
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['email', 'password', 'first_name', 'exams']
