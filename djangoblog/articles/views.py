from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from . import forms
from .models import Article


def user_list(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, 'articles/article_manage.html', {'articles': articles})

def article_delete(request, slug):
    Article.objects.get(slug=slug).delete()
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})

def article_edit(request, id=None):
    instance = get_object_or_404(Article, id=id)
    form = forms.CreateArticle(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('articles:user_list')
    context = {
        'form':form,
        'title': instance.title,
        'body' : instance.body,
        'slug' : instance.slug,
        'thumb' : instance.thumb,
        'id' : id,
        'article': instance,
    }
    return render(request, 'articles/article_edit.html', context)

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})