from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='cityhopper-register'),
    path('profile/', views.profile, name='cityhopper-userprofile'),
    path('booking/', views.booktickets, name='cityhopper-booking'),
    path('timetable/', views.timetable, name='cityhopper-timetable'),
]
