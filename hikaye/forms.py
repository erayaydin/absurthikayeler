from django import forms
from django.conf import settings
from django.contrib.auth.models import User

from .models import Book

class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'content', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Başlık'}),
            'content': forms.Textarea(attrs={'data-provide': 'markdown'}),
            'categories': forms.SelectMultiple()
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'data-provide': 'markdown'}),
        }