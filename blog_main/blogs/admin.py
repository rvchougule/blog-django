from django.contrib import admin
from .models import Category,Blog

# Register your models here.

class  BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','author','status','is_featured','created_at')
    search_fields = ('id','title','author__username','category__category_name')
    list_editable = ('is_featured',)

admin.site.register(Category)

admin.site.register(Blog,BlogAdmin)
