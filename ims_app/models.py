from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length = 300)
    username = models.CharField(max_length=200, default = 'username')# if ntg is send then it will be username
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
class Product_type(models.Model):
    product_category = models.CharField( max_length=350)
    
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)

class Department(models.Model):
    department_name = models.CharField(max_length=350)
    floor = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Product(models.Model):
    product_name = models.CharField( max_length=350)
    description = models.TextField()
    Product_type_id = models.ForeignKey('Product_type', on_delete = models.SET_NULL, null=True)
    quantity = models.IntegerField()
    department = models.ManyToManyField('Department') # fk ko class tala define cha vaneni fk model lai '' ma halda chalxa
    
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=350)
    supplier_email = models.EmailField(max_length=100)
    supplier_phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)   
    
class purchase(models.Model):
    product_id = models.ForeignKey('Product', on_delete = models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    Supplier_id = models.ForeignKey('Supplier', on_delete = models.SET_NULL, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=350)
    address = models.CharField(max_length=200,null=True)
    email = models.EmailField()
    
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Sell(models.Model):
    product = models.ForeignKey('Product', on_delete = models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    customer_id = models.ForeignKey('Customer', on_delete = models.SET_NULL, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
