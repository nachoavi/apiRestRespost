from django.db import models


# Create your models here.
class ProductsInventory(models.Model):
    name = models.CharField(max_length=100,null=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=False)
    description = models.TextField(max_length=200,null=True)
    stock = models.PositiveIntegerField(null=False)
    
    def __str__(self):
        return self.name
    
    
class Client(models.Model):
    name = models.CharField(max_length=50,null=False)
    lastName = models.CharField(max_length=50,null=False)
    telephone = models.CharField(max_length=16,null=False)
    
class Roles(models.TextChoices):
    ADMINISTRATOR = 'Admin'
    NORMAL_USER = 'Normal User'

class Collaborator(models.Model):
    name = models.CharField(max_length=50,null=False)
    lastName = models.CharField(max_length=50,null=False)
    telephone = models.CharField(max_length=16,null=False)
    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.NORMAL_USER
    )
    username = models.CharField(max_length=25,null=False)
    password = models.CharField(max_length=30,null=False)
    
    def __str__(self):
        return self.username
    
class Sales(models.Model):
    date = models.DateTimeField(auto_now_add=True,null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE,null=False)
    
class SalesDetails(models.Model):
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE,null=False)
    product = models.ForeignKey(ProductsInventory,on_delete=models.CASCADE,null=False)
    amount = models.PositiveIntegerField(null=False)
    totalPrice = models.DecimalField(max_digits=10,decimal_places=2,null=False)
    

    
    
     