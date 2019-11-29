from django.urls import path
from django.conf.urls import url, include
from . import views
from qr_code import urls as qr_code_urls

urlpatterns = [
    path('register/', views.register, name='cityhopper-register'),
    #register page url
    path('profile/', views.profile, name='cityhopper-userprofile'),
    #booking page url
    path('booking/', views.booktickets, name='cityhopper-booking'),
    #timetable page url
    path('timetable/', views.timetable, name='cityhopper-timetable'),
    #home page url
    path('home/', views.home, name='cityhopper-home'),
    #offers page url
    path('offers/', views.offers, name='cityhopper-offers'),
    #latest news page url
    path('news/', views.news, name='cityhopper-news'),
    #contact page URL
    path('contact/', views.contact, name='cityhopper-contact'),
    #adminLink page url
    path('adminLink/', views.adminLink, name='cityhopper-adminLink'),
    #qr page
    path('qr/', views.qr, name='cityhopper-qr'), #Could be this as well, not sure
    #qr code package
    url(r'^qr_code/', include(qr_code_urls, namespace="qr_code")),
    #google analytics package
    url(r'^djga/', include('google_analytics.urls')),
    #Stripe payment page, defined as a view as it is class based...
    path('payment/', views.payment.as_view(), name='cityhopper-payment'),
    #payment confirmation page..
    path('paymentConfirmation/', views.paymentConfirmation, name='paymentConfirmation'),
]
