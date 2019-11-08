from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='cityhopper-register'),
    #path('home/', views.home, name='cityhopper-home'),
]
