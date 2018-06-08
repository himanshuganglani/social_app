from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from post.models import Profile
from django.contrib.auth.models import User

# class PostList(LoginRequiredMixin,ListView):
#     template_name = 'friends/list.html'
#     model = User

#     def get_queryset(self,pk):
#       	object_list = User.objects.exclude(id= u'pk')
#     	retutn object_list

def friendlist(request,pk):
    object_list = User.objects.exclude(id= u'pk')
    Print object_list
    return render(request, 'friends/list.html',{'object_list':object_list,},)
    

