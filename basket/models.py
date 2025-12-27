from django.db import models
from products.models import Product
# Create your models here.


class Basket(models.Model):
    total_flipkart = models.IntegerField( default=0)
    total_jiomart = models.IntegerField( default=0)
    total_amazon = models.IntegerField( default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Cart id: {}".format(self.id)


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, null=True, blank=True, on_delete=models.CASCADE)
    # Basket foriegn key
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    product_total = models.IntegerField(default=1)
    # product total
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        try:
            return str(self.basket.id)
        except AttributeError:
            return self.product.name
