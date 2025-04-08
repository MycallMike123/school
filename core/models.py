from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# This model extends the built-in User model by associating each user with a role

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('TEACHER', 'Teacher'),
        ('PARENT', 'Parent')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES) # Role field


    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Automatically create a UserProfile whenever a new user is created.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# Save the UserProfile when the user is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


# Student model in DB
class Student(models.Model):
    STREAMS = [
        ('1A', '1A'), ('1B', '1B'), ('2A', '2A'), ('2B', '2B'),
        ('3A', '3A'), ('3B', '3B'), ('4A', '4A'), ('4B', '4B')
        ]

    admission_no = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=100)
    stream = models.CharField(max_length=2, choices=STREAMS, null=True)  # Like class or stream
    kcpe_marks = models.IntegerField()
    kcpe_year = models.IntegerField()
    parent_name = models.CharField(max_length=100)
    parent_contact = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)
    home_county = models.CharField(max_length=50, null=True, blank=True)
    primary_school = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.admission_no})"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)


    def __str__(self):
        return f"{self.full_name} ({self.admission_no})"


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
