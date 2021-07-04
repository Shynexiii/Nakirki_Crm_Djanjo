from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'provider/index.html', context)
