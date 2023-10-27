# Generated by Django 4.2.6 on 2023-10-26 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150, unique=True, verbose_name='категория')),
                ('category_desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150, verbose_name='наименование')),
                ('product_desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='описание')),
                ('product_img', models.ImageField(blank=True, null=True, upload_to='products_img/', verbose_name='изображение')),
                ('unit_price', models.FloatField(verbose_name='цена')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('date_last_modified', models.DateField(auto_now=True, verbose_name='дата изменения')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', to_field='category_name', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
