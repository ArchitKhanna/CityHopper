from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

#Specifying URL patterns for Django to resolve
urlpatterns = [
    #Home url
    path('', views.index, name='cityhopper-home'),
    #about page url
    path('about/', views.about, name='cityhopper-about'),
]
