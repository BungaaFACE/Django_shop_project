from pprint import pprint
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from catalog.models import Product, ProductVersion
from catalog.forms import ProductForm, ProductVersionForm


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    # extra_content = {'type': 'Добавить'}
    success_url = reverse_lazy('add_product')

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
            form = ProductForm()
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


class ProductListView(ListView):
    model = Product
    paginate_by = 6
    context_object_name = 'catalog'

    def get_queryset(self):
        data = Product.objects.all().order_by('-date_last_modified')

        return data


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    extra_content = {'type': 'Изменить'}

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

        context_data['type'] = 'Добавить'
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
