from django.urls import path
from supermarket import views

app_name = "supermarket"

urlpatterns = [
    path("products-list/", views.product_list, name="list-products"),
    path("supermarket-list/", views.category_list, name="category-list"),
    path("products-list/<slug>/<smid>", views.product_list, name="list-products-slug"),
    path("products-detail/<int:pk>/", views.product_detail, name="products-detail"),
    path("order_list/", views.order_list, name="order_list"),
]