from django.db import DatabaseError, transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import InvoiceOrderSerializer, OrderSerializer, InvoiceSerializer, InvoiceOrderSerializer, ProductItemSerializer, ProductItemsSerializer

import datetime


@api_view(['POST'])
@transaction.atomic
def create_order(request):
    productItemsSerializer = ProductItemsSerializer(data=request.data)
    if productItemsSerializer.is_valid():
        productItemsSerializer.save()

        return Response({
            'orderId': productItemsSerializer.data['name'],
            'invoice_no': productItemsSerializer.data['address'],
        }, status=status.HTTP_201_CREATED)

    return Response(productItemsSerializer.errors, status=status.HTTP_400_BAD_REQUEST)