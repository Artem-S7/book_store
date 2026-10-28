from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва')
    author = models.CharField(max_length=100, verbose_name='Автор')
    price = models.DecimalField(decimal_places=2, max_digits=13, verbose_name='Ціна')
    description = models.TextField(verbose_name='Опис')
    stock = models.IntegerField(verbose_name='Кількість')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

