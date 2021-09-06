from django.shortcuts import render,redirect
from django.http import HttpResponse
from job.models import Job,Job_skill
# Create your views here.
def home(request):
    job=Job.objects.all()[0:4]
    return render(request,'displayjob/html/home.html',{'jobs':job})
def jobinfo(request,username):
    user=request.user
    if user.is_authenticated:
        job=Job.objects.all().filter(slug=username)
        name=username.replace("-",' ')
        name=name+"."
        skill=Job_skill.objects.all().filter()
        return render(request,'displayjob/html/jobinfo.html',{'username':job,'skills':skill})
        
    else:
        return redirect('login')
    

