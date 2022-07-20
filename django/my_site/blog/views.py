from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request, 'blog/index.html')

def blog_posts(request):
    return render(request, 'blog/blog_posts.html')

def post_detail(request, slug):
    return render(request,'blog/post_detail.html')