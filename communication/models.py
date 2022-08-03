from django.db import models
from account.models import Account
from courses.models import Course
# Create your models here.

class Announcement(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    instructor = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    content = models.TextField(verbose_name="Message")
    posted = models.DateTimeField(auto_now_add=True)
    
