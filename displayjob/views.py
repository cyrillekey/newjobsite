from django.shortcuts import render,redirect
from django.http import HttpResponse
from job.models import Job,Job_skill
from django.db.models import F
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
        skill=Job_skill.objects.all().filter(inter_job_id__job_name=name)
        return render(request,'displayjob/html/jobinfo.html',{'username':job,'skills':skill})
        
    else:
        return redirect('login')
    
def alljobs(request):
    user=request.user
    if user.is_authenticated:
        job=Job.objects.all()
      
        return render(request,'displayjob/html/alljobs.html',{'jobs':job})
        
    else:
        return redirect('login')
