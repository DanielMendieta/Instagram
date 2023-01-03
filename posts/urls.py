from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts, name="posts"),
    path ('create-post/', views.create_post, name="create-post"),
    path ('edit-post/<str:pk>/', views.edit_post, name= "edit-post"),
    path ('delete-post/<str:pk>/', views.delete_post, name= "delete-post"),
]