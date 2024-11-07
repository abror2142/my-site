from django import forms
from .models import UserInfo


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['first_name', 'middle_name', 'last_name', 'date_of_birth', 'phone_number', 'gender', 'image']
