from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """
    extended model of users
    """
    phone_num = models.CharField(verbose_name="Mobile", max_length=10, validators=[MinLengthValidator(10)], null=True,
                                 blank=False)
    phone = models.CharField(verbose_name="Phone", max_length=30, blank=False)
    birthdate = models.DateField(verbose_name="Date of birth", null=True, blank=False)
    person_pic = models.ImageField(verbose_name="Profile picture", upload_to='profile-pic/%Y/%m/%d/', blank=True)
    postal_code = models.CharField(verbose_name="Postal code", max_length=7, blank=False)
    address = models.TextField(verbose_name="Address", blank=False)
    Customer = 'CU'
    SuperMarketAdmin = 'SMA'
    Driver = 'DR'
    Delivery = 'DLV'
    USER_TYPES = [
        (Customer, 'Customer'),
        (SuperMarketAdmin, 'Super Market Admin'),
        (Driver, 'Driver'),
        (Delivery, 'Delivery'),
    ]
    USER_TYPE = models.CharField("User type", choices=USER_TYPES, max_length=3, default=Customer)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    @property
    def get_full_name(self):
        return self.first_name + " " + self.last_name
