from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog,Category
from django.db.models import Q

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

def blog_search(request):
    keyword = request.GET.get('keyword')
    
    if not keyword:
        return redirect('home')
    
    blogs = Blog.objects.filter(
        Q(title__icontains=keyword)|
        Q(short_description__icontains = keyword) | 
        Q(blog_body__icontains = keyword),
        status="Published")
    
    context = {
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search_results.html',context)