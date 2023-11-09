from django.shortcuts import render

from django.views.generic import DetailView, ListView, CreateView
from catalog.models import Product
from catalog.forms import ProductForm
from django.urls import reverse


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product  # Модель
    form_class = ProductForm
    template_name = 'catalog/add_product.html'

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            result = "<h5 style='background-color: #00b91f; color: black; border-radius: 7px; height: 30px; text-align: center;'>Продукт добавлен!</h5>"
            form = ProductForm()
        else:
            result = "<h5 style='background-color: #a50000; color: black; border-radius: 7px; height: 30px; text-align: center;'>Неправильно заполнены данные!</h5>"
        print(reverse("add_product"))
        return render(request, self.template_name, {'form': form, 'result': result})


class ProductListView(ListView):
    model = Product  # Модель
    paginate_by = 6
    context_object_name = 'catalog'
