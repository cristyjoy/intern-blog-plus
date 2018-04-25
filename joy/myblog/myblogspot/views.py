from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views import View, generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import CommentForm
from .models import Post, Index, Category, Tag, Comment

class PostDetailView(View):

    def get(self, request, title, *args, **kwargs):
         post = get_object_or_404(Post, title=title, status='published')
         comment = post.comment_set.all()
         context = {'post':post,'comment': comment,}

         return render(request, "post_detail.html", context)

    def comment(request):
         if request.method == 'POST':
            form = CommentForm(request.POST)
         if form.is_valid():
           comment = form.save(commit=False)
           comment.save()
           return redirect('/posts')
         else:
            form = CommentForm()
            context = {
             'form': form,
         }
         return render(request, 'myblogspot/comment.html', context)

class PostView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        post = Post.objects.all().order_by('-date_created')
        context = {
            'object_list':post,
        }
        return render(request, "post_list.html", context)

