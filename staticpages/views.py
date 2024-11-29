from django.shortcuts import render
from django.shortcuts import render
from post.models import Post, Category

def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()  
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'staticpages/home.html', context)

def about(request):
    return render(request, 'staticpages/about.html')