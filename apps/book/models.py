from django.db import models
from apps.categories.models import Category, Tag
from apps.accounts.models import User

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(
        max_length=255, blank=True, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='book_category', verbose_name='category')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    book_tags = models.ManyToManyField(Tag, related_name='book_tags') 


    def __str__(self) -> str:
        return f'{self.book_name} - {self.author}'   
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['-id']
