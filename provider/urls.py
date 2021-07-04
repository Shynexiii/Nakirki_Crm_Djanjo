from django.urls import path
from . import views

app_name = "provider"

urlpatterns = [
    path('index', views.index, name = "index"),
]