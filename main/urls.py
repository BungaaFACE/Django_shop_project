from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('test_http_response', views.test_http_response, name='test_http_response'),
    path('test_include', views.test_include, name='test_include'),
    path('contacts', views.contacts, name='contacts'),
    path('catalog', views.catalog, name='catalog'),
    path('catalog/product-<int:product_id>/',
         views.product_page, name='product'),
    path('catalog/add_product', views.add_product, name='add_product'),
    path('catalog/page-<int:page_num>/',
         views.catalog_page, name='catalog_page'),
]
