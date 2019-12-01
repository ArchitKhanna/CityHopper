from django.contrib import admin
from .models import Profile
from .models import Contact

#registering profile and contact form in order for admin to use
admin.site.register(Profile)
admin.site.register(Contact)
