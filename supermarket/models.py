from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from MarketDelivery.utillits import upload_path


# Create your models here.


def banner_upload(instance, filepath):
    return upload_path(instance, filepath, instance.__class__.__name__, "banner")


def product_main_image_upload(instance, filepath):
    return upload_path(instance, filepath, instance.__class__.__name__, f"product{instance.id}")


def product_gallery_upload(instance, filepath):
    return upload_path(instance, filepath, instance.__class__.__name__, f"product/gallery{instance.id}")


class SuperMarket(models.Model):
    admin = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="superMarkets")
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=256)
    banner = models.ImageField(upload_to=banner_upload)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, null=True, blank=False)
    image = models.ImageField(upload_to=product_main_image_upload, null=True, blank=False)

    def __str__(self):
        return self.title


class Product(models.Model):
    super_market = models.ForeignKey(SuperMarket, on_delete=models.CASCADE, related_name="products")
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    Number_of_inventory = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to=product_main_image_upload, null=True, blank=False)
    active = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse(
            "supermarket:products-detail",
            kwargs={
                "pk": self.pk
            }
        )

    @property
    def category_list(self):
        a = ''
        for category in self.categories.all():
            a += category.title
        return a

class ProductGallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=product_gallery_upload)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
