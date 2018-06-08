# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.shortcuts import reverse
from users.models import Profile
from datetime import datetime
from django.contrib.auth.models import User

class Post(models.Model):
	user = models.ForeignKey(Profile,null=True)
	title = models.CharField(max_length = 100)
	description = models.CharField(null = True,max_length=100)
	image = models.FileField(upload_to='documents/',null=True)
	
	def __str__(self):
		return str(self.title)
	def get_absolute_url(self):
		return reverse('post-list')
		
class Comment(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)
	comment = models.CharField(null=False,max_length=200)
	created_at = models.DateTimeField(default=datetime.now, blank=True,null=True)

	def get_success_url(self):
		return reverse_lazy('post-list')
	def get_absolute_url(self):
		return reverse('post-list')

class Like(models.Model):
    user = models.ForeignKey(Profile)
    post = models.ForeignKey(Post)
    created = models.DateTimeField(auto_now_add=True)
