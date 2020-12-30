from django.contrib import admin
from .models import Order, OrderItem, Invoice, InvoiceOrder

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order')
    search_fields = ('product', 'order')

@admin.register(InvoiceOrder)
class InvoiceOrderAdmin(admin.ModelAdmin):
    list_display = ('order','invoice')
    search_fields = ('',)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()

