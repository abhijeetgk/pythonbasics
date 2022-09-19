from django.contrib import admin

# Register your models here.
from .models import Post, Author, Tag

class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('first_name',)

admin.site.register(Post)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)