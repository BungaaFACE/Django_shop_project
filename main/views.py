from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
from pprint import pprint
from main.models import Product, Contacts, Category, BlogEntry
from main.forms import ProductForm, EntryForm
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify


def test_http_response(request):
    return HttpResponse("""<h4>Привет мир!</h4><br><h3>Навигация</h3>
                        <ul>
                            <a href="/"><li><i class="fa-solid fa-house fa-fade"></i>Главная</li></a>
                            <a href="test_http_response"><li><i class="fa-solid fa-flask-vial fa-fade"></i>Test HttpResponse</li></a>
                            <a href="test_include"><li><i class="fa-solid fa-flask-vial fa-fade"></i>Test { %include% }</li></a>
                        </ul>""")


def test_include(request):
    return render(request, 'main/test_include.html')


def contacts(request):
    if request.method == 'POST':
        data = {}
        # в переменной request хранится информация о методе, который отправлял пользователь
        data['email'] = request.POST.get('email')
        data['mobile_number'] = request.POST.get('mobile_number')
        data['customer_needs'] = request.POST.get('customer_needs')
        # а также передается информация, которую заполнил пользователь
        pprint(data)
    feedback_data = Contacts.objects.get(id=1)

    return render(request, 'main/contacts.html', {'feedback_data': feedback_data})


class ProductDetailView(DetailView):
    model = Product

    # def product_page(request, product_id):
    #     product_data = Product.objects.get(id=product_id)
    #     return render(request, 'main/product_detail.html', {'product': product_data})


class ProductCreateView(CreateView):
    model = Product  # Модель
    form_class = ProductForm
    template_name = 'main/add_product.html'

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

    # def add_product(request):
    #     result = ''
    #     if request.method == 'POST':
    #         form = ProductForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             print(form.__dict__)
    #             form.save()
    #             result = "<h5 style='background-color: #00b91f; color: black; border-radius: 7px; height: 30px; text-align: center;'>Продукт добавлен!</h5>"
    #             form = ProductForm()
    #         else:
    #             result = "<h5 style='background-color: #a50000; color: black; border-radius: 7px; height: 30px; text-align: center;'>Неправильно заполнены данные!</h5>"
    #     else:
    #         form = ProductForm()
    #     return render(request, 'main/add_product.html', {'form': form, 'result': result})


class ProductListView(ListView):
    model = Product  # Модель
    paginate_by = 6
    context_object_name = 'catalog'

    # def catalog_page(request, page_num):
    #     PRODUCTS_ON_PAGE = 6
    #     pages_buttons = ''
    #     catalog_url = reverse('catalog')

    #     catalog = Product.objects.all()
    #     total_pages = len(catalog) // PRODUCTS_ON_PAGE \
    #         if len(catalog) % PRODUCTS_ON_PAGE == 0 \
    #         else (len(catalog) // PRODUCTS_ON_PAGE) + 1

    #     if page_num > total_pages:
    #         page_num = total_pages
    #     elif page_num < 1:
    #         page_num = 1
    #     # выбираем товары только с нужной страницы и сокращаем описания
    #     catalog = catalog[PRODUCTS_ON_PAGE *
    #                     (page_num-1):PRODUCTS_ON_PAGE*page_num]

    #     for page_button in range(1, total_pages+1):
    #         if page_button == page_num:
    #             button_color = 'ffd900'
    #         else:
    #             button_color = 'd1b200'
    #         pages_buttons += f"<a class='btn' "\
    #             f"style='background-color: #{button_color}; color: black; border-radius: 7px; margin-left: 2px; margin-right: 2px;' "\
    #             f"href='{catalog_url}page/{page_button}' "\
    #             f"role='button'>{page_button}</a>\n"
    #     return render(request, 'main/catalog.html', {'catalog': catalog, 'buttons': pages_buttons})


class EntryCreateView(CreateView):
    model = BlogEntry  # Модель
    form_class = EntryForm
    template_name = 'main/add_blog_entry.html'

    def post(self, request, *args, **kwargs):
        form = EntryForm(request.POST, request.FILES)
        print(form.__dict__)
        if form.is_valid():
            saved_form = form.save()
            saved_form.entry_slug = slugify(
                saved_form.entry_title)
            saved_form.save()
            result = "<h5 style='background-color: #00b91f; color: black; border-radius: 7px; height: 30px; text-align: center;'>Запись добавлена!</h5>"
            form = EntryForm()
        else:
            result = "<h5 style='background-color: #a50000; color: black; border-radius: 7px; height: 30px; text-align: center;'>Неправильно заполнены данные!</h5>"
        return render(request, self.template_name, {'form': form, 'result': result})


class EntryDetailView(DetailView):
    model = BlogEntry
    context_object_name = 'entry'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class EntryListView(ListView):
    model = BlogEntry
    paginate_by = 2
    context_object_name = 'blog_entries'

    def get_queryset(self):
        # data =  super().get_queryset()
        data = BlogEntry.objects.filter(
            is_published=True).order_by('-date_created')
        return data


class EntryUpdateView(UpdateView):
    model = BlogEntry
    form_class = EntryForm
    template_name = 'main/update_blog_entry.html'

    def form_valid(self, form):
        if form.is_valid():
            saved_form = form.save()
            saved_form.entry_slug = slugify(
                saved_form.entry_title)
            saved_form.save()
            EntryUpdateView.success_url = f'{reverse_lazy("list_entry")}{saved_form.pk}'
        return super().form_valid(form)


class EntryDeleteView(DeleteView):
    model = BlogEntry
    success_url = reverse_lazy("list_entry")
    context_object_name = 'entry'
