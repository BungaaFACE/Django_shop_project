from django.contrib import admin

from catalog.models import Product, Category, ProductVersion


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'unit_price',
                    'category_name', 'is_published', 'user')
    list_filter = ('category_name', 'is_published')
    search_fields = ('product_name', 'product_desc')


@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_version',
                    'version_name', 'is_current_version')
    list_filter = ('is_current_version',)
    search_fields = ('product', 'version_name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
