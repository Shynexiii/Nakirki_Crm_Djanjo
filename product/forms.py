from django.forms import ModelForm, TextInput, Select, NumberInput
from .models import Category, SubCategory, Product


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name","slug"]
        widgets = {
            'name' : TextInput(attrs={'class':'form-control'}),
            'slug': TextInput(attrs={'class': 'form-control'})
        }



class SubCategoryForm(ModelForm):
    class Meta:
        model = SubCategory
        fields = ["name", "slug", "category"]
        widgets = {
            'name' : TextInput(attrs={'class':'form-control'}),
            'slug' : TextInput(attrs={'class': 'form-control'}),
            'category' : Select(attrs={'class': 'form-control'}),
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'reference', 'category', 'sub_category', 'buy_price', 'sell_price', 'image', 'availability']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'reference': TextInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'sub_category': Select(attrs={'class': 'form-control'}),
            'buy_price': NumberInput(attrs={'class': 'form-control'}),
            'sell_price': NumberInput(attrs={'class': 'form-control'}),
            'image': TextInput(attrs={'class': 'form-control'}),
            'availability': Select(attrs={'class': 'form-control'}),
        }