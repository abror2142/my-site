from django import forms

from .models import (Brand, Company, Category, Product, 
                     ProductColor, ProductCategory, ProductImage, 
                     ProductImageSet, ProductMemory, ProductSize, 
                     ProductVariant, ProductVariantCustomCharacter, 
                     CustomCharacter, CustomCharacterOption)


class ProductCreateForm(forms.Form):
    company_option = forms.ChoiceField(label="Choose", required=False)
    category_custom = forms.CharField(label="Add", required=False)
    brand_option = forms.ChoiceField(label="Choose", required=False)
    brand_custom = forms.CharField(label="Add", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        company_options = [(obj.id, obj.name) for obj in Category.objects.all()]
        company_options.insert(0, (-1, "Select a choice!"))
        brand_options = [(obj.id, obj.name) for obj in Brand.objects.filter()]
        self.fields['company_option'].choices = company_options

    def clean(self):
        cleaned_data = super().clean()
        company_option = cleaned_data.get('company_option')
        company_custom = cleaned_data.get('company_custom')

        if not company_custom and not company_option:
            raise forms.ValidationError("Please choose or enter a valid category name.")
        
        return cleaned_data
