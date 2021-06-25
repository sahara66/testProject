from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Product, Review


# Create your views here.

def hello_world(request):
    return HttpResponse(b'<h1>Hello WORLD!!!</h1>')


def index(request):
    category = Category.objects.all()
    data = {
        'title': 'Все продукты',
        'category': category
    }
    # for category in categorys:
    #     print(category.id, ':', category.name)
    return render(request, 'index.html', context=data)


def category_item(request, id): # 4
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category_id=id)
    data = {
        'category': category,
        'products': products
    }
    return render(request, 'products.html', context=data)


def products_item(request):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category_id=id)
    data = {
        'category': category,
        'products': products
    }
    return render(request, 'products.html', context=data)