from django.test import TestCase
from .models import Users
# Create your tests here.
from django.test import TestCase

class TestModel(TestCase):
    def test_should_create_user(self):  # start one test
        contact = Users(name='John')  # create a Contact object with 2 params like that
        self.assertEquals(
            str(contact),  
            'John',
        )