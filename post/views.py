# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post,Comment,Like
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CommentForm

class PostList(LoginRequiredMixin,ListView):
    template_name = 'post/list.html'
    model = Post
    paginate_by = 3


class PostCreate(LoginRequiredMixin,CreateView):
    template_name = 'post/create.html'
    model = Post
    fields = ('title','description','image',)
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

class CommentCreate(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentForm
    # initial = {'key': 'value'}
    template_name = 'comment.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/post/list')

        return render(request, self.template_name, {'form': form})





# # return HttpResponseRedirect("/post/list")

# def get_success_url(self):
#         return reverse_lazy('post-list')


# def add_record(request,pk):
#     records = Comment.objects.all()
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         import pdb
#         pdb.set_trace()
#         if form.is_valid():
#             add_record = form.save(commit=False)
#             add_record.save()
#         return HttpResponseRedirect("/post/list")
#     else:
#         form = CommentForm()
#         return HttpResponseRedirect("/post/list")

# def render_data(request):
#     records = Comment.objects.all()
#     return render(request, '/post/list.html', {"records": records})

def like_count(request,pk):
    current_user = request.user
    social_user = request.user.social_auth.filter(
    provider='facebook',).first()

    if request.user.is_authenticated():
        # import pdb
        # pdb.set_trace()
        like_data = Like.objects.filter(user_id=current_user.id,post__id=pk)
        if not like_data :
            like_data = Like.objects.create(user_id=current_user.id,post_id=pk).save()
            print 'abc'
        else:
            count = like_data.count()
            print count
        return HttpResponseRedirect("/post/list")

def dislike_count(request,pk):
    current_user = request.user
    like_data = Like.objects.filter(user_id=current_user.id,post__id=pk)
    if not like_data :
        pass
    else:
        count = like_data.count()
        return render_to_response('post/list.html', count)
        print count-1
        return HttpResponseRedirect("/post/list")


