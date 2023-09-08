from django.contrib import admin
from .models import ProductsInventory,Client,Sales,SalesDetails

# Register your models here.
admin.site.register(ProductsInventory)
admin.site.register(Client)
admin.site.register(Sales)
admin.site.register(SalesDetails)

