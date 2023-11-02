from django.contrib import admin

from main.models import Product, Category, Contacts, BlogEntry


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'unit_price', 'category_name')
    list_filter = ('category_name',)
    search_fields = ('product_name', 'product_desc')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')


@admin.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('entry_title', 'entry_slug', 'entry_body',
                    'is_published', 'views_count')
