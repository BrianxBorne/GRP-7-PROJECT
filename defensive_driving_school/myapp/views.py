from django.shortcuts import redirect,render
from .models import Student, Register
from .forms import StudentForm, RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        # If form is invalid fall through to re-render with errors
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
    
def login(request):
    return render(request, 'login.html')
def sidebar(request):
    return render(request,'sidebar.html')
def studentform(request):
    student=Student.objects.all()
    return render(request, "studentform.html", {'student':student})
@login_required


def studentlist(request):
    student=Student.objects.all()
    return render(request, "studentlist.html", {'student':student})

def create_student(request):
    if request.method == "POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sidebar')

    else:
        form=StudentForm()        

    return render(request, "studentform.html", {'form':form})


def update_student(request,id):
    student=Student.objects.get(id=id)
    form=StudentForm(instance=student)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('sidebar')
        

    return render(request,"studentform.html",{'form':form})
#delete a record
def delete_student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('home')
 
