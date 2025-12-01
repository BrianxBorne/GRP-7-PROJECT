from . import views
from django.urls import path

urlpatterns = [

path('',views.home,name='homepage'),
path('about/',views.about,name='aboutpage'),
path('register/',views.register,name='registerpage'),
path('login/',views.login_view,name='loginpage'),

]