from django.shortcuts import render

from .forms import CourseRegistrationForm
def register_course(request):
    # if request.method =="POST":
    #     form=CourseRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         print(form.errors)
    # else:
    form=CourseRegistrationForm()
    return render(request, "register_course.html", {'form':form})  

def Course_list(request):
    course=Course.objects.all()    
    return render(request,"Course_list.html",{"course":course})

# Create your views here.
