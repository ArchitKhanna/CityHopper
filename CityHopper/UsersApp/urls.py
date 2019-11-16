from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='cityhopper-register'),
    path('profile/', views.profile, name='cityhopper-userprofile'),
    path('booking/', views.booktickets, name='blog-booking'),
]
