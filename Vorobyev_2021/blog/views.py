from django.shortcuts import render
from .models import Post, Comment


# Create your views here.

def blog_index1(request):
    posts = Post.objects.all().order_by('-create_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index1.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog_detail.html", context)
