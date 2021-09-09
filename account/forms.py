from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account
#for the user will use when registering
class RegistrationForm(UserCreationForm):
    """
    Set the fields that will be needed when a user needs to register
    """
    email=forms.EmailField(max_length=60,widget=forms.EmailInput(attrs={'placeholder':'Enter email'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Repeat password'}))
#set fields to be shown on the form
    class Meta:
        #define model to be used when signinn up
        model=Account
        fields=('email','username', 'password1','password2')        
#form the user wil use to login
class AccountAuthentication(forms.ModelForm):
    """
    Set the fields that will be needed when a user wants to login
    """
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'EnterPassword'}), required=True)
    email=forms.EmailField(max_length=60,widget=forms.EmailInput(attrs={'placeholder':'Enter email'}))
    #define fields that will be shown on the form
    class Meta:
        #define model to be used when loging in
        model=Account
        fields=('email','password')
    def clean(self):

        if self.is_valid:
            #check if information entered is valid amd clean the input passed from the form to prevent injection and cross site scripting
            email=self.cleaned_data['email']    
            password=self.cleaned_data['password']
            #if information passed is not authentic set the error that will be shown on the form
            if not authenticate(email=email,password=password):
                raise forms.ValidationError("Invalid login details")    


