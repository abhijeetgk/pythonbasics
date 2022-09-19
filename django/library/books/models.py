from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Format(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Genere(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,  on_delete=models.CASCADE, related_name="authors")
    rating = models.IntegerField()
    edition = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="publisher")
    summary = models.TextField()
    length = models.CharField(max_length=50)
    format = models.ForeignKey(Format, on_delete=models.CASCADE, related_name="format")
    genere = models.ForeignKey(Genere, on_delete=models.CASCADE, related_name="genere")
    image_name = models.ImageField(upload_to="book_images", null=True)

    def __str__(self):
        return self.title

