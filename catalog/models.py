from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='описание')


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    purchase_price = models.FloatField(verbose_name='цена за покупку')
    date_of_creation = models.DateField(verbose_name='дата создания')
    last_modified_date = models.DateField(verbose_name='дата последнего изменения')
