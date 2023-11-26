from django.urls import path
from . import views
from catalog.views import CategoryListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('test_http_response', views.test_http_response, name='test_http_response'),
    path('test_include', views.test_include, name='test_include'),
    path('contacts', views.contacts, name='contacts'),
]
