from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from .models import Student, Organizer

class OrgRegisterForm(UserCreationForm):
    is_staff = forms.BooleanField(initial=True, widget=forms.HiddenInput)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_staff']

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(label='', widget=forms.TextInput(attrs={'autofocus':True, 'placeholder':'University ID'}))
    password = UsernameField(label='', widget=forms.PasswordInput(attrs={'autofocus':True, 'placeholder':'Password'}))

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = ['mobile']

class OrganizerUpdateForm(ModelForm):
    class Meta:
        model = Organizer
        exclude = ['user','idno', 'events',]