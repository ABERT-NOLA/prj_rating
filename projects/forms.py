from django import forms
from .models import Comment, Post, Rating

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']