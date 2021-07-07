from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('fournisseur/', include('provider.urls')),
    path('produit/', include('product.urls')),
]