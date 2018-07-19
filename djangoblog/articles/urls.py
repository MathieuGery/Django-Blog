from django.urls import path
from django.conf.urls import url
from . import views

app_name='articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    path('user_lsit/', views.user_list, name="user_list"),
    path('create/', views.article_create, name="create"),
    path('delete/<slug:slug>/', views.article_delete, name="delete"),
    path('edit/<int:id>/', views.article_edit, name="edit"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]