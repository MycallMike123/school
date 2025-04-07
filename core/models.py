from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

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
