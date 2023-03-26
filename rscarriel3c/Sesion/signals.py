from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_superuser(sender, instance, created, **kwargs):
    if created and instance.is_superuser == True:
        instance.is_staff = True
        instance.save()