from django.contrib import admin
from order.models import Basket, OrderDetail

# Register your models here.

admin.site.register(OrderDetail)


@admin.register(Basket)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ("owner", 'is_paid', 'payment_date', 'user_selected_delivery_time', 'delivery_time',
                       'delivery_image', 'address')
    exclude = ('status',)
