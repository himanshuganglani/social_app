# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class PostList(LoginRequiredMixin,ListView):
    template_name = 'post/list.html'
    model = Post
    paginate_by = 3


class PostCreate(LoginRequiredMixin,CreateView):
    template_name = 'post/create.html'
    model = Post
    fields = '__all__'
    def form_valid(self,form):
        save_image = Post(image=self.get_form_kwargs().get('files')['image'])
        save_image.save()
        self.id = save_image.id
        return HttpResponseRedirect("/") 

class PostDetail(UpdateView):
	template_name = 'post/detail.html'
	model = Post


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('post-list')