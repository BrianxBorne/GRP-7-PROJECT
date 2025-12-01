from urllib import request
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def register(request):
     if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #redirect to home page
            return redirect('home')
     else:
        form=RegisterForm()
     return render(request, 'register.html', {'form':form})
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("POST data:", request.POST)
        user = authenticate(request, username=username, password=password)
        print("Authenticated user:", user)
        if user is not None:
         auth_login(request, user)
         #redirect to home
         return redirect('/')
        else:
           messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')