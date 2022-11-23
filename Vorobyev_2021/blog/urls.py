from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index1'),
    path('', views.blog_detail, name='blog_detail'),
]