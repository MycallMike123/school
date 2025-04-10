from django.contrib import admin
from .models import UserProfile, Student, Teacher, Subject, ExamResult


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('admission_no', 'full_name', 'stream', 'kcpe_year', 'kcpe_marks')
    list_filter = ('stream', 'kcpe_year', 'home_county')
    search_fields = ('admission_no', 'full_name', 'parent_name', 'parent_contact')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id')
    search_fields = ('user__username', 'employee_id')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'code')
    search_fields = ('subject_name', 'code')


@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'teacher', 'percentage', 'exam_date')
    list_filter = ('subject', 'teacher', 'exam_date')
    search_fields = ('student__full_name', 'subject__subject_name')