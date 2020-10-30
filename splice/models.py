from django.db import models

# Create your models here.

class vendor(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    companyName = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    telephone = models.CharField(max_length=12)
    addressline1=models.CharField(max_length=100)
    addressline2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    postalzip=models.CharField(max_length=10)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=100)

class bidder(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    companyName = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    telephone = models.CharField(max_length=12)
    addressline1=models.CharField(max_length=100)
    addressline2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    postalzip=models.CharField(max_length=10)
    country=models.CharField(max_length=50)
    state=models.CharField(max_length=100)