from django.db import models

# Create your models here.



class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    name = models.CharField(max_length=100, verbose_name='Название')
    title = models.CharField(max_length=100, verbose_name='Заглавие')
    description = models.CharField(max_length=100, verbose_name='Описание')
    price = models.IntegerField(default=50, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категория')


    def __str__(self):
        return self.name


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    text: str = models.CharField(max_length=100, verbose_name='Текст')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name='Продукт')

    def __str__(self):
        return self.text