from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver

from .models import Student, Organizer


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff:
            Organizer.objects.create(user=instance)
        else:
            Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if instance.is_staff:
        instance.organizer.idno = instance.username
        instance.organizer.save()
        try:
            organizer_group = Group.objects.get(name='organizers')
        except:
            organizer_group = Group(name='organizers')
            organizer_group.save()

        organizer_group.user_set.add(instance)
        
    else:
        instance.student.idno = instance.username
        instance.student.save()
