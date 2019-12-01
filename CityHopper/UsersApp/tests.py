from django.test import TestCase
from django.utils import timezone
from django.test import Client
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import *
from .forms import *

#The test classes and cases for automated testing

#This is the test class to check user authentication componets
class UserAuthenticationTest(TestCase):

    #Test existing user login with correct credentials
    def test_login_success_with_correct_details(self):

        #The setup method adds test data to the DB
        def setUp(self):
            User = get_user_model()
            user = User.objects.create_user('temporary', 'abc@company.com', 'temporary')

        #The test method runs the test with the data provided
        def test_login_success(self):
            User = get_user_model()
            self.client.login(username='temporary', password='temporary')
            response = self.client.get('/home/', follow=True)
            user = User.objects.get(username='temporary')
            #Assertion
            self.assertEqual(response.context['email'], 'abc@company.com')

        #Django provides the ability to make our own destroy method but also has
        # a default destroy method that runs at the end of each test

    #Test existing user login with incorrect credentials
    def test_login_fail_with_incorrect_details(self):

        #The setup method adds test data to the DB
        def setUp(self):
            User = get_user_model()
            user = User.objects.create_user('temporary', 'abc@company.com', 'temporary')

        #The test method runs the test with the data provided
        def test_login_fail(self):
            User = get_user_model()
            self.client.login(username='temporary', password='tempor')
            response = self.client.get('/login/', follow=True)
            user = User.objects.get(username='temporary')
            #Assertion
            self.assertEqual(response.context['email'], '')

    #Test user registration fail for new user
    def test_user_register_fail(self):

            User = get_user_model()
            #provide incomplete data
            user = User.objects.create_user('temporary', 'abc@company.com', '')
            response = self.client.get('/register/', follow=True)

class UsabilityTestsForForms(TestCase):
#Testing the contact form

#checking if contact is sucessful
    def test_contact_successful(self):
        form = contactForm(data={'user_name': "ARCHIE",
                                 'first_name': "Archit",
                                 'last_name': "Khana",
                                 'age': 6,
                                 'email': "archi@archertd.com",
                                 'message': "Hello world!"})
        self.assertTrue(form.is_valid())

#checking id contact is not sucessful
    def test_contact_Not_successful(self):
        form = contactForm(data={'user_name': "",
                                'first_name': "Archit",
                                'last_name': "Khana",
                                'age': 6,
                                'email': "archi:archertd.com",
                                'message': "Hello world!"})
        self.assertFalse(form.is_valid())

#Testing user registration
    def test_registrationTest(self):
       User = get_user_model()
       user = User.objects.create_user('tempory', 'abc@company.com',  '')

       #Testing reg sucessful
       def test_userReg_sucessful(self):
        User = get_user_model()
        form = UserRegisterForm(data={'username': "reebok12",
                                      'email': "daveod@davido.com",
                                      'password1': "davidBrom13",
                                      'password2': "davidBrom13",
                                      'mobile': 860541833,
                                      'address': "Willow Drive",
                                      'birthdate': 30/12/1998})
        self.assertFalse(form.is_valid())

    #Testing the booking form - successful
    def test_booking_sucessful(self):
            form = UserBookingForm(data={'startlocation': 'Limerick',
                                         'destination': 'Galway',
                                         'journeydate': '02/12/2020',
                                         'departuretime': '10:00:00' ,
                                         'journeytype': 'Single',
                                         'numberoftickets': 2})
            self.assertTrue(form.is_valid())

    #Testing the booking form - unsuccessful
    def test_booking_unsucessful(self):
            form = UserBookingForm(data={'startlocation': "",
                                         'destination': "Galway",
                                         'journeydate': '02/12/2012',
                                         'departuretime': '10' ,
                                         'journeytype': "Single",
                                         'numberoftickets': 2})
            self.assertFalse(form.is_valid())
