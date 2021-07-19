from json import JSONEncoder
from functools import partial
from os import stat
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.utils import json
from main.models import Student, StudentTopic, Topic, Feedback
from .serializers import FeedbackSerializer, GetHelpSerializer, LoginSerializer, ResultSerializer, StudentTopicSerializer, TopicSerializer
from importlib import util
import io
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password
import jwt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import connection

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

    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def GetMyTopics(request):
    qs = StudentTopic.objects.all().count()
    if(qs <= 0):
        error_message = {
            'msg': 'No data.'
        }
        return JsonResponse(error_message, status=200)
    student = request.session.get('user')
    topics = StudentTopic.objects.all().filter(student=student)
    serializer = StudentTopicSerializer(topics, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def GetQuestion(request, id):

    qs = Topic.objects.get(id=id)
    algo = get_module(qs.algorithm.name, qs.algorithm.path)
    rand_question = algo.get_question()
    rand_answer = algo.get_answer()
    rand_instruction = algo.get_instruction()

    context = {
        'title': rand_question,
        'answer': rand_answer,
        'instructions': rand_instruction,
        'video_link': qs.video_link

    }
    json_data = JSONRenderer().render(context)
    return HttpResponse(json_data, content_type='application/json', status=200)


@csrf_exempt
def GetHelp(request):
    content = request.body
    input_stream = io.BytesIO(content)
    data = JSONParser().parse(input_stream)

    serializer = GetHelpSerializer(data=data)
    if serializer.is_valid():
        question = serializer.data['question']
        answer = serializer.data['answer']
        effort = serializer.data['effort']
        topic = serializer.data['topic']

        qs = Topic.objects.get(id=topic)
        algo = get_module(qs.algorithm.name, qs.algorithm.path)
        get_help = algo.get_help(question, answer, effort)

        print(answer)
        print(effort)
        print(get_help)
        json_data = JSONRenderer().render(get_help)
        return HttpResponse(json_data, content_type='application/json', status=200)


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

@csrf_exempt
def SubmitResult(request):
    content = request.body
    input_stream = io.BytesIO(content)
    json_data = JSONParser().parse(input_stream)

    serializer = ResultSerializer(data=json_data)

    if serializer.is_valid():
        if serializer.data['student_topic_id']:
            qs = StudentTopic.objects.get(
                id=serializer.data['student_topic_id'])

            previous_correct = qs.correct_answer
            previous_progress = (previous_correct/5) * 100

            current_correct = serializer.data['correct_answer']
            current_progress = (current_correct/5) * 100

            if previous_progress >= current_progress:

                context = {
                    'msg': 'Result has been updated.'
                }
                json_result = JSONRenderer().render(context)
                return HttpResponse(json_result, content_type='application/json', status=200)

            qs.total_attempts = serializer.data['total_attempts']
            qs.has_passed = serializer.data['has_passed']
            qs.correct_answer = serializer.data['correct_answer']
            qs.time_taken = serializer.data['time_taken']

            qs.save()

            context = {
                'msg': 'Result has been updated.'
            }
            json_result = JSONRenderer().render(context)
            return HttpResponse(json_result, content_type='application/json', status=200)

        topic = Topic.objects.get(id=serializer.data['topic_id'])
        student = Student.objects.get(id=request.session.get('user'))
        new_student_topic = StudentTopic(
            topic=topic,
            student=student,
            has_passed=serializer.data['has_passed'],
            total_attempts=serializer.data['total_attempts'],
            correct_answer=serializer.data['correct_answer'],
            time_taken=serializer.data['time_taken']
        )
        new_student_topic.save()

        context = {
            'msg': 'Result has been added.'
        }
        json_result = JSONRenderer().render(context)
        return HttpResponse(json_result, content_type='application/json', status=200)

    else:
        context = {
            'msg': 'Some error occured.'
        }

        json_result = JSONRenderer().render(context)
        return HttpResponse(json_result, content_type='application/json', status=400)


@csrf_exempt
def SubmitFeedback(request):
    content = request.body
    input_stream = io.BytesIO(content)
    data = JSONParser().parse(input_stream)
    serializer = FeedbackSerializer(data=data)

    if serializer.is_valid():
        student = Student.objects.get(id=serializer.data['student_id'])
        topic = Topic.objects.get(id=serializer.data['topic_id'])
        message = serializer.data['message']

        feedback = Feedback(
            student=student,
            topic=topic,
            message=message
        )
        feedback.save()
        context = {'msg': 'Feedback submitted successfully.'}
        json_data = JSONRenderer().render(context)
        return HttpResponse(json_data, content_type='application/json', status=200)

    context = {'msg': 'Error'}
    json_data = JSONRenderer().render(context)
    return HttpResponse(json_data, content_type='application/json', status=400)
