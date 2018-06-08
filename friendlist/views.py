from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.shortcuts import render
# from post.models import Post,Comment,Like
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from post.models import Profile
from django.contrib.auth.models import User
from .models import FriendRequest

    
def friendlist(request,pk):
    object_list = User.objects.exclude(id=pk)
    return render(request, 'friends/list.html',{'object_list':object_list,},)

def sendrequest(request,pk):
	user_id = request.user.id
	data = FriendRequest.objects.create(user_id=user_id,friend_id=pk).save()
	print data
	
	return HttpResponseRedirect("/post/list")