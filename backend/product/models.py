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
    

class CompanyBrand(models.Model):
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
    brand_company = models.ForeignKey(CompanyBrand, on_delete=models.SET_NULL, null=True, blank=True)
    added_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    produced_at = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'ProductCategories'

    def __str__(self):
        return f"{self.category} {self.product}"
    

class ProductColor(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    code = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.code}"


class ProductMemory(models.Model):
    label = models.CharField(max_length=150)

    def __str__(self):
        return self.label


class ProductSize(models.Model):
    size = models.CharField(max_length=5)
    roman_label = models.CharField(max_length=3)

    def __str__(self):
        return self.size


class ProductImage(models.Model):
    image = models.ImageField(upload_to="product")
    alt_text = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.image}"
    

class ProductImageSet(models.Model):
    product_image = models.ForeignKey(ProductImage, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}"
    

class CustomCharacter(models.Model):
    custom_character_name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.custom_character_name
    

class CustomCharacterOption(models.Model):
    custom_character = models.ForeignKey(CustomCharacter, on_delete=models.CASCADE)
    option = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.custom_character} {self.option}"
    

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    short_description = models.CharField(max_length=255)
    full_description = models.TextField(null=True, blank=True)
    color = models.ForeignKey(ProductColor, on_delete=models.SET_NULL, null=True, blank=True)
    memory = models.ForeignKey(ProductMemory, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.ForeignKey(ProductSize, on_delete=models.SET_NULL, null=True, blank=True)
    image_set = models.ForeignKey(ProductImageSet, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name
    

class ProductVariantCustomCharacter(models.Model):
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.SET_NULL, null=True)
    custom_character = models.ForeignKey(CustomCharacter, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.product_variant} {self.custom_character}"