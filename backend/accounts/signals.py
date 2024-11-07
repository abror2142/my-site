import requests
from django.core import files
from io import BytesIO

from django.contrib.auth import get_user_model

from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import UserInfo

"""
    AIM: To store image came as response from the Social Login Option.

    STEPS:  a) Login/Signup with Social Provider 
            b) Use user_signup_signal to do have a chance to save the image
                WHY user_signup_signal? Signal will be triggered when the user 
                first time sign up into his/her account, it doesn't metter whether
                he uses simple sign up or social signup function. If he uses social 
                sign in(we'll have sociallogin as a valid argument) and new account is created,
                we can use the info in sociallogin to get the user image.
            c) GET the ImageURL provided in sociallogin argument
            d) FETCH the image 
            e) POPULATE the UserInfo field with ifetched image and other user details
    ** Using social login signal won't work as when this signal triggered, 
    socialaccount object will be created but the User object won't be created which means
    we can't create UserInfo object for the user! 
"""

User = get_user_model()

@receiver(user_signed_up)
def social_sigup_handler(request, sociallogin, user, **kwargs):
    # Only if the user signs in with sociallogin option,
    # We can get the imageURL from the provider, otherwise skip
    if sociallogin:
        # Get User ID for the Successfully Signed in user
        user_id = sociallogin.account.user_id
        # The User object will already be created here. 
        user = User.objects.get(pk=user_id)
        
        # Get details about user from the provider
        provider = sociallogin.account.provider
        if provider == 'google':
            first_name = sociallogin.account.extra_data['given_name']
            last_name = sociallogin.account.extra_data['family_name']

        # Here in first-time registration, UserInfo object won't be created
        # So we create it with the user details
        user_info, created = UserInfo.objects.get_or_create(user=user, first_name=first_name, last_name=last_name)

        # Get the image URL and request it
        pictureURL = sociallogin.account.extra_data['picture']
        response = requests.get(pictureURL)

        # If reponse is ok, save else just skip.
        if response.status_code == requests.codes.ok:
            fp = BytesIO()
            fp.write(response.content)
            file_name = f"{user}_{provider}.jpg" 
            user_info.image.save(file_name, files.File(fp))