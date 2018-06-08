from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime 
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class FriendRequest(models.Model):
    PENDING = 'pending'
    FINISH = 'finish'
    STATUS = ((PENDING, _('Pending')), 
        (FINISH, _('Finish')))
    user_id = models.IntegerField(null= True)
    friend_id = models.IntegerField(null= True)
    status = models.CharField(max_length=20, default=PENDING, null=False, blank=False)
    send_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
		return str(self.user)
