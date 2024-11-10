from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=150)
    short_description = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey(to="self", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'ProductCategories'

    def __str__(self):
        return f"{self.category} {self.product}"


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    short_description = models.CharField(max_length=255)
    full_description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    produced_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product")

    def __str__(self):
        return f"{self.product}"