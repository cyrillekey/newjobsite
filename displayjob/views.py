from django.shortcuts import render,redirect
from django.http import HttpResponse
from job.models import Job,Job_skill,Material_skill,materials_table
from textblob import TextBlob#library to correct spelling mistake in string
# Create your views here.
#view to display the homepage
def home(request):
    #selection the first 4 jobs from the jobs table
    job=Job.objects.all()[0:4]
    #rendering the home page and passing the 4 jobs collected from the Job model
    return render(request,'displayjob/html/home.html',{'jobs':job,'name':'Home'})
#view to show information about the a particularjob the username arg is the name of the specif job    
def jobinfo(request,username):
    #check is user is authenticated first before proceeding
    user=request.user
    if user.is_authenticated:
        #if user is authenticated select the specific job from the Jobs model and return it
        job=Job.objects.all().filter(slug=username)
        """
        sanitize the job name by removing - and adding a fullstop at the end
        """
        name=username.replace("-",' ')
        name=name+"."
        #select all the skills associated with the specific job
        skill=Job_skill.objects.all().filter(inter_job_id__job_name=name)
        
      
        mamerials=Material_skill.objects.all().filter(inter_skills_id__skill_name='Java')
        mamerials=(materials_table.objects.all().filter(material_name=mamerials[0].inter_material_id))
        #render the job infromation  page with the information collected from the Jobs model 
        return render(request,'displayjob/html/jobinfo.html',{'username':job,'skills':skill,'name':'Job info','materials':mamerials})
        
    else:
        #if user is not authenticated redirect user to the login page to login first before accesing the jibs infromation
        return redirect('login')

#method to show all the jobs    
def alljobs(request):
    #check if the user is authenticated
    user=request.user
    if user.is_authenticated:
        #get all the jobs from the Joob model
        job=Job.objects.all()
      #render all the Jobs from the job model
        return render(request,'displayjob/html/alljobs.html',{'jobs':job,'name':'Alljobs'})
        
    else:
        #if user is not authenticetd redirect back to login page
        return redirect('login')
#method to search for a specific job using the Jobname        
def search(request):
    #get the job to be searched for from the search form
    searchword=request.GET.get('searchword')
    #using the textblob library correct any spelling mistakes in the word

    searchword=TextBlob(searchword)
    searchword=searchword.correct()
    #check if user is authenticated
    user=request.user
    #if user is authenticated search for jobs with the searchword in the name of the job and job description
    if user.is_authenticated:
        job=Job.objects.all().filter(job_name__contains=searchword) | Job.objects.all().filter(job_description__contains=searchword)
      #render all the jobs found that have the keyword in the name or description
        return render(request,'displayjob/html/alljobs.html',{'jobs':job,'name':'Alljobs'})
    else:
        #redirect user to lgin page if not authenticated
        return redirect('login')    