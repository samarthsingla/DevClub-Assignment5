from django.forms import ModelForm
from django import forms
from courses.models import Course

class CourseAddForm(ModelForm):
    code = forms.CharField(max_length=10, help_text="10 characters or less")
    
    class Meta:
        model = Course
        fields = ['code', 'title', 'members',]