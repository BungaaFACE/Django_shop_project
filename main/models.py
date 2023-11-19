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


class Client(models.Model):
    email = models.EmailField(verbose_name='email')
    full_name = models.CharField(verbose_name='ФИО', max_length=450)
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.email} {self.full_name}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class EmailFilling(models.Model):
    email_theme = models.CharField(verbose_name='тема письма', max_length=300)
    email_body = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return f'{self.email_theme}: {self.email_body}'

    class Meta:
        verbose_name = 'наполнение письма'
        verbose_name_plural = 'нополнения писем'


class EmailSubscribtion(models.Model):
    time = models.TimeField(verbose_name='время рассылки', auto_now=True)
    client = models.ForeignKey(
        Client, verbose_name="клиент", on_delete=models.CASCADE)
    email_filling = models.ForeignKey(
        EmailFilling, verbose_name="наполнение письма", on_delete=models.CASCADE)
    periodic_time = models.CharField(
        verbose_name='периодичность', max_length=100)
    status = models.CharField(verbose_name='статус рассылки', max_length=50)
    next_send_date = models.DateField(
        verbose_name='дата следующей отправки', **NULLABLE)

    def __str__(self):
        return f'{self.client} {self.email_filling} {self.periodic_time}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class EmailSubscribtionLogs(models.Model):
    subscription = models.ForeignKey(
        EmailSubscribtion, verbose_name="рассылка", on_delete=models.CASCADE)
    last_try_date = models.DateTimeField(
        verbose_name="дата и время последней попытки", auto_now_add=True)
    is_success = models.BooleanField(
        verbose_name="статус попытки", default=True)
    last_mail_response = models.TextField(
        verbose_name="ответ почтового сервера", **NULLABLE)

    def __str__(self):
        return f'{self.subscription} {self.last_try_date} {self.is_success}'

    class Meta:
        verbose_name = 'лог рассылки'
        verbose_name_plural = 'логи рассылки'
