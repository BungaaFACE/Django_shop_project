from django.urls import path
from catalog import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', views.ProductListView.as_view(), name='catalog'),
    path('product/<int:pk>/',
         cache_page(60)(views.ProductDetailView.as_view()), name='product'),
    path('add_product', views.ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/update',
         views.ProductUpdateView.as_view(), name='update_product'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
]
