from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('index', views.list_product, name = 'list_product'),


    path('category', views.list_category, name='list_category'),
    path('sub_category/<str:pk>', views.view_sub_category, name='sub_category'),

    path('add_product', views.add_product, name='add_product'),
    path('add_category', views.add_category, name='add_category'),
    path('add_sub_category/<str:pk>', views.add_sub_category, name='add_sub_category'),

    path('edit_product/<str:pk>', views.edit_product, name = 'edit_product'),
    path('edit_category/<str:pk>', views.edit_category, name = 'edit_category'),
    path('edit_sub_category/<str:pk>', views.edit_sub_category, name = 'edit_sub_category'),


    path('delete_product/<str:pk>', views.delete_product, name='delete_product'),
    path('delete_category/<str:pk>', views.delete_category, name='delete_category'),
    path('delete_sub_category/<str:pk>', views.delete_sub_category, name='delete_sub_category'),
]


