from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('categories/',views.categories,name='categories'),
    path('add-category/',views.add_category,name='add_category'),
    path('update-category/<int:id>/',views.update_category,name='update_category'),
    path('delete-category/<int:id>/',views.delete_category,name='delete_category'),
    path('blogs/',views.blogs,name='blogs'),
    path('add-blog/',views.add_blog,name='add_blog'),
    path('update-blog/<int:id>/',views.update_blog,name='update_blog'),
    path('delete-blog/<int:id>/',views.delete_blog,name='delete_blog'),
    
    # User Management
    path('users/',views.users,name='users'),
    path('add-user/',views.add_user,name='add_user'),
    path('update-user/<int:id>/',views.update_user,name='update_user'),
    path('delete-user/<int:id>/',views.delete_user,name='delete_user'),
    
]
