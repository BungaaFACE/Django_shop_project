from django.contrib import admin

from main.models import Contacts


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')
