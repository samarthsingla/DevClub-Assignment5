from django.db import models
from account.models import Account
from courses.models import Course

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



