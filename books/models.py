from django.conf import settings
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512, default=None)
    author = models.CharField(max_length=64)
    price = models.FloatField(default=0.0, null=True, blank=True)
    image = models.ImageField(upload_to="cover_images", default=None)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, blank=True, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title


class Request(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    book_title = models.CharField(max_length=128)
    book_author = models.CharField(max_length=64)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_title

