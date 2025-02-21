from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def set_is_staff_on_user_creation(sender, instance, created, **kwargs):
    if created:
        # If the user is newly created, set is_staff to True
        instance.is_staff = True
        instance.save()
