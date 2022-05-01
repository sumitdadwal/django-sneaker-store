from django.db import models
from django.utils.html import mark_safe

class Banner(models.Model):
    img = models.ImageField(upload_to='static/banner_imgs/')
    alt_text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "7. Banners"

class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="static/cat_imgs/")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "1. Categories"

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))



class Brand(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="static/brand_imgs/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "2. Brands"

class Color(models.Model):
    title = models.CharField(max_length=50)
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def color_display(self):
        return mark_safe('<div style="width:50px; height:50px; background:%s" />' % (self.color_code))

    class Meta:
        verbose_name_plural = "4. Colors"

class Size(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "5. Sizes"

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=400)
    detail = models.TextField()
    specs = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "3. Products"

class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to="static/product_imgs/", null=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name_plural = "6. ProductAttributes"
    