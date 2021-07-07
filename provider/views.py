from django.shortcuts import render, redirect, reverse
from .models import Provider
from .forms import ProviderForm

def list_provider(request):
    providers = Provider.objects.all()
    context = {
        'providers' : providers
    }
    return render(request, 'provider/index.html', context)

def view_provider(request, pk):
    provider = Provider.objects.get(pk = pk)
    context = {
        'provider' : provider
    }
    return render(request, 'provider/view_provider.html', context)

def add_provider(request):
    form = ProviderForm()
    if request.method == "POST":
        form = ProviderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('provider:list_provider'))
    context = {
        'form' : form
    }
    return render(request, 'provider/form_provider.html', context)

def edit_provider(request, pk):
    provider = Provider.objects.get(pk = pk)
    form = ProviderForm(instance = provider)
    if request.method == "POST":
        form = ProviderForm(request.POST, instance = provider)
        if form.is_valid():
            form.save()
            return redirect(reverse('provider:view_provider', args=[pk]))
    context = {
        'form' : form
    }
    return render(request, 'provider/form_provider.html', context)

def delete_provider(request, pk):
    provider = Provider.objects.get(pk=pk)
    provider.delete()
    return redirect('provider:index')