from django.contrib import admin
from api.models import Offer, Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'description')
   
admin.site.register(Product, ProductAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('offer_id', 'price', 'items_in_stock')
   
admin.site.register(Offer, OfferAdmin)