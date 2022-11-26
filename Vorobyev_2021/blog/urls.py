from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index1, name="blog_index1"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
]