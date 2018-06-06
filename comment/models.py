rom __future__ import unicode_literals
from django.db import models
from django.shortcuts import reverse
from users.models import Profile
from datetime import datetime    
from post.models import Post		

class Comment(models.Model):
	user = models.ForeignKey(Profile)
	post = models.ForeignKey(Post)
	comment = models.CharField(null=True,max_length=200)
	created_at = models.DateTimeField(default=datetime.now, blank=True)

	def get_success_url(self):
		return reverse_lazy('post-list')
