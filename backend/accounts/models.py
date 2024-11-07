from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class RegionCountry(models.Model):
    region = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.region} {self.country}"


class Address(models.Model):
    address_line_1 = models.CharField(max_length=200, null=True, blank=True)
    address_line_2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    region = models.ForeignKey(RegionCountry, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.city} {self.region}"


# Custom User Model that excludes default fields 
class User(AbstractUser):
    first_name = None
    last_name = None


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to="user", blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} {self.first_name} {self.last_name}"