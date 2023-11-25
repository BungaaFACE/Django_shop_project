from django_filters import FilterSet
from catalog.models import Product


class ProductFilter(FilterSet):

    class Meta:
        model = Product
        fields = ['is_published',]
