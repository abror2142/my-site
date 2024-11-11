from django.urls import path

from .views import product_create_view


urlpatterns = [
    path('create/', product_create_view, name="product-create"),
]
