from django.db import models

class promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    #returns product of particular field applied to 

class Collection(models.Model):
    collection_name = models.CharField(max_length=255)
    # Product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

    

    

class Product(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,max_length=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(promotion)



class customer(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique = True )
    phone = models.CharField(max_length=255)
    order = models.ForeignKey("Order", on_delete=models.SET_NULL)

class Order(models.Model):
    order_id = models.DecimalField( max_digits=5, decimal_places=2)
    item = models.ForeignKey('Item', on_delete=models.SET_NULL)

class cart(models.Model):
    item = models.ForeignKey('Item', on_delete=models.SET_NULL )

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    


class Cartitem(models.Model):
    cart = models.ForeignKey(cart , on_delete=models.CASCADE)
    Product = models.ForeignKey(Product , on_delete=models.CASCADE)



class address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(customer, on_delete=models.CASCADE, primary_key=True)# one adress with each customer with primary key
    # Create your models here.
