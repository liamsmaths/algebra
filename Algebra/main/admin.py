from django.contrib import admin
from .models import Topic, Student, StudentTopic, Feedback


class AdminStudent(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'is_active']
    search_fields = ['name', 'email']


class AdminTopic(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', ]
    list_filter = ['is_active']
    search_fields = ['name']


class AdminStudentTopic(admin.ModelAdmin):
    list_display = ['id', 'student', 'topic',
                    'has_passed', 'total_attempts', 'time_taken']
    search_fields = ['student__name', 'topic__name']
    list_filter = ['has_passed']


class AdminFeedback(admin.ModelAdmin):
    list_display = ['id', 'student', 'topic', 'message']
    search_fields = ['student__name', 'topic__name']


admin.site.register(Topic, AdminTopic)
admin.site.register(Student, AdminStudent)
admin.site.register(StudentTopic, AdminStudentTopic)
admin.site.register(Feedback, AdminFeedback)
