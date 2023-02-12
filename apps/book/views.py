from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book

from rest_framework import viewsets

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    gueryset = Book.objects.all()
    serializer_class = BookSerializer
