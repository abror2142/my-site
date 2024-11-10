from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=150)
    short_description = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logo', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    

class BrandCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'BrandCompany'

    def __str__(self):
        return f"{self.brand} {self.company}"


class Category(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey(to="self", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    brand_company = models.ForeignKey(BrandCompany, on_delete=models.SET_NULL, null=True, blank=True)

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


class ProductColorOption(models.Model):
    product_variant = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=7)

    def __str__(self):
        return self.name
    

class ProductImage(models.Model):
    product = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    color_option = models.ForeignKey(ProductColorOption, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product")

    def __str__(self):
        return f"{self.product}"