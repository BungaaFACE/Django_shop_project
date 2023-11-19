# Generated by Django 4.2.6 on 2023-11-19 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=150, unique=True, verbose_name='наименование'),
        ),
        migrations.CreateModel(
            name='ProductVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_version', models.CharField(max_length=50, verbose_name='номер версии')),
                ('version_name', models.CharField(max_length=50, verbose_name='название версии')),
                ('is_current_version', models.BooleanField(verbose_name='признак текущей версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', to_field='product_name', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'версия продукта',
                'verbose_name_plural': 'версии продуктов',
            },
        ),
    ]