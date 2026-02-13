from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, World!')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/index.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'catalog/index2.html', {'product': product})
