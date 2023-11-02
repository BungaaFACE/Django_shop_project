from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(
        max_length=150, verbose_name='категория', unique=True)
    category_desc = models.CharField(
        max_length=500, verbose_name='описание', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов


class Product(models.Model):
    product_name = models.CharField(
        max_length=150, verbose_name='наименование')
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

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name} {self.category_name} {self.unit_price}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов


class Contacts(models.Model):
    anons = models.TextField(verbose_name='обращение')
    phone = models.CharField(verbose_name='phone', max_length=15)
    email = models.EmailField(verbose_name='email')
    feedback_anons = models.TextField(verbose_name='заполнение формы')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.phone} {self.email}'

    class Meta:
        verbose_name = 'контакт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'контакты'  # Настройка для наименования набора объектов


class BlogEntry(models.Model):
    entry_title = models.CharField(
        max_length=150, verbose_name='заголовок')
    entry_slug = models.CharField(
        max_length=150, verbose_name='slug')
    entry_body = models.TextField(verbose_name='содержимое')
    entry_img = models.ImageField(
        upload_to='entry_img/', verbose_name='изображение', **NULLABLE)
    date_created = models.DateField(
        verbose_name="дата создания", auto_now_add=True)
    is_published = models.BooleanField(
        verbose_name="признак публикации", default=False)
    views_count = models.IntegerField(
        verbose_name="количество просмотров", default=0)

    def __str__(self):
        # Строковое отображение объекта
        return f'Название:{self.entry_title} Создание:{self.date_created} Опубликовано:{self.is_published} Просмотры:{self.views_count}'

    class Meta:
        verbose_name = 'Топик'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Топики'  # Настройка для наименования набора объектов
