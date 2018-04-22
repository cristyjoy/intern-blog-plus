from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views import View, generic


from .models import Post, Index, Category, Tag,Comment

class PostDetailView(View):

    def get(self, request, post_id, *args, **kwargs):
         post = Post.objects.filter(pk=post_id).order_by('-date_created')
         context = {
            'object_list':post,
        }
         return render(request, "post_detail.html", context)

class PostView(View):

    def get(self, request, *args, **kwargs):
         post = Post.objects.all().order_by('-date_created')
         context = {
            'object_list':post,
        }
         return render(request, "post_list.html", context)
