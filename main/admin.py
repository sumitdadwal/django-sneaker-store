from django.contrib import admin
from .models import Category, Brand, Color, Size, Product, ProductAttribute, Banner

admin.site.register(Banner)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')
admin.site.register(Category, CategoryAdmin)


admin.site.register(Brand)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'color_display')
admin.site.register(Color, ColorAdmin)


admin.site.register(Size)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'brand', 'is_active', 'is_featured')
    list_editable=('is_active', 'is_featured')
admin.site.register(Product, ProductAdmin)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_tag', 'price', 'color', 'size')

admin.site.register(ProductAttribute, ProductAttributeAdmin)