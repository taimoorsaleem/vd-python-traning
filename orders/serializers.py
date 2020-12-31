from rest_framework import serializers
from products.models import Product
from .models import Order, OrderItem, Invoice, InvoiceOrder
import datetime
from phonenumber_field.serializerfields import PhoneNumberField


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = serializers.ALL_FIELDS


class OrderItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    order = serializers.SlugRelatedField(
        queryset=Order.objects.all(), slug_field='id')

    product = serializers.SlugRelatedField(
        queryset=Product.objects.all(), slug_field='id')

    class Meta:
        model = OrderItem
        fields = serializers.ALL_FIELDS

    def validate_quantity(self, quantity):
        if quantity > 0:
            return quantity
        else:
            raise serializers.ValidationError(
                'Quantity must be greater than zero.')


class InvoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Invoice
        fields = serializers.ALL_FIELDS


class InvoiceOrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    invoice = serializers.SlugRelatedField(
        queryset=Invoice.objects.all(), slug_field='id')
    order = serializers.SlugRelatedField(
        queryset=Order.objects.all(), slug_field='id')

    class Meta:
        model = InvoiceOrder
        fields = serializers.ALL_FIELDS


class ProductItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate_quantity(self, quantity):
        if quantity > 0:
            return quantity
        else:
            raise serializers.ValidationError(
                'Quantity must be greater than zero.')

    def validate_id(self, id):
        if id > 0:
            return id
        else:
            raise serializers.ValidationError(
                'Invalid id.')


class ProductItemsSerializer(serializers.Serializer):
    products = serializers.ListField(child=ProductItemSerializer())
    name = serializers.CharField(max_length=250)
    phone = PhoneNumberField()
    email = serializers.EmailField()
    address = serializers.CharField()

    class Meta:
        list_serializer_class = ProductItemSerializer

    def create(self, validated_data):
        products = validated_data.get('products')
        print('product', products)

        order = Order.objects.create(
            status='pending',
            order_date=datetime.datetime.now(),
            email=validated_data['email'],
            phone=validated_data['phone'],
            name=validated_data['name'],
            address=validated_data['address'],
        )
        total = 0
        for selected_product in products:
            print('selected_product.get(id)', selected_product.get('id'))
            print('selected_product.get(quantity)',
                  selected_product.get('quantity'))
            product = Product.objects.get(id=selected_product.get('id'))
            print('product', product.price)

            OrderItem.objects.bulk_create([
                OrderItem(
                    order=order,
                    cost=product.price,
                    quantity=selected_product.get('quantity'),
                    product=product,
                )
            ])
            total = total + (product.price * selected_product.get('quantity'))
        invoice = Invoice.objects.create(
            status='pending',
            period_start_date=datetime.date.today(),
            period_end_date=datetime.date.today() + datetime.timedelta(days=7),
            invoice_date=datetime.datetime.now(),
        )

        invoiceorder = InvoiceOrder.objects.create(
            invoice=invoice,
            order=order,
        )

        order.total = total
        order.save()
        return {
            'products': products,
            'name': order.id,
            'address': invoice.invoice_no,
            'phone': validated_data.get('phone'),
            'email': validated_data.get('email'),
        }
