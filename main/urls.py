from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('test_http_response', views.test_http_response, name='test_http_response'),
    path('test_include', views.test_include, name='test_include'),
    path('contacts', views.contacts, name='contacts'),
    path('catalog/', views.ProductListView.as_view(), name='catalog'),
    path('catalog/product/<int:pk>/',
         views.ProductDetailView.as_view(), name='product'),
    path('catalog/add_product', views.ProductCreateView.as_view(), name='add_product'),
    path('blog/add_entry', views.EntryCreateView.as_view(), name='add_entry'),
    path('blog/', views.EntryListView.as_view(), name='list_entry'),
    path('blog/<int:pk>', views.EntryDetailView.as_view(), name='entry_details'),
    path('blog/<int:pk>/delete',
         views.EntryDeleteView.as_view(), name='delete_entry'),
    path('blog/<int:pk>/update',
         views.EntryUpdateView.as_view(), name='update_entry'),
]
