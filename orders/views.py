from django.http import HttpResponse, JsonResponse
from django.db import DatabaseError, transaction
from .models import Order, OrderItem, Invoice, InvoiceOrder
from products.models import Product
import json
import datetime


@transaction.atomic
def create_order_view(request):
    body = json.loads(request.body.decode('utf-8'))
    order = Order(
        status='pending',
        order_date=datetime.datetime.now(),
    )
    order.save()
    total = 0
    for selected_product in body['products']:
        product = Product.objects.get(id=selected_product['id'])
        OrderItem.objects.bulk_create([
            OrderItem(
                order=order,
                cost=product.price,
                quantity=selected_product['quantity'],
                product=product,
            )
        ])
        total = total + (product.price * selected_product['quantity'])

    invoice = Invoice(
        status='pending',
        period_start_date=datetime.date.today(),
        period_end_date=datetime.date.today() + datetime.timedelta(days=7),
        invoice_date=datetime.datetime.now(),
    )

    invoiceorder = InvoiceOrder(
        invoice=invoice,
        order=order,
    )

    order.total = total
    order.save()
    invoice.save()
    invoiceorder.save()
    data = {
        'orderId': order.id,
        'invoice_no': invoice.invoice_no,
        'invoice_no1': 'invoice.invoice_no',
    }
    return JsonResponse(data)
