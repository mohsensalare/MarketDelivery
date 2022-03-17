import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
from MarketDelivery.utillits import upload_path
from supermarket.models import Product
from accounts.models import User
# from location_field.models.spatial import LocationField
# from django.contrib.gis.geos import Point


def delivery_image_upload(instance, filepath):
    return upload_path(instance, filepath, instance.__class__.__name__, f"baskets/deliver-image-{instance.id}")


class Basket(models.Model):
    """
    user Basket model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="baskets")
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(blank=True, null=True)
    delivery = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_baskets", null=True, blank=True)
    user_selected_delivery_time = models.PositiveSmallIntegerField(blank=True, null=True)
    delivery_time = models.DateField(blank=True, null=True)
    delivery_image = models.ImageField(null=True, blank=True, upload_to=delivery_image_upload)
    address = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, default="1", blank=True)
    # location_point = LocationField(based_fields=['city'], default=Point(45.573083, -73.569587), null=True, blank=True,
    #                                zoom=4, verbose_name="deliver point")

    def __str__(self):
        return self.owner.username + " basket " + str(self.id) + str(self.delivery_time) + " hour" + \
               str(self.user_selected_delivery_time)

    @property
    def total_price(self):
        """
        calculation sum of price all products in Basket
        :return: sum of price all products in Basket
        """
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.product.price
        return amount


class OrderDetail(models.Model):
    """
    detail product in Basket
    """
    order = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    count = models.PositiveSmallIntegerField(null=False)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products", null=True,
                               blank=True)

    def detail_sum_price(self):
        return self.count * self.price

    def __str__(self):
        return self.order.owner.get_full_name + str(self.id)
