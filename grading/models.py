from django.db import models
from account.models import Account
from courses.models import Course
from django.core.validators import *

class QuestionBank(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    qb_code = models.CharField(verbose_name="Question Bank Code",unique=True, max_length=50)
    name = models.CharField(verbose_name="Full Name", max_length=50)

    def __str__(self):
        return self.qb_code + " : " + self.name

class Question(models.Model):
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    question_bank = models.ManyToManyField(QuestionBank)
    content = models.JSONField(verbose_name="Question Content")
    # correct_marks = models.FloatField()


class Quiz(models.Model):
    pass

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField()

class Grade(models.Model):
    GRADE_CHOICES = (('A', 'A'), ('A-', 'A-'), ('B', 'B'), ('B-', 'B-'), ('C', 'C'), ('C-', 'C-'), ('D', 'D'), ('F', 'F'))
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Account, on_delete=models.CASCADE)
    points = models.IntegerField(validators=[MaxValueValidator(100)])
    grade  = models.CharField(max_length=2, choices=GRADE_CHOICES)
