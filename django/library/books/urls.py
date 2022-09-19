from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books", views.books_listing, name="books_listing")
]
