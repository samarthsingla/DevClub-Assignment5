from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from account.models import Account
from django.contrib.auth import authenticate

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)
    name = forms.CharField(label='Full Name', required=True)
    is_instructor = forms.BooleanField(label="Instructor Account", required=False, help_text='Check the box if you are an instructor')

    class Meta:
        model = Account
        fields = ['username', 'name', 'email', 'password1', 'password2', 'is_instructor' ]
    # field_order = []

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Invalid Login Credentials")