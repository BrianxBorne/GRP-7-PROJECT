
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile, Student


from . models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['full_name','email', 'age', 'course_start' ,'course_end','phone_num']


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','email','password1','password2']

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic'] 