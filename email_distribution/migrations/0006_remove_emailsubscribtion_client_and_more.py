# Generated by Django 4.2.6 on 2023-12-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_distribution', '0005_alter_emailsubscribtion_next_send_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailsubscribtion',
            name='client',
        ),
        migrations.AlterField(
            model_name='emailsubscribtion',
            name='status',
            field=models.CharField(choices=[('in_progress', 'В работе'), ('idle', 'Ожидание')], default='idle', max_length=50, verbose_name='статус рассылки'),
        ),
        migrations.AddField(
            model_name='emailsubscribtion',
            name='client',
            field=models.ManyToManyField(to='email_distribution.client', verbose_name='клиент'),
        ),
    ]
