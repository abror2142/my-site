from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import UserInfo
# Register your models here.

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'email']
    list_display_links = ['username']


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'pictureURL']
    list_display_links = ['user']