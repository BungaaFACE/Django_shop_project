# Generated by Django 4.2.6 on 2023-12-07 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_distribution', '0003_emailsubscribtion_is_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsubscribtionlogs',
            name='is_success',
            field=models.BooleanField(default=True, verbose_name='успешно'),
        ),
    ]
