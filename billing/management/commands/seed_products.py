from django.core.management.base import BaseCommand
from billing.models import Product


class Command(BaseCommand):
    help = 'Seed the database with initial product data'

    def handle(self, *args, **kwargs):
        products = [
            {"name": "Product 1", "product_id": "PID123", "available_stocks": 100, "price": 10.0,
             "tax_percentage": 5.0},
            {"name": "Product 2", "product_id": "PID456", "available_stocks": 50, "price": 20.0,
             "tax_percentage": 10.0},
            {"name": "Product 3", "product_id": "PID789", "available_stocks": 75, "price": 30.0, "tax_percentage": 8.0},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'{product.name} already exists'))