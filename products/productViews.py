from django.http import HttpResponse, JsonResponse
from .models import Product, Category
import json

def product_list_view(request):
    category = request.GET.get('category')
    queryset = Product.objects.filter(
        category__name__icontain=category) if category else Product.objects.all()
    products = [
        {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.display_price,
            'image': product.image,
            'rating': product.rating,
            'category': product.category.name,
        }
        for product in queryset
    ]
    return JsonResponse({'products': products})


def product_create_view(request):
    body = json.loads(request.body.decode('utf-8'))
    product = Product(
        name=body['name'],
        description=body['description'],
        price=body['price'],
        image=body['image'],
        rating=body['rating'],
        category=Category.objects.get(name__iexact=body['category'])
    )
    product.save()
    data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'image': product.image,
        'rating': product.rating,
        'category': product.category.name
    }
    return JsonResponse(data)


def product_delete_view(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if not product:
        return JsonResponse({'message': 'Product not exist'})
    else:
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully'})


def product_update_view(request, product_id):
    body = json.loads(request.body.decode('utf-8'))
    product = Product.objects.filter(id=product_id).first()
    if not product:
        return JsonResponse({'message': 'Product not exist'})

    product.name = body['name']
    product.save()

    data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'image': product.image,
        'rating': product.rating,
        'category': product.category.name
    }
    return JsonResponse(data)


def product_By_id_view(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if not product:
        return JsonResponse({'message': 'Product not exist'})

    data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'image': product.image,
        'rating': product.rating,
        'category': product.category.name
    }
    return JsonResponse(data)
