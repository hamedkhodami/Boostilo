from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import ProfileTeam,AccessControl

@receiver(post_save, sender=User)
def create_user_profile_and_access(sender,instance,created,**kwargs):
    if created:
        ProfileTeam.objects.create(user=instance,fullname=instance.username)
        AccessControl.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile_and_access(sender,instance,**kwargs):
    if hasattr(instance,'profile'):
        instance.profile.save()
    if hasattr(instance, 'access_control'):
        instance.access_control.save()