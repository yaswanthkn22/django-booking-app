from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
# Create your models here.

class Customer(AbstractUser):
    
    email = models.EmailField(_('Email field'),unique=True)
    username = None
    dateOfBirth = models.DateField(blank=False)
    profileImg = models.ImageField(upload_to='images/',blank=True)
    mobileNumber = models.CharField(max_length=10,null=True,default='Not Provided')
    gender_choices = [('M','Male'),('F','Female'),('O','others')]
    gender = models.CharField(max_length=1, choices=gender_choices, null=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['dateOfBirth']


    def __str__(self):

        return self.email



class Owner(models.Model):

    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    



class House(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    houseId = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False,default='House')
    country = models.CharField(max_length=200, blank=False, default='India')
    state = models.CharField(max_length=200, blank=False)
    district = models.CharField(max_length=200, blank=False)
    nearestTown = models.CharField(max_length=200, blank=False)
    aminities = models.CharField(max_length=500, blank=True)

    pricePerDay = models.IntegerField(blank=False)
    bookingStart = models.DateField(null=True,blank=True)
    bookingEnd = models.DateField(null=True,blank=True)
    

class HouseImg(models.Model):
    imgId = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to='images/')
    houseId = models.ForeignKey(House, on_delete=models.CASCADE)
    


class Booking(models.Model):

    bookingId = models.BigAutoField(primary_key=True)
    userId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    houseId = models.ForeignKey(House, on_delete=models.CASCADE)
    bookingStart = models.DateTimeField(blank=False)
    bookingEnd = models.DateTimeField(blank=False)
    numberOfAdults = models.IntegerField(blank=False, default=0)
    numberOfChild = models.IntegerField(blank=False, default=0)


class Review(models.Model):

    reviewId = models.BigAutoField(primary_key=True)
    HouseId = models.ForeignKey('House', on_delete=models.CASCADE)
    userId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.FloatField(blank=False)
    comment = models.CharField(max_length=400)


