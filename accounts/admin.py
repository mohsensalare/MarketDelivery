from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreate


# Register your models here.


class AdminUser(UserAdmin):
    model = User
    add_form = CustomUserCreate
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional data',
            {
                "fields": (
                    'USER_TYPE',
                    'phone_num',
                    'phone',
                    'birthdate',
                    'person_pic',
                    'postal_code',
                    'address'
                )
            }
        )
    )


admin.site.register(User, AdminUser)

