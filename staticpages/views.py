from django.shortcuts import render
from django.shortcuts import render
from .models import Post, Category

def home(request):
    posts = Post.objects.all()
    event_categories = Category.objects.all()  
    context = {
        'posts': posts,
        'event_categories': event_categories,
    }
    return render(request, 'staticpages/home.html', context)

def about(request):
    return render(request, 'staticpages/about.html')