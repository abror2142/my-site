from django.contrib import admin
from .models import Category, Product, ProductCategory, ProductImage, ProductVariant, Brand, Company, ProductColorOption


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


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']
    list_display_links = ['product']


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'product']
    list_display_links = ['name', 'product']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']

@admin.register(ProductColorOption)
class ProductColorOptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']
    list_display_links = ['name', 'code']