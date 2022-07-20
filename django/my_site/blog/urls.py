from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name="index_page"),
    path('posts/', views.blog_posts, name="blog_posts_page"),
    path('post/<slug>', views.post_detail, name="post_detail_page")
]