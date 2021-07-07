from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect

from .forms import CategoryForm, SubCategoryForm, ProductForm
from .models import Product, Category, SubCategory

def list_product(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request, 'product/index.html', context)

def add_product(request,):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('product:list_product'))
    context = {
        'form' : form
    }
    return render(request, 'product/form_product.html', context)

def add_category(request,):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('product:list_category'))
    context = {
        'form' : form
    }
    return render(request, 'category/form_category.html', context)

def add_sub_category(request, pk):
    form = SubCategoryForm(initial={'category' : pk })
    if request.method == "POST":
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('product:sub_category', args=[pk]))
    context = {
        'form' : form,
    }
    return render(request, 'category/form_category.html', context)

def edit_product(request, pk):
    product = Product.objects.get(pk = pk)
    form = ProductForm(instance = product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect(reverse('product:list_product'))
    context = {
        'form' : form
    }
    return render(request, 'product/form_product.html', context)

def list_category(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
    }
    return render(request, 'category/index.html', context)


def view_sub_category(request, pk):
    sub_categories = SubCategory.objects.filter(category_id=pk)
    context = {
        'category_id': pk,
        'sub_categories' : sub_categories,
    }
    return render(request, 'category/view_sub_category.html', context)


def edit_category(request, pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(instance = category)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance = category)
        if form.is_valid():
            form.save()
            return redirect('product:list_category')

    context = {
        'form' : form
    }
    return render(request, 'category/form_category.html', context)


def edit_sub_category(request, pk):
    sub_category = SubCategory.objects.get(pk=pk)
    form = SubCategoryForm(instance = sub_category)
    if request.method == "POST":
        form = SubCategoryForm(request.POST, instance = sub_category)
        if form.is_valid():
            form.save()
            return redirect(reverse('product:sub_category', args=[sub_category.category_id]))

    context = {
        'form' : form
    }
    return render(request, 'category/edit_category.html', context)

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('product:list_product')

def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('product:list_category')

def delete_sub_category(request, pk):
    sub_category = SubCategory.objects.get(pk=pk)
    sub_category.delete()
    return redirect(reverse('product:sub_category', args=[sub_category.category_id]))
