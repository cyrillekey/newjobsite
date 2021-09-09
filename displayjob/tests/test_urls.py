from django.test import SimpleTestCase
from django.urls import reverse,resolve
from displayjob.views import home,alljobs,search,jobinfo
#test if the urls to display jobs work correctly
class TestUrls(SimpleTestCase):

    def test_login_urls_resolves(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)

    def test_logout_url_resolves(self):
        url=reverse('search')
        self.assertEquals(resolve(url).func,search)

    def test_signup_url_resolves(self):
        url=reverse('alljobs')
        
        self.assertEquals(resolve(url).func,alljobs)        
    def test_school_url__resolves(self):
        url=reverse('jobinfo',args=['some-trila'])
        self.assertEquals(resolve(url).func,jobinfo)    