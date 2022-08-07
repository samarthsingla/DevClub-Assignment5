from django import forms
from grading.models import Assignment

class createAssignmentForm(forms.ModelForm):
    file = forms.FileInput()


