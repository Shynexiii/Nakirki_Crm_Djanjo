from django.urls import path
from . import views

app_name = "provider"

urlpatterns = [
    path('index', views.list_provider, name = "list_provider"),
    path('add_provider', views.add_provider, name = "add_provider"),
    path('view_provider/<str:pk>', views.view_provider, name = "view_provider"),
    path('edit_provider/<str:pk>', views.edit_provider, name = "edit_provider"),
    path('delete_provider/<str:pk>', views.delete_provider, name='delete_provider'),
]