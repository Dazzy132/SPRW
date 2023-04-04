from posts.models.post import Post
from posts.models.comment import Comment

from django import forms


class MyAdminForm(forms.Form):
    select1 = forms.ModelChoiceField(queryset=Post.objects.all())
    select2 = forms.ModelChoiceField(queryset=Comment.objects.all())
