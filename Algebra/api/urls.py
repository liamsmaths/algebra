from codecs import register
from django.urls import path
from .views import GetQuestion, SubmitResult, login, GetAllTopics, GetHelp

urlpatterns = [
    path('getQuestion/<int:id>', GetQuestion),
    path('getAllTopics', GetAllTopics),
    #path('register', signup),
    path('login', login),
    path('getHelp/<int:id>', GetHelp),
    path('submitResult', SubmitResult)
]
