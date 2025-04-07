from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterUserForm, StudentRegistrationForm
from .models import UserProfile, Student


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

            return redirect('dashboard')  # fallback
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# Only Admins can register new users (e.g., Teachers)
@login_required
def register_user(request):
    if request.user.userprofile.role != 'ADMIN':
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

            return redirect('dashboard')  # Redirect or success message
    else:
        form = RegisterUserForm()

    return render(request, 'register_user.html', {'form': form})


# Admin registers students (adds to DB only, not Django user model)
@login_required
def register_student(request):
    if request.user.userprofile.role != 'ADMIN':
        return redirect('unauthorized')

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentRegistrationForm()

    return render(request, 'register_student.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def unauthorized(request):
    return render(request, 'unauthorized.html', status=403)
