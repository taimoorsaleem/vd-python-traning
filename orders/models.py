from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from products.models import Product


class Order(models.Model):
    total = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=250)
    order_date = models.DateTimeField()
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    name = models.CharField(max_length=250,  null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        pass


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE)
    cost = models.IntegerField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        pass


class Invoice(models.Model):
    def __str__(self):
        pass

    def increment_invoice_number():
        last_invoice = Invoice.objects.all().order_by('id').last()
        if not last_invoice:
            return 'MAG0001'
        invoice_no = last_invoice.invoice_no
        invoice_int = int(invoice_no.split('MAG')[-1])
        new_invoice_int = invoice_int + 1
        new_invoice_no = 'MAG' + str(new_invoice_int)
        return new_invoice_no

    invoice_no = models.CharField(
        max_length=500, default=increment_invoice_number, null=True, blank=True)
    status = models.CharField(max_length=250)
    period_start_date = models.DateField()
    period_end_date = models.DateField()
    invoice_date = models.DateTimeField()


class InvoiceOrder(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        pass