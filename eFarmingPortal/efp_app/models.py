from django.db import models

# Create your models here.
class Admin(models.Model):
    adminID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=255)
    role = models.CharField(max_length=45)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Farmer(models.Model):
    farmerID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=255)
    role = models.CharField(max_length=45)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Customer(models.Model):
    customerID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=255)
    role = models.CharField(max_length=45)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

class Product(models.Model):
    productID=models.AutoField(primary_key=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    farmerID = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.FloatField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)