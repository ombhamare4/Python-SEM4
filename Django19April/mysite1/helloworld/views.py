from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from django.forms import StudentForm
from .models import Student

def hello(request):    
    return HttpResponse("<h1>Hello</h1>")#adding html css

def greet(request):
    return HttpResponse("Ohayo")
 
def student(request):

    data= Student.objects.all()
    context={
        "data":data
    }
    return render(request,'helloworld/student.html',context)






    
    # if request.method=='POST':
    #     form=StudentForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()

    #         pass
    # else:
    #     form = StudentForm()
    
    # return HttpResponse("")