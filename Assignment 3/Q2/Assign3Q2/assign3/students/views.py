from django.shortcuts import render,redirect
from .forms import CreateStudentForm
from .models import Student

# Create your views here.
def home(request):
    student_list=Student.objects.all()
    context={
        "student_list":student_list
    }
    print(context)
    return render(request,'students/home.html',context)

def add(request):
    if request.method=="POST":
        form=CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:

        form =  CreateStudentForm()
    context={
        'form':form
    }
    return render(request,'students/add.html')