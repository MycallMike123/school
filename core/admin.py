from django.contrib import admin
from .models import UserProfile, Student, Teacher, Subject, ExamResult


# Register your UserProfile here so thar it appears in the Django Admin Panel
admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(ExamResult)
