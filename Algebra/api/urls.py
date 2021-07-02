from codecs import register
from django.urls import path
from .views import GetQuestion, login, GetAllTopics

urlpatterns = [
    path('getQuestion/<int:id>', GetQuestion),
    path('getAllTopics', GetAllTopics),
    #path('register', signup),
    path('login', login)
]
