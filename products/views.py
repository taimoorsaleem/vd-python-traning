from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product, Category
import json


def home(request):
    return HttpResponse('Hello products')


def category_list_view(request):
    name = request.GET.get('q')
    queryset = Category.objects.filter(
        name__icontains=name) if name else Category.objects.all()
    categories = [
        {
            'id': category.id,
            'name': category.name,
            'description': category.description,
        }
        for category in queryset
    ]
    return JsonResponse({'categories': categories})


def category_create_view(request):
    body = json.loads(request.body.decode('utf-8'))
    category = Category(
        name=body['name'],
        description=body['description'],
    )
    category.save()
    data = {
        'id': category.id,
        'name': category.name,
    }
    return JsonResponse(data)


def category_delete_view(request, category_id):
    category = Category.objects.filter(id=category_id).first()
    if not category:
        return JsonResponse({'message': 'Category not exist'})
    else:
        category.delete()
        return JsonResponse({'message': 'Category deleted successfully'})


def category_update_view(request, category_id):
    body = json.loads(request.body.decode('utf-8'))
    category = Category.objects.filter(id=category_id).first()
    if not category:
        return JsonResponse({'message': 'Category not exist'})

    category.name = body['name']
    category.description = body['description']
    product.save()

    data = {
        'id': category.id,
        'name': category.name,
        'description': category.description,
    }
    return JsonResponse(data)


def category_By_id_view(request, category_id):
    category = Category.objects.filter(id=category_id).first()
    if not category:
        return JsonResponse({'message': 'Category not exist'})

    data = {
        'id': category.id,
        'name': category.name,
        'description': category.description
    }
    return JsonResponse(data)


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
