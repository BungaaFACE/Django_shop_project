from main.models import Product, Category, BlogEntry
from django import forms


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ("product_name", "product_desc",
                  "product_img", "category_name", "unit_price")
        categories = Category.objects.values('category_name', 'category_name')

        widgets = {
            "product_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "product_desc": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "product_img": forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Картинка'
            }),
            "category_name": forms.Select(choices=categories, attrs={
                'class': 'form-control',
                'placeholder': 'Категория'
            }),
            "unit_price": forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена в рублях'
            }),
        }


class EntryForm(forms.ModelForm):
    is_published = forms.BooleanField(required=False)

    class Meta:
        model = BlogEntry
        fields = ("entry_title", "entry_body", "entry_img", "is_published")

        widgets = {
            "entry_title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),
            "entry_body": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержание записи'
            }),
            "entry_img": forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Картинка'
            }),

        }
