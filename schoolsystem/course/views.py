from django.shortcuts import render
from .models import Course
from .forms import CourseForm

# Create your views here.


def course_form(request):
    if request.method == "POST":
        form = CourseForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)    
    else:
        form = CourseForm()
    return render(request,'course_form.html',{'form':form})
def course_list(request):
    courses=Course.objects.all()
    return render(request,'course_list.html',{'courses':courses})       
