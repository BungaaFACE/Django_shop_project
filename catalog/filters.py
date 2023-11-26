from django_filters import FilterSet
from catalog.models import Product


class ProductFilter(FilterSet):

    class Meta:
        model = Product
        fields = ['category_name', 'is_published',]
