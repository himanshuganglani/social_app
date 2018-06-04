# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.shortcuts import reverse
class Post(models.Model):
	
	title = models.CharField(max_length = 100)
	description = models.CharField(null = True,max_length=100)
	image = models.FileField(upload_to='documents/',null=True)
	def __str__(self):
		return str(self.title)
	def get_absolute_url(self):
		return reverse('post-list')
		

	

		