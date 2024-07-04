from django.contrib import admin

# Register your models here.
from .models import Profile, Link

admin.site.register(Profile)
admin.site.register(Link)

