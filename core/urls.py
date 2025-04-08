from django.urls import path
from . import views

urlpatterns = [
    path('unauthorized/', views.unauthorized, name='unauthorized'),
    path('login/', views.user_login, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('register-exam/', views.register_exam_result, name='register_exam_result'),
    path('register-subject/', views.register_subject, name='register_subject'),
    path('register/teacher/', views.register_user, name='register_user'),
    path('register/student/', views.register_student, name='register_student'),
    # Add other views like dashboard, login, etc.
]
