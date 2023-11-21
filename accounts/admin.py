from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import MyUser, Analyst, Hod, Management
from accounts.forms import UserCreationForm, UserChangeForm

# Register your models here.


class UserAdmin(BaseUserAdmin):
    # form = UserChangeForm
    # add_form = UserCreationForm

    list_display = ("email",)
    ordering = ("email",)  # Use the actual field in your model

    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "password",
                ],
            },
        ),
        ("Personal info", {"fields": ["first_name", "last_name", "phone"]}),
        (
            "Permissions",
            {
                "fields": [
                    "is_superuser",
                    "is_staff",
                    "is_management",
                    "is_analyst",
                    "is_hod",
                    "is_active",
                ]
            },
        ),
        ("Permission", {"fields": ["groups", ]}),
    ]

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2"],
            },
        ),
        ("Personal info", {"fields": ["first_name", "last_name", "phone"]}),
        (
            "Permissions",
            {
                "fields": [
                    "is_superuser",
                    "is_staff",
                    "is_management",
                    "is_analyst",
                    "is_hod",
                    "is_active",
                ]
            },
        ),
        ("Permission", {"fields": ["groups", ]}),
    ]


class AnalystAdmin(UserAdmin):
    list_display = ("email",)
    ordering = ("email",)  # Use the actual field in your model


admin.site.register(MyUser, UserAdmin)
admin.site.register(Analyst, AnalystAdmin)
