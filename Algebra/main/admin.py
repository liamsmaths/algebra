from django.contrib import admin
from .models import Topic, Question, Student, StudentTopic


class AdminStudent(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'is_active']


class AdminTopic(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', ]
    # list_filter = ['is_active', 'published']
    # search_fields = ['name']


class AdminQuestion(admin.ModelAdmin):
    list_display = ['id', 'title', 'answer']


class AdminStudentTopic(admin.ModelAdmin):
    list_display = ['id', 'student', 'topic',
                    'has_passed', 'total_attempts', 'time_taken']


admin.site.register(Topic, AdminTopic)
admin.site.register(Question, AdminQuestion)
admin.site.register(Student, AdminStudent)
admin.site.register(StudentTopic, AdminStudentTopic)
