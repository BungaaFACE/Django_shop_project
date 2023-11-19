from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='catalog'),
    path('product/<int:pk>/',
         views.ProductDetailView.as_view(), name='product'),
    path('add_product', views.ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/update',
         views.ProductUpdateView.as_view(), name='update_product'),
]
