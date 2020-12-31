from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def fetch_product_by_id(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'error': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({'error': 'Interna server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({'error': 'Interna server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def update_product_patch(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({'error': 'Interna server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    print(product)
    serializer = ProductSerializer(product, data=request.data, partial=True))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({'error': 'Interna server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    product.delete()
    return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
