from django.shortcuts import render
from blogs.models import Blog, Category

def home(request):
    
    featured_blogs = Blog.objects.filter(is_featured=True).order_by('-updated_at')[:3]
    
    posts = Blog.objects.filter(is_featured=False,status="Published").order_by('-created_at')
    
    context = {
        'featured_blogs': featured_blogs,
        'posts':posts
        }
    return render(request, 'home.html', context)