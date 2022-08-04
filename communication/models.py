from django.db import models
from account.models import Account
from courses.models import Course
import json
# Create your models here.

class Announcement(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    instructor = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    content = models.TextField(verbose_name="Message")
    posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title + " in " + self.course.code + " by " + self.instructor.name
    
    def announcement_info(self):
        obj = {}
        obj['instructor'] = json.dumps(self.instructor.basicInfo())
        obj['title'] = self.title
        obj['content'] = self.content
        obj['posted_on'] = self.posted.strftime("%d %b, %Y at %H:%M")
        obj['course'] = self.course.code
        return obj


