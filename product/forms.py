from django.forms import ModelForm
from .models import Category, SubCategory, Product


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategoryForm(ModelForm):
    class Meta:
        model = SubCategory
        fields = "__all__"

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"