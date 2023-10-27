from main.models import Product, Category
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
