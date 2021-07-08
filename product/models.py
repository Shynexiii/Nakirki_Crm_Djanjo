from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 255, null = True)
    slug = models.SlugField(max_length = 255, null = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)


    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Categories"

class SubCategory(models.Model):
    name = models.CharField(max_length = 255, null = True)
    slug = models.SlugField(max_length = 255, null = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "SubCategories"

class Product(models.Model):

    AVAILABILITY = (
        ('Disponible', 'Disponible'),
        ('Non disponible', 'Non disponible'),
    )

    name = models.CharField(max_length = 255, null = True, verbose_name='Nom')
    reference = models.CharField(max_length = 255, null = True, verbose_name='Référence')
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, verbose_name='Catégorie')
    sub_category = models.ForeignKey(SubCategory, on_delete = models.SET_NULL, null = True, verbose_name='Sous catégorie')
    buy_price = models.FloatField(null = True, verbose_name="Prix d'achat")
    sell_price = models.FloatField(null = True, verbose_name='Prix de vente')
    image = models.CharField(max_length = 255, null = True, verbose_name='Image')
    availability = models.CharField(max_length = 255, null = True, choices = AVAILABILITY, verbose_name='Disponibilité')
    created_at = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.name
