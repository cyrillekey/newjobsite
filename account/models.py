from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class MyaccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have a username")    
        user=self.model(
            email=self.normalize_email(email),
            username=username,
        )    
        user.set_password(password)
        user.save(using=self._db)
        return user
     
    def create_superuser(self,email,username,password):
        user=self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        ) 
        user.is_admin=True
        user.is_staff=True
        user.is_supperuser=True
        user.save(using=self._db)

        return user



class Account(AbstractBaseUser):
    username=models.CharField( verbose_name="username" ,max_length=50 ,unique=True)
    email=models.EmailField( verbose_name="email" ,max_length=254 ,unique=True)
    date_joined=models.DateTimeField(verbose_name="date-joined", auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last-login",auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_password=models.CharField(max_length=50)
    user_passwordRepeat=models.CharField(max_length=50)
    
    USERNAME_FIELD= "email"
    REQUIRED_FIELDS=["username"]

    objects=MyaccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True 

class Educationinfo(models.Model):
    education_level=models.CharField(max_length=50)
    working_experience_year=models.CharField(max_length=20)
    field_of_study=models.CharField(max_length=50)
    skills=models.JSONField(default=dict)