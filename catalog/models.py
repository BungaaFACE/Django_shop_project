from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(
        max_length=150, verbose_name='категория', unique=True)
    category_desc = models.CharField(
        max_length=500, verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(
        max_length=150, verbose_name='наименование', unique=True)
    product_desc = models.TextField(verbose_name='Описание', **NULLABLE)
    product_img = models.ImageField(
        upload_to='products_img/', verbose_name='изображение', **NULLABLE)
    category_name = models.ForeignKey(
        Category, to_field='category_name', verbose_name="категория", on_delete=models.CASCADE)
    unit_price = models.FloatField(verbose_name="цена")
    date_created = models.DateField(
        verbose_name="дата создания", auto_now_add=True)
    date_last_modified = models.DateField(
        verbose_name="дата изменения", auto_now=True)
    user = models.ForeignKey(User, verbose_name=_(
        "пользователь"), on_delete=models.CASCADE, default=None, **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов


class ProductVersion(models.Model):
    product = models.ForeignKey(
        Product, to_field='product_name', verbose_name="продукт", on_delete=models.CASCADE)
    product_version = models.CharField(
        verbose_name="номер версии", max_length=50)
    version_name = models.CharField(
        verbose_name="название версии", max_length=50)
    is_current_version = models.BooleanField(
        verbose_name="признак текущей версии")

    def __str__(self):
        return f'{self.product} {self.version_name} {self.product_version} {self.is_current_version}'

    class Meta:
        verbose_name = 'версия продукта'
        verbose_name_plural = 'версии продуктов'
