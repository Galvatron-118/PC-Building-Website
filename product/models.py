from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class cpu(models.Model):
    product_image= models.ImageField(upload_to='static/images/',null=True,blank=True)
    name=models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    stock=models.CharField(max_length=15)
    def __str__(self):
        return self.name


class cpucooler(models.Model):
    product_image= models.ImageField(upload_to='static/images/',null=True,blank=True)
    name=models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    stock=models.CharField(max_length=15)
    def __str__(self):
        return self.name
    
class motherboard(models.Model):
    product_image= models.ImageField(upload_to='static/images/',null=True,blank=True)
    name=models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    stock=models.CharField(max_length=15)
    def __str__(self):
        return self.name
    
class memory(models.Model):
    product_image= models.ImageField(upload_to='static/images/',null=True,blank=True)
    name=models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    stock=models.CharField(max_length=15)
    def __str__(self):
        return self.name
    
class storage(models.Model):
    product_image= models.ImageField(upload_to='static/images/',null=True,blank=True)
    name=models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    stock=models.CharField(max_length=15)
    def __str__(self):
        return self.name
    
class videocard(models.Model):
    product_image= models.ImageField(upload_to='static/images/',null=True,blank=True)
    name=models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    stock=models.CharField(max_length=15)
    def __str__(self):
        return self.name
    
class case(models.Model):
    product_image= models.ImageField(upload_to='static/images/',null=True,blank=True)
    name=models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    stock=models.CharField(max_length=15)
    def __str__(self):
        return self.name
    
class powersupply(models.Model):
    product_image= models.ImageField(upload_to='static/images/',null=True,blank=True)
    name=models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    stock=models.CharField(max_length=15)
    def __str__(self):
        return self.name
    

    
