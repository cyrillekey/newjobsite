from django.test import TestCase,Client
from django.urls import reverse
from account.models import Account,Educationinfo
import json
#test if the views render corrctly as specified
class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        self.account_url=reverse('login')
        self.signup_url=reverse('signup')
        self.logout_url=reverse('logout')
        self.school_url=reverse('school')
    def test_login(self):
        
        response=self.client.get(self.account_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'account/html/login.html')
    def test_signup(self):
        response=self.client.get(self.signup_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'account/html/signup.html')
    def test_logout(self):
        response=self.client.get(self.logout_url)
        self.assertRedirects(response,'/',302)
    def test_school(self):
        response=self.client.get(self.school_url)
        self.assertRedirects(response,'/login/',302)