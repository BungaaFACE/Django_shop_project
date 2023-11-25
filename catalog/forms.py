from catalog.models import Product, Category, ProductVersion
from django import forms


RESTRICTED_WORDS = {'казино', 'криптовалюта', 'крипта',
                    'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'}

PRODUCT_WIDGETS = {
    "product_name": forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Название',
    }),
    "product_desc": forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Описание'
    }),
    "product_img": forms.FileInput(attrs={
        'class': 'form-control',
        'placeholder': 'Картинка',
    }),
    "category_name": forms.Select(choices=Category.objects.values('category_name', 'category_name'), attrs={
        'class': 'form-control',
        'placeholder': 'Категория'
    }),
    "unit_price": forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Цена в рублях',
    }),
    "is_published": forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'type': "checkbox",
        'role': "switch",
        'id': "flexSwitchCheckDefault",
        'placeholder': 'Опубликовано',
    })
}


def check_restricted_words(cleaned_data, message='Использованы запрещенные слова.'):
    for restrict in RESTRICTED_WORDS:
        if restrict in cleaned_data:
            raise forms.ValidationError(message)


class ProductFormAdmin(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        widgets = PRODUCT_WIDGETS

    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name').lower().strip()
        check_restricted_words(
            cleaned_data,
            message='Данный продукт запрещен к добавлению.')

        return cleaned_data

    def clean_product_desc(self):
        cleaned_data = self.cleaned_data.get('product_desc').lower().strip()
        check_restricted_words(
            cleaned_data,
            message='Использовано запрещенное слово.')

        return cleaned_data


class ProductFormUser(ProductFormAdmin):

    class Meta:
        model = Product
        fields = ("product_name", "product_desc",
                  "product_img", "category_name", "unit_price")

        widgets = PRODUCT_WIDGETS


class ProductFormModerator(ProductFormAdmin):

    class Meta:
        model = Product
        exclude = ('user', 'product_img')

        widgets = PRODUCT_WIDGETS.copy()
        widgets['product_name'].attrs['readonly'] = ''
        widgets['product_img'].attrs['readonly'] = ''
        widgets['unit_price'].attrs['readonly'] = ''


class ProductVersionForm(forms.ModelForm):
    is_current_version = forms.BooleanField(required=False)

    class Meta:
        model = ProductVersion
        exclude = ('product',)

        widgets = {
            "product_version": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер версии'
            }),
            "version_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название версии'
            }),
            "is_current_version": forms.RadioSelect(attrs={
                'class': "form-check-input",
                'name': "flexRadioDefault",
                'type': "radio",
                'placeholder': 'Текущая версия'
            })
        }
