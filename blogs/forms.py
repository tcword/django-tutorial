from django import forms
from .models import Blog

class BlogForm(forms.Form):
    # Form to create/update a blog instance
    class Meta:
        model = Blog

    title = forms.CharField(max_length=100, label="Title of Blog")
    description = forms.CharField(label="Description of Blog")