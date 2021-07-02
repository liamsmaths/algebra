from functools import partial
from os import stat
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from main.models import Student, Topic, Question
from .serializers import LoginSerializer, QuestionSerializer, RegisterSerializer, TopicSerializer
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
    qs = Topic.objects.all().filter(is_active=True).count()
    print(qs)
    if qs <= 0:
        error_message = {
            'msg': 'No data.'
        }
        return JsonResponse(error_message, status=200)

    topics = Topic.objects.all().filter(is_active=True)
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def GetQuestion(request, id):

    qs = Topic.objects.filter(id=id)
    algo = get_module(qs.algorithm.name, qs.algorithm.path)
    rand_question = algo.get_question()
    rand_answer = algo.get_answer()
    rand_hints = algo.get_hint()

    question = Question(
        topic=qs,
        title=rand_question,
        hints=rand_hints,
        answer=rand_answer
    )
    question.save()
    serializer = QuestionSerializer(question)
    json_data = JSONRenderer().render(serializer.data)
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
