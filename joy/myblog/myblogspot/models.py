from django.db import models
from django.conf import settings

from django.urls import reverse
from django.db.models.signals import pre_save

User = settings.AUTH_USER_MODEL

# Create your models here
POST_STATUS = (
    ('published', 'Published'),
    ('draft', 'Draft'),
    ('hidden', 'Hidden'),
)

class Index(models.Model):
    heading = models.CharField(max_length=150)
    sub_heading = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.heading)
class Tag(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    title                   = models.CharField(max_length=120)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)


class Category(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    title                   = models.CharField(max_length=120)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)


class Post(models.Model):
    STATUS_CHOICES = (('publishsed', 'Published'), ('draft', 'Draft'), ('hidden', 'Hidden'),)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)
    banner_photo = models.ImageField(upload_to = 'static/media')
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Index, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=10, choices=POST_STATUS, default='draft')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.text)


# class Profile(models.Model):
#     user                    = models.OneToOneField(User, on_delete=models.CASCADE)
#     picture                 = models.ImageField(upload_to='media')
#     first_name              = models.CharField(max_length=255)
#     middle_name             = models.CharField(max_length=255)
#     last_name               = models.CharField(max_length=255)

#     def __str__(self):
#         return '{} {} {}'.format(
#                             self.first_name,
#                             self.middle_name,
#                             self.last_name
#                         )

# def rl_pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)

# pre_save.connect(rl_pre_save_receiver, sender=Post)
# pre_save.connect(rl_pre_save_receiver, sender=Category)
# pre_save.connect(rl_pre_save_receiver, sender=Tag)
# pre_save.connect(rl_pre_save_receiver, sender=Comment)
