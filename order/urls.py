from django.urls import path
from order import views

app_name = "order"

urlpatterns = [
    path("add-to-basket/", views.add_user_order, name="add-to-basket"),
    path('remove-order-detail/<detail_id>', views.remove_order_detail, name="remover-order-detail"),
    path("basket/", views.basket, name="basket"),
    path('payment/<basket_id>', views.fake_payment, name="payment"),
    path('payment-done/<int:basket_id>', views.fake_payment_done, name="payment_done"),
]
