from django.shortcuts import render,get_object_or_404
from .models import Blog,Category

def blogs_by_category(request, category_id):
    posts = Blog.objects.filter(status="Published",category=category_id).order_by('-updated_at')
    
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return render(request, '404.html')
    
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blogs_by_category.html', context)

def blog_page(request,slug):
    single_blog = get_object_or_404(Blog,slug=slug,status="Published")
    
    context ={
        'single_blog': single_blog
    }
    return render(request, 'blog.html',context)