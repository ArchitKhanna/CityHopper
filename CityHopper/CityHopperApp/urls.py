from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='cityhopper-home'),
    #path('home/', views.home, name='cityhopper-home'),
    path('about/', views.about, name='cityhopper-about'),
]
