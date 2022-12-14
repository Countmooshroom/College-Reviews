import datetime
from django.db import models
from django.utils import timezone


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.course_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    homework = models.IntegerField(default=0)
    essays = models.IntegerField(default=0)
    attendance = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    def __str__(self):
        return self.name
