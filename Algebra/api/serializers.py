from datetime import date
from rest_framework import serializers


class TopicSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=120)
    published = serializers.DateTimeField()


class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    email = serializers.CharField(max_length=120)
    password = serializers.CharField(max_length=300)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=120)
    password = serializers.CharField(max_length=300)


class QuestionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    answer = serializers.CharField(max_length=120)
    hints = serializers.CharField(max_length=120)
