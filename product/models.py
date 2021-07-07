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

    name = models.CharField(max_length = 255, null = True)
    reference = models.CharField(max_length = 255, null = True)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True)
    sub_category = models.ForeignKey(SubCategory, on_delete = models.SET_NULL, null = True)
    buy_price = models.FloatField(null = True)
    sell_price = models.FloatField(null = True)
    image = models.CharField(max_length = 255, null = True)
    availability = models.CharField(max_length = 255, null = True, choices = AVAILABILITY)
    created_at = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.name
