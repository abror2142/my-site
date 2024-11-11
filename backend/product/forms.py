from django import forms

from .models import Brand, Company, Product, ProductColor, ProductCategory, ProductImage, ProductImageSet, ProductMemory, ProductSize, ProductVariant, ProductVariantCustomCharacter, CustomCharacter, CustomCharacterOption


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']

    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']

class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductColorForm(forms.ModelForm):
    class Meta:
        model = ProductColor
        fields = ['name', 'code']


class ProductMemoryForm(forms.ModelForm):
    class Meta:
        model = ProductMemory
        fields = ['label']


class ProductImageSetForm(forms.ModelForm):
    class Meta:
        model = ProductImageSet
        fields = '__all__'


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSizeForm(forms.ModelForm):
    class Meta:
        model = ProductSize
        fields = '__all__'


class CustomCharacterForm(forms.ModelForm):
    class Meta:
        model = CustomCharacter
        fields = '__all__'

        
class CustomCharacterOptionForm(forms.ModelForm):
    class Meta:
        model = CustomCharacterOption
        fields = '__all__'


class ProductVariantCustomCharacterForm(forms.ModelForm):
    class Meta:
        model = ProductVariantCustomCharacter
        fields = '__all__'
