from django.urls import path
from django.conf.urls import url, include
from . import views
from qr_code import urls as qr_code_urls

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
    path('qr/', views.qr, name='cityhopper-qr'),
    url(r'^qr_code/', include(qr_code_urls, namespace="qr_code")),
    path('payment/', views.payments, name='cityhopper-payment'),
]
