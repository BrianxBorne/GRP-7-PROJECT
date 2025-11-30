from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

path('',views.home,name='homepage'),
path('about/',views.about,name='aboutpage'),
path('register/',views.register,name='registerpage'),
path('login/',views.login,name='loginpage'),
path('sidebar/',views.studentlist,name='sidebar'),
path('studentform/', views.studentform, name='studentform'),
path('add/', views.create_student,name="add"),
path('update/<int:id>',views.update_student,name="update"),
path('delete/<int:id>',views.delete_student,name="delete"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)