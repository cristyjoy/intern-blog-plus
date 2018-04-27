from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View, generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import (CommentForm, CategoryForm, TagForm, PostForm)
from .models import Post, Index, Category, Tag, Comment

class PostDetailView(View):

    def get(self, request, title, *args, **kwargs):
         post = get_object_or_404(Post, title=title, status='published')
         comment = post.comment_set.all()
         context = {'post':post,'comment': comment,}

         return render(request, "post_detail.html", context)

def comment(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('/posts')
    else:
        form = CommentForm()
        context = {
        'form': form,
    }
    return render(request, 'comment.html', context)

    def get_object(self):
        title = self.kwargs.get("title")
        if title is None:
            raise Http404
        return get_object_or_404(Post, title__iexact=title)

class PostView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        post = Post.objects.all().order_by('-date_created')
        context = {
            'object_list':post,
        }
        return render(request, "post_list.html", context)

def Draft(request):
    post = Post.objects.filter(status__contains='draft')
    context = {'object_list': post,}
    return render(request, 'post_list.html', context)

def Hidden(request):
    post = Post.objects.filter(status__contains='Hidden')
    context = {'object_list': post,}
    return render(request, 'post_list.html', context)

class PostCreateView(LoginRequiredMixin, View):
    form_class = PostForm
    initial = {'key': 'value'}
    template_name = 'post_edit.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog:post-detail', title = post.title)
        else:
            form = PostForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
# def  post_edit(request, title):
#     post_user = Post.objects.filter(user=request.user)
#     # post = get_object_or_404(Post, title=title)
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save()
#             return redirect('posts:post-detail', title=title)
#     else:
#         form = PostForm(instance=post)
#     context = {
#         'form': form,
#     }
#     return render(request, 'post_edit.html', context)

# class ProfileDetailView(View):
#     def get(self, request, username, *args, **kwargs):
#         profile_detail = get_object_or_404(User, username__iexact=username)
#         post_list = profile_detail.post_set.filter(user=self.request.user, status='published')
#         paginator = Paginator(post_list, 10)
#         page = request.GET.get('page')
#         try:
#             post = paginator.page(page)
#         except PageNotAnInteger:
#             post = paginator.page(1)
#         except EmptyPage:
#             post = paginator.page(paginator.num_pages)
#         context = {
#             'profile_detail': profile_detail,
#             'post': post,
#         }
#         return render(request, 'profile_detail.html', context)
