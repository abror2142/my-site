from django.contrib.auth import get_user_model

from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import UserInfo

User = get_user_model()

@receiver(user_signed_up)
def social_signal(request, sociallogin, **kwargs):
    picture = sociallogin.account.extra_data['picture']
    user_id = sociallogin.account.user_id
    print('-'*100, user_id)
    user = User.objects.get(pk=user_id)
    print("-"*100)
    print(picture, user_id, user)
    user_info, created = UserInfo.objects.get_or_create(user=user, pictureURL=picture)

    print("-"*100, user_info)
