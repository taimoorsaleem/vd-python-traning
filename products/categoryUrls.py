from django.urls import path
from .views import category_list_view, category_create_view, category_delete_view, category_update_view, category_By_id_view

urlpatterns = [
    path('list/', category_list_view, name='category-list'),
    path('create/', category_create_view, name='category-create'),
    path('<int:category_id>/delete/', category_delete_view, name='category-delete'),
    path('<int:category_id>/update/', category_update_view, name='category-update'),
    path('<int:category_id>/', category_By_id_view, name='category-By-id'),
]

