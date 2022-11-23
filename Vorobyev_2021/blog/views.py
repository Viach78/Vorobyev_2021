from django.shortcuts import render
from .models import Post, Comment


# Create your views here.

def blog_index(request):
    blog = Post.objects.all()
    context = {
        "blog": blog
    }
    return render(request, 'blog_index1.html', context)


# def blog_detail(request, pk):
#     comment = Comment.objects.get(pk=pk)
#     context = {
#         "comment": comment
#     }
#     return render(request, 'blog_detail.html', context)

def blog_detail(request):
    return render(request, 'blog_detail.html')