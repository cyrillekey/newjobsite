from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(max_length=60,widget=forms.EmailInput(attrs={'placeholder':'Enter email'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Repeat password'}))

    class Meta:
        model=Account
        fields=('email','username', 'password1','password2')        

class AccountAuthentication(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'EnterPassword'}), required=True)
    email=forms.EmailField(max_length=60,widget=forms.EmailInput(attrs={'placeholder':'Enter email'}))
    
    class Meta:
        model=Account
        fields=('email','password')
    def clean(self):
        if self.is_valid:
            email=self.cleaned_data['email']    
            password=self.cleaned_data['password']
            if not authenticate(email=email,password=password):
                raise forms.ValidationError("Invalid login details")    


