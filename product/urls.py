from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('index', views.index, name = 'index')
]