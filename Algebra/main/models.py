from os import stat
from django.db import models
from django.contrib.auth.hashers import make_password


class Student(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    plain_password = models.CharField(max_length=120)
    password = models.CharField(max_length=300, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.password = make_password(self.plain_password)
        super(Student, self).save(*args, **kwargs)

    @staticmethod
    def get_student_by_email(email):
        try:
            return Student.objects.get(email=email)
        except:
            return False


class Topic(models.Model):
    name = models.CharField(max_length=200)
    algorithm = models.FileField(upload_to="algorithms")
    published = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    answer = models.CharField(max_length=120)
    hints = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.title


class StudentTopic(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    has_passed = models.BooleanField(default=False)
    total_attempts = models.IntegerField(null=True, blank=True)
    time_taken = models.TimeField(null=True)
    last_attempt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.student.name) + " " + str(self.topic.title)
