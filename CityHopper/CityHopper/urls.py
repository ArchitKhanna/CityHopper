"""CityHopper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#importing required components
from django.contrib import admin
from django.contrib.auth import views as auth_views # mabye here
from django.urls import path
from django.conf.urls import include, url
from UsersApp import views as user_views
from django.conf import settings
from django.conf.urls.static import static

#Specifying the main URL patterns for Django to resolve
urlpatterns = [
    #includes all urls from CityHopperApp
    path('CityHopperApp/', include('CityHopperApp.urls')),
    #includes all urls from UsersApp
    path('', include('UsersApp.urls')),
    #url for profile
    path('profile/', user_views.profile, name='profile'),
    #url for timetable
    path('timetable/', user_views.timetable, name='timetable'),
    #url for Admin page
    path('admin/', admin.site.urls),
    #url for new user registration
    path('register/', user_views.register, name='register'),
    #url for logout page
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    #url for user login page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True), name='login'),
    #url for ERD generator
    url(r'^plate/', include('django_spaghetti.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
