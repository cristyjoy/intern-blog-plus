from django import forms
from .models import Post, Comment
# Register your models here.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post', 'author',)
        fields = (
        'post',
        'content',
        'author')
