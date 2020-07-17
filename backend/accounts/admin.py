from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Fields",
            {
                "fields": (
                    "avatar",
                    "bio",
                    "birthdate",
                    "gender",
                    "superhost",
                    "nickname",
                )
            },
        ),
    )
    list_filter = (
        UserAdmin.list_filter + (
            "superhost",
        )
    )
    list_display = (
        "username",
        "email",
        "superhost",
        "is_staff",
        "is_active",
        "is_superuser",
    )
