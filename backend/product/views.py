from django.shortcuts import render


from .forms import ProductCategoryForm, ProductColorForm, ProductImageForm, ProductImageSetForm, ProductMemoryForm, ProductSizeForm, ProductVariantCustomCharacterForm, ProductForm, ProductVariantForm, CompanyForm, CustomCharacterForm, CustomCharacterOptionForm, BrandForm


def product_create_view(request):
    state = {
        "forms":  {
            "product_form": ProductForm(),
            "product_variant_form": ProductVariantForm(),
            "product_image_set_form": ProductImageSetForm(),
            "product_image_form": ProductImageForm(),
            "product_color_form": ProductColorForm(),
            "product_category_form": ProductCategoryForm(),
            "product_memory_form": ProductMemoryForm(),
            "product_size_form": ProductSizeForm(),
            "product_company_form": CompanyForm(),
            "product_brand_form": BrandForm(),
            "product__variant_custom_character_from": ProductVariantCustomCharacterForm(),
            "product_custom_character_form": CustomCharacterForm(),
            "product_custom_character_option_form": CustomCharacterOptionForm(), 
        },
    }

    return render(request, 'product_create_page.html', state)