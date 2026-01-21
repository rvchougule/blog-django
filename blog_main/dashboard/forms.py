from django.forms import ModelForm
from blogs.models import Category,Blog

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
        
class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title','category','featured_image','short_description','blog_body','status','is_featured']