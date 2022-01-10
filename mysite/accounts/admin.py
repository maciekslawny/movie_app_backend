from accounts.models import CustomUser
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminPrimary
from django.db import models
from django.forms import CharField, Textarea, TextInput


@admin.register(CustomUser)
class UserAdmin(UserAdminPrimary):
    model = CustomUser
    search_fields = (
        "email",
        "first_name",
    )
    list_filter = ("email", "first_name", "is_active", "is_staff")
    ordering = ("email",)
    list_display = ("email", "id", "first_name", "is_active", "is_staff")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "first_name",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})},
    }
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "user_name",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )
