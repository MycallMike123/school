from django.contrib import admin
from .models import UserProfile


# Register your UserProfile here so thar it appears in the Django Admin Panel
admin.site.register(UserProfile)
