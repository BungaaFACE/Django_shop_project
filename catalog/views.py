from pprint import pprint
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from catalog.filters import ProductFilter
from catalog.models import Category, Product, ProductVersion
from catalog.forms import ProductFormAdmin, ProductFormModerator, ProductFormUser, ProductVersionForm
from django_filters.views import FilterView

from catalog.services import get_category_list


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['version'] = ProductVersion.objects.get(
                product=context['object'], is_current_version=True)
        except:
            pass
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('add_product')

    def get_form_class(self):
        if self.request.user.is_superuser:
            self.form_class = ProductFormAdmin
        else:
            self.form_class = ProductFormUser
        return super().get_form_class()

    def form_valid(self, form):
        if form.is_valid():
            result = "<h5 style='background-color: #00b91f; color: black; border-radius: 7px; height: 30px; text-align: center;'>Продукт добавлен!</h5>"
            # Сохранение формы
            product = form.save()
            product.user = self.request.user
            product.save()
            # Создание и сохранение версии
            version = ProductVersion(product=product, product_version="1.0",
                                     version_name="Создание продукта", is_current_version=True)
            version.save()
            # Очистка формы для вывода удачного результата
            form = self.form_class
            return self.render_to_response(self.get_context_data(form=form, result=result))
        return super().form_valid(form)

    def form_invalid(self, form):
        if not form.is_valid():
            result = "<h5 style='background-color: #a50000; color: black; border-radius: 7px; height: 30px; text-align: center;'>Неправильно заполнены данные или данный продукт уже добавлен!</h5>"
            return self.render_to_response(self.get_context_data(form=form, result=result))
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context["result"] = kwargs['result']
        context['type'] = 'Добавить'
        return context


class ProductListView(FilterView):
    model = Product
    paginate_by = 6
    context_object_name = 'catalog'
    filterset_class = ProductFilter
    template_name = 'catalog/product_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.has_perm('catalog.set_published'):
            data = Product.objects.all().order_by('-date_last_modified')
        else:
            data = Product.objects.filter(
                is_published=True).order_by('-date_last_modified')

        return data


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'catalog/add_product.html'

    def get_form_class(self):
        if self.request.user.is_superuser:
            self.form_class = ProductFormAdmin
        elif self.request.user == self.object.user:
            self.form_class = ProductFormUser
        elif self.request.user.has_perm('catalog.set_published'):
            self.form_class = ProductFormModerator
        return super().get_form_class()

    def test_func(self):
        return self.request.user.is_superuser or \
            self.request.user == self.get_object().user or \
            self.request.user.has_perm('catalog.set_published')

    def get_success_url(self, *args, **kwargs):
        return reverse('product', args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(
            Product, ProductVersion, form=ProductVersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(
                self.request.POST, instance=self.object)
            context_data["result"] = kwargs.get('result', '')
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        context_data['type'] = 'Изменить'
        return context_data

    def form_invalid(self, form):
        if not form.is_valid():
            result = "<h5 style='background-color: #a50000; color: black; border-radius: 7px; height: 30px; text-align: center;'>Неправильно заполнены данные!</h5>"
            return self.render_to_response(self.get_context_data(form=form, result=result))
        return super().form_invalid(form)

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()

        current_version_checked = False
        for key, value in formset.__dict__['data'].items():
            # Ищем нажатые поля активной версии
            if '-is_current_version' in key and value == 'on':
                # Если раньше уже находили активированное поле
                if current_version_checked:
                    result = "<h5 style='background-color: #a50000; color: black; border-radius: 7px; height: 30px; text-align: center;'>Можно выбрать только одну активную версию!</h5>"
                    # Возвращаем сообщение с ошибкой
                    return self.render_to_response(
                        self.get_context_data(form=form, result=result))

                # Если это первое активированное поле
                else:
                    # Отмечаем это
                    current_version_checked = True

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class CategoryListView(ListView):
    model = Category
    paginate_by = 6
    context_object_name = 'categories'
    # template_name = 'catalog/product_list.html'

    def get_queryset(self):
        return get_category_list()
