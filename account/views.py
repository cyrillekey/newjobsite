#django imports used to manage account,login,logout and signup
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login as dj_login,authenticate,logout
from account.forms import RegistrationForm,AccountAuthentication

from job.models import Job,Job_skill,Skill

# Create your views here.
#function to allow user to login
def login(request):

    context={}
    
    user=request.user
    #check if user is authenticated and redirect to home page if authenticated otherwise login the user
    if user.is_authenticated:
        return redirect('home')
    #check is the request is a POST request if it is a post request check the details and log in the user otherwise show the login form 
    if request.POST:
        form=AccountAuthentication(request.POST)
        #check if the form was filled and is valid
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            #authenticate using the django authenticate method to check if the user exists
            user=authenticate(email=email,password=password)
            if user:
                dj_login(request,user)
                return redirect('home')
        else:
             #if from is invalid redirect user back to form to fill it correctly
            context['loginform']=form      
    else:
        #user accessing form through get initialive the form and pass it to the login template
        form=AccountAuthentication() 
        context['loginform']=form         
    #render the form for user to signin  
    return render(request, 'account/html/login.html',context)     

def signup(request):
    context={}
    user=request.user
    #check is user is loged in
    if not user.is_authenticated:
        #if user is not logged in proceed with signing up the user
        if request.POST:       
            form=RegistrationForm(request.POST)
            #check if the form was filled correctly
            if form.is_valid():
                #save the records in the account md=odel
                form.save()
                email=form.cleaned_data.get('email')
                raw_password=form.cleaned_data.get('password1')
                #use the password and email to create a session and redirect the user to the home page
                account=authenticate(email=email,password=raw_password)
                dj_login(request,account)
                return redirect('home')
            else:
                #form has some errors redirect the user to fill the form again
                context['registration_form']=form        

        else:
            #if form was accesed using a get method initialze the form and render the form
            form=RegistrationForm()
            context['registration_form']=form
        return render(request, 'account/html/signup.html',context)
    else:
        #user is authenticated so redirect to the homepage
        return redirect('home')                
              
def logout_view(request):
    #destroy the current session and redirect user to homepage
    logout(request)
    return redirect('home')

def school(request):
    user=request.user
    #check if user is authenticated and show them the school information form otherwise redirect to login page 
    if user.is_authenticated:
        return render(request,'account/html/school.html',{'name':'School information'})
    else:
        return redirect('login')

