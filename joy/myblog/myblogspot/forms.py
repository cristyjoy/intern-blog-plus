from django import forms
from .models import Post, Comment, Tag, Category
# Register your models here.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post', 'author',)
        fields = (
        'post',
        'content',
        'author')
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'sub_title',
            'banner_photo',
            'tags',
            'category',
            'body',
            'status'
        ]

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            'title'
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title'
        ]
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = (
#                 'picture',
#                 'first_name',
#                 'middle_name',
#                 'last_name'
#             )
