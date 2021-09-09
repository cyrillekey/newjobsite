from django.test import SimpleTestCase
from django.urls import reverse,resolve
from account.views import login,logout_view,signup,school

class TestUrls(SimpleTestCase):

    def test_login_urls_resolves(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func,login)

    def test_logout_url_resolves(self):
        url=reverse('logout')
        self.assertEquals(resolve(url).func,logout_view)

    def test_signup_url_resolves(self):
        url=reverse('signup')
        
        self.assertEquals(resolve(url).func,signup)        
    def test_school_url__resolves(self):
        url=reverse('school')
        self.assertEquals(resolve(url).func,school)    