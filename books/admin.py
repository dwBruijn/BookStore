from django.contrib import admin
from .models import Book, Order, Request

admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Request)