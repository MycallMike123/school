from django.urls import path
from . import views

urlpatterns = [
    path('unauthorized/', views.unauthorized, name='unauthorized'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/teacher/', views.register_user, name='register_user'),
    path('register/student/', views.register_student, name='register_student'),
    # Add other views like dashboard, login, etc.
]
