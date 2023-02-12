
from django.db import models





class User(models.Model):
    name = models.CharField(
        max_length=255, blank=True, verbose_name='Название')
    
    # books = models.ForeignKey(Book,
    #     on_delete=models.CASCADE,
    #     verbose_name='Категория',
    #     related_name='books' 
    #     )
        

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


        