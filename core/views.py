from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm, StudentRegistrationForm, ExamResultForm
from .models import UserProfile, Student, Teacher
from django.contrib import messages
from django.db.models import Count

def home_view(request):
    return render(request, 'home.html')


# Custom login for all users
# After login, redirect based on the role e.g. Admin, Teacher, Parent
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user using Django's built-in system
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Optional: Redirect based on role
            if hasattr(user, 'userprofile'):
                role = user.userprofile.role
                if role == 'ADMIN':
                    return redirect('admin_dashboard')
                elif role == 'TEACHER':
                    return redirect('teacher_dashboard')
                elif role == 'PARENT':
                    return redirect('parent_dashboard')

            return redirect('login')  # fallback
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def LogoutUser(request):
    logout(request)
    return redirect('home')


# Only Admins can register new users (e.g., Teachers)
@login_required
def register_user(request):
    if not hasattr(request.user, 'userprofile') or request.user.userprofile.role != 'ADMIN':
        return redirect('unauthorized')  # Optional access denied page

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()

            # Set role via profile
            role = form.cleaned_data['role']
            profile = user.userprofile
            profile.role = role
            profile.save()

            return redirect('admin_dashboard')  # Redirect or success message
    else:
        form = RegisterUserForm()

    return render(request, 'register_user.html', {'form': form})


# Admin registers students (adds to DB only, not Django user model)
@login_required
def add_student(request):
    if not hasattr(request.user, 'userprofile') or request.user.userprofile.role != 'ADMIN':
        return redirect('unauthorized')

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Show a success message after successful registration
            messages.success(request, 'Student registered successfully!')
            # Redirect to the admin dashboard or any other page you want
            return redirect('add_student')
    else:
        form = StudentRegistrationForm()

    return render(request, 'add_student.html', {'form': form})


@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


@login_required
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')


@login_required
def parent_dashboard(request):
    return render(request, 'parent_dashboard.html')


def unauthorized(request):
    return render(request, 'unauthorized.html', status=403)


@login_required
def register_exam_result(request):
    if not hasattr(request.user, 'userprofile') or request.user.userprofile.role != 'TEACHER':
        messages.error(request, "Only teachers can register exam results.")
        return redirect('login')  # or your dashboard

    if request.method == 'POST':
        form = ExamResultForm(request.POST)
        if form.is_valid():
            exam_result = form.save(commit=False)
            exam_result.teacher = Teacher.objects.get(user=request.user)
            exam_result.save()
            messages.success(request, "Exam result recorded successfully.")
            return redirect('register_exam_result')
    else:
        form = ExamResultForm()

    return render(request, 'exam_result_form.html', {'form': form})


@login_required
def register_subject(request):
    if not hasattr(request.user, 'userprofile') or request.user.userprofile.role != 'ADMIN':
        return redirect('unauthorized')

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subject registered successfully.")
            return redirect('admin_dashboard')
    else:
        form = SubjectForm()

    return render(request, 'register_subject.html', {'form': form})



def stream_analysis(request):
    streams = Student.objects.values('stream').annotate(count=Count('id')).order_by('stream')
    return render(request, 'stream_analysis.html', {'streams': streams})


def students_by_stream(request, stream_name):
    students = Student.objects.filter(stream=stream_name)
    return render(request, 'dashboard/students_by_stream.html', {
        'students': students,
        'stream_name': stream_name
    })


def number_of_students(request):
    return render(request, 'number_of_students.html')

def number_of_teachers(request):
    return render(request, 'number_of_teachers.html')

def add_teacher(request):
    return render(request, 'add_teacher.html')

def streams(request):
    return render(request, 'streams.html')