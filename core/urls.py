from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('logout/', views.LogoutUser, name="logout"),
    path('unauthorized/', views.unauthorized, name='unauthorized'),
    path('login/', views.user_login, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('parent_dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('register/exam/', views.register_exam_result, name='register_exam_result'),
    path('register/subject/', views.register_subject, name='register_subject'),
    path('register/teacher/', views.register_user, name='register_user'),
    path('dashboard/stream-analysis/', views.stream_analysis, name='stream_analysis'),
    path('number_of_students/', views.number_of_students, name='number_of_students'),
    path('number_of_teachers/', views.number_of_teachers, name='number_of_teachers'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('streams/', views.streams, name='streams'),
    path('dashboard/students/stream/<str:stream_name>/', views.students_by_stream, name='students_by_stream'),
    # Add other views like dashboard, login, etc.
]
