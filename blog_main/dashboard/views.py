
from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Blog,Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogForm
from django.contrib import messages
from django.core.paginator import Paginator


@login_required(login_url='login')
def dashboard(request):
    blogs_count = Blog.objects.all().count()
    categories_count = Category.objects.all().count()
    context = {
        'blogs_count': blogs_count,
        'categories_count': categories_count,
    }
    return render(request, 'dashboard/dashboard.html',context)

def categories(request):
    return render(request, 'dashboard/categories.html')

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully')
            return render(request, 'dashboard/categories.html')
    else:
        form = CategoryForm()
        
    context = {
        'form':form
    }
    return render(request, 'dashboard/add_category.html',context)

def update_category(request,id):
    category = get_object_or_404(Category,id=id)    
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully')
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
        
    context = {
        'form':form,
        'category':category
    }
        
    return render(request, 'dashboard/update_category.html',context)

def delete_category(request,id):
    category = get_object_or_404(Category,id=id)
    category.delete()
    messages.success(request, 'Category deleted successfully')
    return redirect('categories')

def blogs(request):
    blogs = Blog.objects.filter(status="Published",author=request.user).order_by('-created_at')

    context = {
        'blogs': blogs
    }
    return render(request, 'dashboard/blogs.html',context)

def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        print(form )
        print(request.FILES)

        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, 'Blog added successfully')
            return redirect('blogs')
    else:
        form = BlogForm()
    
    context = {
        'form':form
    }
    return render(request, 'dashboard/add_blog.html',context)

def update_blog(request,id):
    blog = get_object_or_404(Blog,id=id)
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog updated successfully')
            return redirect('blogs')
    else:
        form = BlogForm(instance=blog)

    context = {
        'form':form,
        'blog':blog
    }
    return render(request, 'dashboard/update_blog.html',context)

def delete_blog(request,id):
    blog = get_object_or_404(Blog,id=id)
    blog.delete()
    messages.success(request, 'Blog deleted successfully')
    return redirect('blogs')
    
