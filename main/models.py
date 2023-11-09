from django.db import models


NULLABLE = {'blank': True, 'null': True}


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


class EmailSubscribers(models.Model):
    email = models.EmailField(verbose_name='email')
    full_name = models.CharField(verbose_name='ФИО', max_length=450)
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.email} {self.full_name}'

    class Meta:
        verbose_name = 'подписчик рассылки'
        verbose_name_plural = 'подписчики рассылки'
