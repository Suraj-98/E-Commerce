from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from django.utils.text import slugify


class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)

class Sub_Category(models.Model):
    id=models.AutoField(primary_key=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)

class Brand(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    availablity=(('In Stock','In Stock'),('Out Of Stock','Out Of Stock'))

    id=models.AutoField(primary_key=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    sub_category=models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=80 ,null=True)
    image=models.ImageField(upload_to="media")
    available=models.CharField(choices=availablity,null=True,max_length=200)
    price=models.CharField(max_length=50,null=True)
    date_created=models.DateTimeField(auto_now_add=True ,null=True)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return str(self.name)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args,**kwargs)


class UpdateProfileImage(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image=models.ImageField(upload_to="media", default="4568172.jpg")
    bio=models.CharField(max_length=250, null=True)
    mobile_no=models.CharField(max_length=13,null=True)
    date_created=models.DateTimeField(auto_now_add=True ,null=True)

    def __str__(self):
        return f"{self.user} profile"

class Order(models.Model):

    choices = (('Received', 'Received'),
        ('Scheduled', 'Scheduled'), 
        ('Shipped', 'Shipped'),
        ('In Progress','In Progress'),
        )

    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to="media",null=True)
    product=models.CharField(max_length=1000,null=True)
    quantity=models.CharField(max_length=5,null=True,blank=True)
    price=models.IntegerField(null=True)
    total=models.IntegerField(null=True)
    address=models.CharField(max_length=500,null=True)
    state=models.CharField(max_length=500,null=True)
    mobile_no=models.CharField(max_length=13,null=True)
    zipcode=models.CharField(max_length=6,null=True)
    status=models.CharField(max_length = 500, choices = choices ,default="In Progress")
    deliver_date=models.DateTimeField(auto_now_add=False,null=True)
    date_created=models.DateTimeField(auto_now_add=True ,null=True)

    def __str__(self):
        return str(self.product)

class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=1000,null=True)
    email=models.EmailField(null=True)
    subject=models.CharField(max_length=1000,null=True)
    message=models.CharField(max_length=1000,null=True)
    date_created=models.DateTimeField(auto_now_add=True ,null=True)

    def __str__(self):
        return str(self.email)

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    wished_item = models.ForeignKey(Product,on_delete=models.CASCADE)
    slug = models.CharField(max_length=30,null=True,blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.wished_item.name)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.wished_item.name)
        super(Wishlist,self).save(*args,**kwargs)