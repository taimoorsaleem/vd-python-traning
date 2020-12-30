from django.db import models
from products.models import Product


class Order(models.Model):
    total = models.IntegerField()
    status = models.CharField(max_length=250)
    order_date = models.DateTimeField()

    def __str__(self):
        pass


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cost = models.IntegerField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        pass


class Invoice(models.Model):
    invoice_number = models.IntegerField()
    statsus = models.CharField(max_length=250)
    period_start_date = models.DateField()
    period_end_date = models.DateField()
    invoice_date = models.DateTimeField()

    def __str__(self):
        pass


class InvoiceOrder(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        pass
