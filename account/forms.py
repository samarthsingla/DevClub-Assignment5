from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)
    class meta:
        model = User
    field_order = ['username', 'email', 'password1', 'password2']
