from urllib import request
from django.shortcuts import redirect, render
from .forms import RegisterForm
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
    
def login(request):
    return render(request, 'login.html')