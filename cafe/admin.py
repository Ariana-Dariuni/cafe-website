from django.contrib import admin # type:ignore
from .models import Costumer, Admin, Product, Order, OrdersProduct, UsersOrders, Storage

admin.site.register(Costumer)
admin.site.register(Admin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrdersProduct)
admin.site.register(UsersOrders)
admin.site.register(Storage)

