from functools import partial
from os import stat
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from main.models import Student, StudentTopic, Topic, Question
from .serializers import EffortSeriliazer, LoginSerializer, QuestionSerializer, ResultSerializer, StudentTopicSerializer, TopicSerializer
from importlib import util
import io
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password
import jwt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# @csrf_exempt
# def signup(request):
#     if request.method == 'POST':
#         content = request.body
#         input_stream = io.BytesIO(content)
#         data = JSONParser().parse(input_stream)
#         serializer = RegisterSerializer(data=data, partial=True)

#         if serializer.is_valid():
#             name = serializer.data['name']
#             email = serializer.data['email']
#             password = serializer.data['password']

#             student = Student.get_student_by_email(email)
#             if student:
#                 error_message = {
#                     'msg' : "Email is already taken."
#                 }
#                 json_data = JSONRenderer().render(error_message)
#                 return HttpResponse(json_data, content_type='application/data', status=400)

#             newStudent = Student(
#                 name = name,
#                 email = email,
#             )
#             newStudent.password = make_password(password)
#             newStudent.save()

#             send_activation_email(newStudent, request)

#             success_message = {
#                 'msg': "Registration successful."
#             }
#             json_data = JSONRenderer().render(success_message)
#             return HttpResponse(json_data, content_type='application/json', status=200)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        content = request.body
        input_stream = io.BytesIO(content)
        data = JSONParser().parse(input_stream)
        serializer = LoginSerializer(data=data, partial=True)
        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']

            student = Student.get_student_by_email(email)
            if student:
                checkPassword = check_password(password, student.password)
                if checkPassword:
                    request.session['user'] = student.id
                    encoded = jwt.encode({
                        'id': student.id,
                        'email': student.email,
                        'name': student.name
                    },
                        "algebra",
                        algorithm='HS256')
                    return HttpResponse(encoded, content_type='application/json', status=200)
                error_message = {
                    'msg': "Incorrect email or password."
                }
                json_data = JSONRenderer().render(error_message)
                return HttpResponse(json_data, content_type='application/josn', status=400)
            error_message = {
                'msg': "Incorrect email or password."
            }
            json_data = JSONRenderer().render(error_message)
            return HttpResponse(json_data, content_type='application/josn', status=400)


@api_view()
def GetAllTopics(request):
    topics = Topic.objects.all().filter(is_active=True)
    topic_serializer = TopicSerializer(topics, many=True)

    id = request.session.get('user')
    my_topics = StudentTopic.objects.filter(student=id)
    my_topic_serializer = StudentTopicSerializer(my_topics, many=True)

    context = {
        'all_topics': topic_serializer.data,
        'my_topics': my_topic_serializer.data
    }
    json_data = JSONRenderer().render(context)
    return HttpResponse(json_data, content_type='application/json', status=200)


def GetQuestion(request, id):

    qs = Topic.objects.get(id=id)
    algo = get_module(qs.algorithm.name, qs.algorithm.path)
    rand_question = algo.get_question()
    rand_answer = algo.get_answer()
    rand_instruction = algo.get_instruction()
    question = Question(
        topic=qs,
        title=rand_question,
        answer=rand_answer,
        instructions=rand_instruction
    )
    question.save()
    serializer = QuestionSerializer(question)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json', status=200)


@csrf_exempt
def GetHelp(request, id):
    topic = Topic.objects.get(id=id)
    content = request.body
    print(content)
    input_stream = io.BytesIO(content)
    data = JSONParser().parse(input_stream)
    serializer = EffortSeriliazer(data=data)

    algo = get_module(topic.algorithm.name, topic.algorithm.path)
    if serializer.is_valid():
        print(serializer.data['effort'])
        help_text = algo.get_help(serializer.data['effort'])
        json_data = JSONRenderer().render(help_text)
        return HttpResponse(json_data, content_type='application/josn', status=200)
    error_message = {
        'msg': 'Something went wrong.'
    }
    json_data = JSONRenderer().render(error_message)
    return HttpResponse(json_data, content_type='application/json', status=400)


@csrf_exempt
def SubmitResult(request):
    content = request.body
    print(content)
    input_stream = io.BytesIO(content)
    data = JSONParser().parse(input_stream)
    serializer = ResultSerializer(data=data)

    if serializer.is_valid():
        student = Student.objects.get(id=request.session.get('user'))
        topic = Topic.objects.get(id=serializer.data['topic_id'])
        newStudentResult = StudentTopic(
            student=student,
            topic=topic,
            has_passed=serializer.data['has_passed'],
            total_attempts=serializer.data['total_attempts'],
            time_taken=serializer.data['time_taken'],
            # last_attempt=serializer.data['last_attempt']
        )
        newStudentResult.save()
        success_message = {
            'msg': 'Practice session ended.'
        }
        json_data = JSONRenderer().render(success_message)
        return HttpResponse(json_data, content_type='application/json', status=200)
    error_message = {
        'msg': 'Something went wrong.'
    }
    json_data = JSONRenderer().render(error_message)
    return HttpResponse(json_data, content_type='application/json', status=400)


def get_module(name, location):
    spec = util.spec_from_file_location(name, location)
    foo = util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo


# def email_confirmation(request, uidb64, token):

#     student = confirm_email(request, uidb64, token)
#     if student:
#         student.is_email_confirmed = True
#         student.save()
#         return render(request, 'build/index.html')
#     else:
#         return render(request, 'error.html')
