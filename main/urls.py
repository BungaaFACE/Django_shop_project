from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('test_http_response', views.test_http_response, name='test_http_response'),
    path('test_include', views.test_include, name='test_include'),
    path('contacts', views.contacts, name='contacts'),
    path('catalog', views.catalog, name='catalog')
]
