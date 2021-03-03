from django.db import models


class Product(models.Model):
    '''     
    Products - Each product corresponds to a real world product you can buy 

    id: The type is up to you :-) 
    name : string 
    description: string 
    '''

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    class Meta:
        verbose_name_plural = 'products'
    
    def __str__(self):
        return self.name



class Offer(models.Model):
    '''     
    Offers - Each offer represents a product offer being sold for some price somewhere 
    
    id: The type is up to you :-) 
    price : integer 
    items_in_stock: integer 
    '''

    id = models.AutoField(primary_key=True)
    price = models.PositiveIntegerField()
    items_in_stock = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, related_name='offers')

    class Meta:
        verbose_name_plural = 'offers'
    
    def __str__(self):
        return str(self.id)