from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint
from main.models import Product, Contacts
from main.forms import ProductForm
from django.urls import reverse


def test_http_response(request):
    return HttpResponse("""<h4>Привет мир!</h4><h3>Навигация</h3>
                        <ul>
                            <a href="/"><li><i class="fa-solid fa-house fa-fade"></i>Главная</li></a>
                            <a href="test_http_response"><li><i class="fa-solid fa-flask-vial fa-fade"></i>Test HttpResponse</li></a>
                            <a href="test_include"><li><i class="fa-solid fa-flask-vial fa-fade"></i>Test { %include% }</li></a>
                        </ul>""")


def test_include(request):
    return render(request, 'main/test_include.html')


def index(request):
    catalog = Product.objects.all()
    for product in catalog:
        if len(product.product_desc) > 100:
            product.product_desc = product.product_desc[:100] + '...'
    return render(request, 'main/index.html', {'catalog': catalog})


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


def catalog(request):
    catalog = Product.objects.all()[:5]
    for product in catalog:
        if len(product.product_desc) > 100:
            product.product_desc = product.product_desc[:100] + '...'
    return render(request, 'main/catalog.html', {'catalog': catalog})


def product_page(request, product_id):
    product_data = Product.objects.get(id=product_id)
    return render(request, 'main/product.html', {'product': product_data})


def add_product(request):
    result = ''
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.__dict__)
            form.save()
            result = "<h5 style='background-color: #00b91f; color: black; border-radius: 7px; height: 30px; text-align: center;'>Продукт добавлен!</h5>"
            form = ProductForm()
        else:
            result = "<h5 style='background-color: #a50000; color: black; border-radius: 7px; height: 30px; text-align: center;'>Неправильно заполнены данные!</h5>"
    else:
        form = ProductForm()
    return render(request, 'main/add_product.html', {'form': form, 'result': result})


def catalog_page(request, page_num):
    PRODUCTS_ON_PAGE = 6
    pages_buttons = ''
    catalog_url = reverse('catalog')

    catalog = Product.objects.all()
    total_pages = len(catalog) // PRODUCTS_ON_PAGE \
        if len(catalog) % PRODUCTS_ON_PAGE == 0 \
        else (len(catalog) // PRODUCTS_ON_PAGE) + 1

    if page_num > total_pages:
        page_num = total_pages
    elif page_num < 1:
        page_num = 1
    # выбираем товары только с нужной страницы и сокращаем описания
    catalog = catalog[PRODUCTS_ON_PAGE *
                      (page_num-1):PRODUCTS_ON_PAGE*page_num]
    for product in catalog:
        if len(product.product_desc) > 100:
            product.product_desc = product.product_desc[:100] + '...'

    for page_button in range(1, total_pages+1):
        print(page_button)
        if page_button == page_num:
            button_color = 'ffd900'
        else:
            button_color = 'd1b200'
        pages_buttons += f"<a class='btn' "\
            f"style='background-color: #{button_color}; color: black; border-radius: 7px; margin-left: 2px; margin-right: 2px;' "\
            f"href='{catalog_url}/page-"\
            f"{page_button}' "\
            f"role='button'>{page_button}</a>\n"
    print(pages_buttons)

    return render(request, 'main/catalog.html', {'catalog': catalog, 'buttons': pages_buttons})
