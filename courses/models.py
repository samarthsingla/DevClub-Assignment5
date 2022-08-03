from django.db import models
from account.models import Account

class Course(models.Model):
    code = models.CharField(unique=True, max_length=10, null=False, verbose_name="Course Code")
    title = models.CharField(max_length=100, verbose_name="Course Title")
    members = models.ManyToManyField(Account, verbose_name="Students", null=True) #both student and instructor members. This is more flexible because if we decide to add more user types (maybe admins) then we can just add them too. Also, these classes can overlap too (example: admin is also an instructor)
    credits = models.IntegerField(verbose_name="Credits")
    def __str__(self):
        return self.code
    

    def instructor_Count(self):
        return self.members.filter(is_instructor=True).count()
    
    def student_Count(self):
        return self.members.filter(is_instructor=False).count()

