from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime 
from django.template.defaultfilters import date

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    full_name = models.CharField(default=False,max_length=25)
    birthday = models.DateField(blank=True, null=True)
    image_url = models.FileField(upload_to='profilepics/',null=True)
    provider = models.CharField(max_length=50)
    # other fields...
    def __str__(self):
		return str(self.user)

    

    # @property
    # def lifespan(self):
    #     return '%s - present' % date(self.birthdate, "n/j/Y")
# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()

