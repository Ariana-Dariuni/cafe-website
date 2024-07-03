from django.db import models # type:ignore
from django.contrib.auth.models import User # type:ignore


class Costumer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=255,null=True)
    password = models.CharField(max_length=255,null=True)
    phone_number = models.IntegerField(null=True)

    def __str__(self):
        return self.username


class Admin(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=255)
    sugar = models.IntegerField()
    coffee = models.IntegerField()
    flour = models.IntegerField()
    chocolate = models.IntegerField()
    egg = models.IntegerField()
    vertical = models.BinaryField(max_length=1)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_amount = models.IntegerField()
    type = models.BinaryField(max_length=1)
    date_orderd=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.order_id)


class OrdersProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,blank=True,null=True)

    date_aded=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.order.order_id} - Product {self.product.name}'


class UsersOrders(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order {self.order.order_id} - Product {self.user.username}'


class Storage(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()

    def __str__(self):
        return self.name
