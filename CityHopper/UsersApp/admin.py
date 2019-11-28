from django.contrib import admin

from .models import Profile
from .models import Contact

admin.site.register(Profile)
#registering profile and contact form in order for admin to use
admin.site.register(Contact)
# Register your models here.
