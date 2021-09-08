from django.shortcuts import render,redirect
#from django.http import HttpResponse
from django.contrib.auth import login as dj_login,authenticate,logout
from account.forms import RegistrationForm,AccountAuthentication
#from bs4 import BeautifulSoup
#mport requests
from job.models import Job,Job_skill,Skill
#from django.template.defaultfilters import slugify
#import time

# Create your views here.

def login(request):

    context={}
    user=request.user

    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form=AccountAuthentication(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(email=email,password=password)
            if user:
                dj_login(request,user)
                return redirect('home')
        else:
             
            context['loginform']=form      
    else:
        form=AccountAuthentication() 
        context['loginform']=form           
    return render(request, 'account/html/login.html',context)     

def signup(request):
    context={}
    user=request.user
    if not user.is_authenticated:
        
        if request.POST:       
            form=RegistrationForm(request.POST)
            if form.is_valid():
                print('hello world')
                form.save()
                email=form.cleaned_data.get('email')
                raw_password=form.cleaned_data.get('password1')
                account=authenticate(email=email,password=raw_password)
                dj_login(request,account)
                return redirect('home')
            else:
                
                context['registration_form']=form        

        else:
            print("and not this")
            form=RegistrationForm()
            context['registration_form']=form
        return render(request, 'account/html/signup.html',context)
    else:
        return redirect('home')                
              
def logout_view(request):
    logout(request)
    return redirect('home')

def school(request):
    user=request.user
    if user.is_authenticated:
        return render(request,'account/html/school.html',{'name':'School information'})
    else:
        return redirect('login')
"""
def inserttodatabase(request):
    jobs=['administrator-jobs','business-analyst-jobs','data-engineer-jobs','data-scientist-jobs','developer-jobs','devops-engineer','information-technology-project-manager-jobs','information-technology-specialist-jobs','java-developer-jobs','lead-technician-jobs','network-engineer-jobs','principal-software-engineer-jobs','security-engineer-jobs','senior-software-development-engineer-jobs','senior-oftware-engineer-jobs','senior-systems-engineer-jobs','software-developer-jobs','software-development-engineer-jobs','software-engineer-jobs','software-engineer-lead-jobs','software-engineering-manager-jobs','solutions-architect-jobs','specialist-jobs','staff-software-engineer-jobs','support-jobs','support-associate-jobs','support-specialist-jobs','systems-administrator-jobs','systems-engineer-jobs','technical-support-specialist-jobs']
    #jobs=['senior-software-engineer-jobs']#,'senior-systems-engineer-jobs','software-developer-jobs','software-development-engineer-jobs','software-engineer-jobs','software-engineer-lead-jobs','software-engineering-manager-jobs','solutions-architect-jobs','specialist-jobs','staff-software-engineer-jobs','support-jobs','support-associate-jobs','support-specialist-jobs','systems-administrator-jobs','systems-engineer-jobs','technical-support-specialist-jobs']
    for job in jobs:
        try:
            url='https://www.zippia.com/'+job+'/'
            webpage=requests.get(url,'html.parser')
            soup=BeautifulSoup(webpage.content,features='lxml')
            result=soup.find(attrs={'id':'whatTheyDo'})
            description=result.get_text()
            salary=soup.find(attrs={'class':'average-salary-num'})
            name=job.replace("-"," ")
            name=name.replace(' jobs',".")
            salary=salary.get_text()
            #get the needed skills for the job
            url='https://www.zippia.com/'+job+'/skills/'
            webpage=requests.get(url,'html.parser')
            soup=BeautifulSoup(webpage.content,features='lxml')
            skills=soup.find_all(attrs={'class':'skillNameText'})
            
            skills_data=[]
            education_data=[]
            for skill in (skills):
                skill=skill.get_text()
                skill=''.join(i for i in skill if not i.isdigit())
                skill=skill.replace(". ","")
                skills_data.append(skill)


            url='https://www.zippia.com/'+job+'/education/'
            webpage=requests.get(url,'html.parser')
            soup=BeautifulSoup(webpage.content,features='lxml')
            educations=soup.find_all(attrs={'class':'certification-title'})
            
            education_data=[]
            for education in educations:
                education=education.get_text()
                education=''.join(i for i in education if not i.isdigit())
                education=education.replace(". ","")
                education_data.append(education)    
            #get the most commmon needed education requirements     
            
            #print(name)
            #print(description)
            #print(salary)
            
            
            
            
            salary=salary.replace("$","")
            salary=salary.replace(",","")
            salary=int(salary)
            newjob=Job(job_id=job,job_name=name,job_description=description,job_average_salary=salary,slug=slugify(name),job_education=education_data)    
            newjob.save()
            print(job)
            for skill in skills_data:
                skill_id=skill+"123"
                newskill=Skill(skill_id=skill_id,skill_name=skill,skills_desc=skill,skill_type=skill)
                newskill.save()
                
                job_skills_data=Job_skill(inter_job_id=newjob,inter_skill_id=newskill)
                job_skills_data.save()
                time.sleep(10)
        except:
            print('one failed')
            time.sleep(10)
                    
    return HttpResponse("it run correctly")        
    """