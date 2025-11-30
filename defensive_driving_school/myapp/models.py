from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    age=models.IntegerField()
    course_start=models.DateField()
    course_end=models.DateField()
    phone_num=models.IntegerField()

    def __str__(self):
        return f'{self.full_name} {self.email}'
    
class Register(models.Model):
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.username} {self.email}'
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return f"{self.user.username} Profile"
   
    
