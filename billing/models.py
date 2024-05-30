from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    product_id = models.CharField(max_length=50, unique=True)
    available_stocks = models.PositiveIntegerField()
    price = models.FloatField()
    tax_percentage = models.FloatField()

    def __str__(self):
        return self.name


class Purchase(models.Model):
    customer_email = models.EmailField()
    total_amount = models.FloatField()
    paid_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.FloatField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"