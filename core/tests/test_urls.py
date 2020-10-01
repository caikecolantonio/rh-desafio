from django.test import TestCase
from django.urls import reverse, resolve
from core.views import ProcessCreate



class TestUrls(TestCase):

    def test_process_create_url_works(self):
        url = reverse('process_list')
        self.assertEquals(resolve(url).func , ProcessCreate)