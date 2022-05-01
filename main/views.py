from turtle import title
from django.http import JsonResponse
from django.shortcuts import render
from .models import Brand, Category, Product, ProductAttribute, Banner
from django.template.loader import render_to_string

def home(request):
    banners = Banner.objects.all().order_by('-id')
    featured_products = Product.objects.filter(is_featured=True).order_by('-id')
    return render(request, 'index.html', {'featured_products': featured_products, 'banners': banners})

def category_list(request):
    categories = Category.objects.all().order_by('-id')
    return render(request, 'category_list.html', {'categories': categories})

def brand_list(request):
    brands = Brand.objects.all().order_by('-id')
    return render(request, 'brand_list.html', {'brands': brands})

def product_list(request):
    total_products = Product.objects.count()
    products = Product.objects.all().order_by('-id')[:2]

    return render(request, 'product_list.html', 
        {
            'total_products':total_products,
            'products': products, 
        }
    )

def category_product_list(request, category_id):
    category = Category.objects.get(id=category_id)
    category_products = Product.objects.filter(category=category).order_by('-id')

    return render(request, 'category_product_list.html', {
        'category': category,
        'category_products': category_products, 
    })

def brand_product_list(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    brand_products = Product.objects.filter(brand=brand).order_by('-id')

    return render(request, 'brand_product_list.html', {
        'brand': brand,
        'brand_products': brand_products, 
    })

def product_detail(request, slug, id):
    product_detail = Product.objects.get(id=id)
    related_products = Product.objects.filter(category=product_detail.category).exclude(id=id)[:4]
    colors = ProductAttribute.objects.filter(product=product_detail).values('color__id', 'color__title', 'color__color_code', 'price').distinct()
    sizes = ProductAttribute.objects.filter(product=product_detail).values('size__id', 'size__title', 'price', 'color__id').distinct()
    return render(request, 'product_detail.html', {'product_detail': product_detail, 'related_products': related_products, 'colors':colors, 'sizes':sizes})

def search(request):
    q = request.GET['q']
    featured_products = Product.objects.filter(title__contains=q).order_by('-id')
    return render(request, 'search.html', {'featured_products': featured_products})

def filter_data(request):
    colors=request.GET.getlist('color[]')
    categories=request.GET.getlist('color[]')
    brands=request.GET.getlist('color[]')
    sizes=request.GET.getlist('color[]')
    allProducts = Product.objects.all()
    t=render_to_string('ajax/product-list', {'data':allProducts})
    return JsonResponse({'data': t})

def load_more_data(request):
    offset = int(request.GET['offset'])
    limit = int(request.GET['limit'])
    products = Product.objects.all().order_by('-id')[offset:offset+limit]

    t=render_to_string('ajax/product-list.html', {'products':products})
    return JsonResponse({'data': t})