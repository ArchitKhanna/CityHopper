from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='cityhopper-register'),
    path('profile/', views.profile, name='cityhopper-userprofile'),
    path('booking/', views.booktickets, name='cityhopper-booking'),
    path('timetable/', views.timetable, name='cityhopper-timetable'),
    path('home/', views.home, name='cityhopper-home'),
    path('offers/', views.offers, name='cityhopper-offers'),
    path('news/', views.news, name='cityhopper-news'),
    path('contact/', views.contact, name='cityhopper-contact'),
    path('adminLink/', views.adminLink, name='cityhopper-adminLink'),
]
