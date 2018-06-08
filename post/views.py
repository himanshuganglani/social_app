from __future__ import unicode_literals
from django.shortcuts import render_to_response
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
from post.models import Profile

class PostList(LoginRequiredMixin,ListView):
    template_name = 'post/list.html'
    model = Post
    paginate_by = 3


class PostCreate(LoginRequiredMixin,CreateView):
    template_name = 'post/create.html'
    model = Post
    fields = ('title','description','image','user')
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



def commentcreate(request,pk):
    records = Comment.objects.all()
    post_data = Post.objects.filter(id=pk)
    comment_data = Comment.objects.filter(post__id=pk).values('comment')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return render(request,'post/list.html')
        else:
            return render(request, 'post/partial_comment.html',{'form': form , 'post_data':post_data,'comment_data':comment_data,},)
    else:       
        form = CommentForm()
        return render(request, 'post/partial_comment.html', {'form' : form ,'post_data':post_data,'comment_data':comment_data,})


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
        print count-1
        return HttpResponseRedirect("/post/list")


