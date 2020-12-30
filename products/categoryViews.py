from django.http import HttpResponse, JsonResponse
from .models import  Category
import json

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