from codecs import register
from django.urls import path
from .views import GetHelp, GetMyTopics, GetQuestion, login, GetAllTopics

urlpatterns = [
    path('getQuestion/<int:id>', GetQuestion),
    path('getMyTopics', GetMyTopics),
    path('getAllTopics', GetAllTopics),
    #path('register', signup),
    path('login', login),
    path('getHelp', GetHelp)
]
