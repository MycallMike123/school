from django import forms
from django.contrib.auth.models import User
from core.models import UserProfile, Student


# Generic user Registration form
class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES)


    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['admission_no', 'full_name', 'stream', 'kcpe_marks',
                  'kcpe_year', 'parent_name', 'parent_contact',
                  'date_of_birth', 'home_county', 'primary_school']


    def clean_kcpe_marks(self):
        marks = self.cleaned_data.get("kcpe_marks")
        if marks < 0 or marks > 500:
            raise forms.ValidationError("KCPE Marks must be between 0 and 500.")
        return marks
