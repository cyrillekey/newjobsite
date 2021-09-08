from django.shortcuts import render,redirect
from django.http import HttpResponse
from job.models import Job,Job_skill
from textblob import TextBlob
# Create your views here.
def home(request):
    job=Job.objects.all()[0:4]
    return render(request,'displayjob/html/home.html',{'jobs':job,'name':'Home'})
def jobinfo(request,username):
    user=request.user
    if user.is_authenticated:
        job=Job.objects.all().filter(slug=username)
        name=username.replace("-",' ')
        name=name+"."
        skill=Job_skill.objects.all().filter(inter_job_id__job_name=name)
        return render(request,'displayjob/html/jobinfo.html',{'username':job,'skills':skill,'name':'Job info'})
        
    else:
        return redirect('login')
    
def alljobs(request):
    user=request.user
    if user.is_authenticated:
        job=Job.objects.all()
      
        return render(request,'displayjob/html/alljobs.html',{'jobs':job,'name':'Alljobs'})
        
    else:
        return redirect('login')
def search(request):
    searchword=request.GET.get('searchword',12)
    searchword=TextBlob(searchword)
    searchword=searchword.correct()
    user=request.user
    if user.is_authenticated:
        job=Job.objects.all().filter(job_name__contains=searchword) | Job.objects.all().filter(job_description__contains=searchword)
      
        return render(request,'displayjob/html/alljobs.html',{'jobs':job,'name':'Alljobs'})