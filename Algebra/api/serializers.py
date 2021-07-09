from datetime import date
from django.db.models import query

from rest_framework.relations import RelatedField
from main.models import StudentTopic, Topic
from rest_framework import serializers


class StudentTopicSerializer(serializers.ModelSerializer):
    topic = serializers.StringRelatedField()

    class Meta:
        model = StudentTopic
        fields = ['id', 'has_passed', 'total_attempts',
                  'last_attempt', 'topic']


class TopicRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        return{
            'student_topic_id': obj.id,
            'has_passed': obj.has_passed,
            'total_attempts': obj.total_attempts,
            'last_attempt': obj.last_attempt,
            'correct_answer': obj.correct_answer
        }


class TopicSerializer(serializers.ModelSerializer):
    student_topics = TopicRelatedField(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'name', 'student_topics']


# class RegisterSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=120)
#     email = serializers.CharField(max_length=120)
#     password = serializers.CharField(max_length=300)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=120)
    password = serializers.CharField(max_length=300)


class GetHelpSerializer(serializers.Serializer):
    topic = serializers.IntegerField()
    question = serializers.CharField(max_length=200)
    answer = serializers.CharField(max_length=200)
    effort = serializers.CharField(max_length=200)


class ResultSerializer(serializers.Serializer):
    student_topic_id = serializers.IntegerField()
    topic_id = serializers.IntegerField()
    total_attempts = serializers.IntegerField()
    correct_answer = serializers.IntegerField()
    has_passed = serializers.BooleanField()
    #last_attempt = serializers.DateTimeField()
    time_taken = serializers.TimeField()
