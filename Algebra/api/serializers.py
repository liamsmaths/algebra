from datetime import date
from main.models import StudentTopic
from rest_framework import serializers


class TopicSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=120)


class StudentTopicSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()

    class Meta:
        model = StudentTopic
        fields = ['id', 'has_passed', 'total_attempts',
                  'time_taken', 'last_attempt', 'topic']


# class RegisterSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=120)
#     email = serializers.CharField(max_length=120)
#     password = serializers.CharField(max_length=300)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=120)
    password = serializers.CharField(max_length=300)


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=120)
    answer = serializers.CharField(max_length=120)
    instructions = serializers.CharField(max_length=500)


class EffortSeriliazer(serializers.Serializer):
    effort = serializers.CharField(max_length=200)


class ResultSerializer(serializers.Serializer):
    topic_id = serializers.IntegerField()
    total_attempts = serializers.IntegerField()
    has_passed = serializers.BooleanField()
    #last_attempt = serializers.DateTimeField()
    time_taken = serializers.TimeField()
