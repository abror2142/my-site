from django.shortcuts import render


from .forms import  Category
from .forms import ProductCreateForm

def product_create_view(request):

    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            category_option_id = form.cleaned_data['category_option']
            category_custom_option = form.cleaned_data['category_custom']
            if category_option_id:
                try:
                    selected_option = Category.objects.get(id=category_option_id)
                    
                except:
                    Category.objects.create(name=category_custom_option)
                

    else:
        form = ProductCreateForm()

    state = {
        "form": ProductCreateForm()
    }

    return render(request, 'product_create_page.html', state)