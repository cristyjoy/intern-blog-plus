from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.conf import settings

User = settings.AUTH_USER_MODEL



# Create your models here.

class Myself(models.Model):
    user                  = models.OneToOneField(User, on_delete=models.CASCADE)
    activation_key        = models.CharField(max_length=150, blank=True, null=True)
    activated             = models.BooleanField(default=False)
    timestamp             = models.DateTimeField(auto_now_add=True)
    updated               = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
       return u'/some_url/%d' % self.id


class Profile(models.Model):
    user                    = models.OneToOneField(User, on_delete=models.CASCADE)
    picture                 = models.ImageField(upload_to='media')
    first_name              = models.CharField(max_length=255)
    middle_name             = models.CharField(max_length=255)
    last_name               = models.CharField(max_length=255)

    def __str__(self):
        return '{} {} {}'.format(
                            self.first_name,
                            self.middle_name,
                            self.last_name
                        )

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)





