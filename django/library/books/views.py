from django.shortcuts import render

# Create your views here.
def index(request):
    return render(
        request,
        'books/index.html',
        {}
    )

def books_listing(request):
    return  render(
        request,
        'books/books_listing.html',
        {}
    )