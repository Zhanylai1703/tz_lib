from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Tag
from .serializers import CategorySerializer, TagSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer