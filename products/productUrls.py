from django.urls import path
from .productViews import product_list_view, product_create_view, product_delete_view, product_update_view, product_By_id_view

urlpatterns = [
    path('list/', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-create'),
    path('<int:product_id>/delete/', product_delete_view, name='product-delete'),
    path('<int:product_id>/update/', product_update_view, name='product-update'),
    path('<int:product_id>/', product_By_id_view, name='product-By-id'),
]
