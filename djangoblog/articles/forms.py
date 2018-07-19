from django import forms
from . import models

class CreateArticle(forms.ModelForm):

    id = forms.IntegerField()

    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb', 'id']
