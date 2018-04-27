from django.contrib.auth import get_user_model
from .forms import RegisterForm


from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

User = get_user_model()
# Create your views here.

class RegisterView(CreateView):
   form_class = RegisterForm
   template_name = 'registration/register.html'
   success = '/accounts/login'
