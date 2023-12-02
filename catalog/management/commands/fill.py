from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        products_list = [
            {"name": "iPhone 13",
             "description": "Новый смартфон от Apple с передовыми технологиями и камерой высокого разрешения.",
             "purchase_price": 999.99, "category": Category.objects.get(id=3)},
            {"name": "Dell XPS 13",
             "description": "Легкий и мощный ноутбук с высоким разрешением дисплея и производительным процессором.",
             "purchase_price": 1299.99, "category": Category.objects.get(id=1)},
            {"name": "Sony Bravia 4K TV",
             "description": "4K телевизор с HDR и технологией Acoustic Surface для отличного звука.",
             "purchase_price": 1499.99, "category": Category.objects.get(id=2)},
            {"name": "Canon EOS R5",
             "description": "Зеркальная камера с высоким разрешением и возможностью съемки 8K видео.",
             "purchase_price": 2499.99, "category": Category.objects.get(id=7)},
            {"name": "Apple Watch Series 7",
             "description": "Умные часы с крупным дисплеем и множеством функций для отслеживания здоровья.",
             "purchase_price": 399.99, "category": Category.objects.get(id=8)},
            {"name": "PlayStation 5",
             "description": "Последняя игровая консоль от Sony с высокой производительностью и поддержкой 4K графики.",
             "purchase_price": 499.99, "category": Category.objects.get(id=9)},
            {"name": "AirPods Pro", "description": "Беспроводные наушники с активным шумоподавлением от Apple.",
             "purchase_price": 249.99, "category": Category.objects.get(id=10)}
        ]

        products_for_create = []
        for products_item in products_list:
            products_for_create.append(
                Product(**products_item)
            )

        Product.objects.bulk_create(products_for_create)