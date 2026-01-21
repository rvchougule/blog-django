from django.shortcuts import render,redirect
from blogs.models import Blog, Category
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    
    featured_blogs = Blog.objects.filter(is_featured=True).order_by('-updated_at')[:3]
    
    posts = Blog.objects.filter(is_featured=False,status="Published").order_by('-created_at')
    
    context = {
        'featured_blogs': featured_blogs,
        'posts':posts
        }
    return render(request, 'home.html', context)

    
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:    
        form = RegistrationForm()
    
    context = {
        'form':form
    }
    return render(request, 'register.html',context)

def login_view(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = auth.authenticate(username=username,password=password)
            
            if user is not None:
                auth.login(request,user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    
    context = {
        'form':form
    }
    
    return render(request, 'login.html',context)

def logout_view(request):
    auth.logout(request)
    return redirect('home')