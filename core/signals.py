from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, Teacher  # + ParentProfile, AdminProfile if defined

# Automatically create a UserProfile whenever a new user is created.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Save the UserProfile when the user is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

@receiver(post_save, sender=UserProfile)
def create_role_related_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'TEACHER' and not hasattr(instance.user, 'teacher'):
            Teacher.objects.create(user=instance)
        elif instance.role == 'PARENT' and not hasattr(instance.user, 'parentprofile'):
            ParentProfile.objects.create(user=instance)
        elif instance.role == 'ADMIN' and not hasattr(instance.user, 'adminprofile'):
            AdminProfile.objects.create(user=instance)