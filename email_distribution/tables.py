import django_tables2 as tables
from email_distribution.models import Client, EmailFilling, EmailSubscribtion
from django.urls import reverse
from django.utils.html import format_html

from users.models import User


class UserTable(tables.Table):
    user_action = tables.Column(empty_values=(), verbose_name='Действия')

    class Meta:
        model = User
        template_name = "django_tables2/bootstrap5.html"
        fields = ("email", 'phone', 'is_active')
        attrs = {"class": "table table-striped table-dark table-hover table-sm",
                 "style": "font-size: 18px"}

    def render_email(self, value, record):
        # Delete link mail_to:email
        return record.email

    def render_user_action(self, record):
        if record.is_active:
            return format_html('<a class="btn btn-danger" href="{}" role="button">Заблокировать</a>', reverse("block_user", args=(record.pk,)))
        else:
            return format_html('<a class="btn btn-warning" href="{}" role="button">Разблокировать</a>', reverse("unblock_user", args=(record.pk,)))


class ClientTable(tables.Table):
    class Meta:
        model = Client
        template_name = "django_tables2/bootstrap5.html"
        fields = ("email", 'full_name', 'comment')
        attrs = {"class": "table table-striped table-dark table-hover table-sm",
                 "style": "font-size: 18px"}

    def render_email(self, value, record):
        return format_html('<a href="{}" role="button">{}</a>', reverse("clients_detail", args=(record.pk,)), value)


class EmailFillingTable(tables.Table):
    class Meta:
        model = EmailFilling
        template_name = "django_tables2/bootstrap5.html"
        fields = ("email_template_name", 'email_subject', 'email_body')
        attrs = {"class": "table table-striped table-dark table-hover table-sm",
                 "style": "color: white; font-size: 18px"}

    def render_email_body(self, value, record):
        return f'{value[:50]}...'

    def render_email_template_name(self, value, record):
        return format_html('<a href="{}" role="button">{}</a>', reverse("templates_detail", args=(record.pk,)), value)


class EmailSubscribtionTable(tables.Table):
    class Meta:
        model = EmailSubscribtion
        template_name = "django_tables2/bootstrap5.html"
        fields = ("client", 'periodic_time', 'time', 'email_filling', 'status')
        attrs = {"class": "table table-striped table-dark table-hover table-sm",
                 "style": "color: white; font-size: 18px"}

    def render_client(self, value, record):
        return format_html('<a href="{}" role="button">{}</a>', reverse("distributions_detail", args=(record.pk,)), value)
