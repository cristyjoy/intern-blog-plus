"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .import views

from .views import (
    PostDetailView,
    PostView,
    PostCreateView
    )

app_name = 'myblogspot'

urlpatterns = [
    path('detail/<title>/', PostDetailView.as_view(), name='post_detail'),
    path('', PostView.as_view(), name='post-list'),
    path('<int:pk>/', views.comment, name='post-comment'),
    path('draft/', views.Draft, name='draft'),
    path('hidden/', views.Hidden, name='hidden'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('edit/<title>/', views.post_edit, name='post-edit'),
    #path('profile/<username>/', ProfileDetailView.as_view(), name='profile')
]
