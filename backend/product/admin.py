from django.contrib import admin
from .models import (Category, Product, ProductCategory, ProductVariant, 
                     Brand, Company, ProductColor, ProductImage, ProductImageSet, 
                     ProductMemory, ProductSize, ProductVariantCustomCharacter, 
                     CompanyBrand, CustomCharacter, CustomCharacterOption)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'category']
    list_display_links = ['product']


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'product']
    list_display_links = ['name', 'product']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']


@admin.register(CompanyBrand)
class CompanyBrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'brand']
    list_display_links = ['company', 'brand']


@admin.register(ProductColor)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']
    list_display_links = ['name']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
    list_display_links = ['id']


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'size', 'roman_label']
    list_display_links = ['size']


@admin.register(ProductMemory)
class ProductMemoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'label']
    list_display_links = ['label']


@admin.register(ProductImageSet)
class ProductImageSetAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_image']
    list_display_links = ['product_image']


@admin.register(CustomCharacter)
class CustomCharacterAdmin(admin.ModelAdmin):
    list_display = ['id', 'custom_character_name', 'description']
    list_display_links = ['custom_character_name']


@admin.register(CustomCharacterOption)
class CustomCharacterOptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'custom_character']
    list_display_links = ['custom_character']


@admin.register(ProductVariantCustomCharacter)
class ProductVariantCustomCharacterAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_variant', 'custom_character']
    list_display_links = ['product_variant', 'custom_character']

