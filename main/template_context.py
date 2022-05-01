from .models import Product, ProductAttribute

def get_filter(request):
    categories = Product.objects.distinct().values('category__title')
    brands = Product.objects.distinct().values('brand__title')
    colors = ProductAttribute.objects.distinct().values('color__title', 'color__id', 'color__color_code')
    sizes = ProductAttribute.objects.distinct().values('size__title', 'size__id')

    data= {
        'categories': categories,
        'brands': brands,
        'colors': colors,
        'sizes': sizes,
    }
    return data

#with the help of context processor we can show the common data in everypage easily