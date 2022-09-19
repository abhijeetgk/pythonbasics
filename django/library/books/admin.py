import imp
from django.contrib import admin

# Register your models here.
from .models import Book, Author, Publisher, Format, Genere

class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_filter = ('author','publisher','genere')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher)
admin.site.register(Format)
admin.site.register(Genere);

