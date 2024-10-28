from django.urls import path, include
from .views import profile

urlpatterns = [
    path('', include('allauth.urls')),
    path('', include('allauth.socialaccount.urls')),
    path('profile/', profile, name='profile_page'),
]
