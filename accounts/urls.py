from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("register/", views.register, name="register"),
    path("log-out/", views.log_out, name="log-out"),
]
