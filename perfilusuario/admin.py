from django.contrib import admin
from .models import Profile, create_user_profile, save_user_profile

# Register your models here.
admin.site.register(Profile)