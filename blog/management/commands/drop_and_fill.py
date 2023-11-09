from django.core.management import BaseCommand
from main.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options) -> str | None:

        try:
            Product.objects.get().delete()
        except:
            pass

        products_list = [
            {'product_name': 'Кухонный стол раздвижной Мехико 120х76х90 см, Белый',
             'product_desc': 'Коллекция\tМехико\r\nПроизводитель\tРоссия\r\nГарантия\t24 мес.\r\nСрок службы\tГод: 5\r\nРазмер (ШхВхГ)\t90(120)x76x90 см\r\nМатериал\tмассив бука, ЛДСП, закалённое стекло\r\nЦвет\tбелый\r\nМаксимальная нагрузка\t50 кг',
             'product_img': 'products_img/116478aa325899ac9e7199168be517af.jpg',
             'category_name_id': 'Мебель',
             'unit_price': 22000.0,
             },
            {'product_name': 'Стол Милан раздвижной 125х76х90 см, Белый',
             'product_desc': 'Коллекция\Милан\r\nПроизводитель\tРоссия\r\nГарантия\t24 мес.\r\nСрок службы\tГод: 5\r\nРазмер (ШхВхГ)\t90(125)x76x90 см\r\nМатериал\tметалл, ЛДСП, закалённое стекло\r\nЦвет\сатин, белый\r\nМаксимальная нагрузка\t50 кг',
             'product_img': 'products_img/b8fa7e781fbf8669daac81aec9e0fcef.jpg',
             'category_name_id': 'Мебель',
             'unit_price': 19999.0,
             },
        ]

        # for product in products_list:
        #     Product.objects.create(**product)

        product_instances = []
        for product in products_list:
            product_instances.append(Product(**product))

        Product.objects.bulk_create(product_instances)
