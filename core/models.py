from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime
from django.core.validators import RegexValidator

# This model extends the built-in User model by associating each user with a role

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('TEACHER', 'Teacher'),
        ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES) # Role field


    def __str__(self):
        return f"{self.user.username} - {self.role}"
        
# Student model in DB
class Student(models.Model):
    STREAMS = [
        ('1A', '1A'), ('1B', '1B'), ('2A', '2A'), ('2B', '2B'),
        ('3A', '3A'), ('3B', '3B'), ('4A', '4A'), ('4B', '4B')
    ]

    admission_no = models.CharField(max_length=10, unique=True, blank=True)
    full_name = models.CharField(max_length=30)
    stream = models.CharField(max_length=2, choices=STREAMS)  # Now required
    kcpe_marks = models.IntegerField()
    kcpe_year = models.IntegerField(
        max_length=4,
        validators=[RegexValidator(r'^\d{4}$', 'Enter a valid 4-digit year')],
        blank=False,  # Ensures it's required
    )
    parent_name = models.CharField(max_length=30)
    
    # Ensure parent's contact is exactly 10 digits
    parent_contact = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit contact number')],
        blank=False,  # Ensures it's required
    )

    date_of_birth = models.DateField()  # Now required
    home_county = models.CharField(max_length=10)  # Now required
    primary_school = models.CharField(max_length=50)  # Now required

    def save(self, *args, **kwargs):
        if not self.admission_no:
            year = datetime.now().year
            last_student = Student.objects.filter(admission_no__startswith=str(year)).order_by('admission_no').last()
            next_num = int(last_student.admission_no[-3:]) + 1 if last_student else 1
            self.admission_no = f"{year}{next_num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.admission_no})"
        
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.employee_id:
            last = Teacher.objects.all().order_by('id').last()
            last_num = int(last.employee_id[3:]) + 1 if last and last.employee_id.startswith("EMP") else 1
            self.employee_id = f"EMP{last_num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        full_name = self.user.get_full_name() or self.user.username
        return f"{full_name} ({self.employee_id})"


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.subject_name} ({self.code})"


class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    score_obtained = models.PositiveIntegerField()
    out_of = models.PositiveIntegerField()
    percentage = models.PositiveIntegerField(editable=False)

    exam_date = models.DateField()

    class Meta:
        unique_together = ('student', 'subject', 'exam_date')

    def save(self, *args, **kwargs):
        if self.out_of > 0:
            self.percentage = int((self.score_obtained / self.out_of) * 100)
        else:
            self.percentage = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.full_name} - {self.subject.subject_name}: {self.percentage}%"
        