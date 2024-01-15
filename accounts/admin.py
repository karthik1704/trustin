from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import MyUser, Analyst, Hod, Management, Marketing
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
                    "role",
                    "is_superuser",
                    "is_staff",
                 
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
                    'role',
                    "is_superuser",
                    "is_staff",
                  
                ]
            },
        ),
        ("Permission", {"fields": ["groups", ]}),
    ]


class AnalystAdmin(UserAdmin):
    list_display = ("email",)
    ordering = ("email",)  # Use the actual field in your model
class HodAdmin(UserAdmin):
    list_display = ("email",)
    ordering = ("email",)  # Use the actual field in your model
class ManagementAdmin(UserAdmin):
    list_display = ("email",)
    ordering = ("email",)  # Use the actual field in your model
class MarketingAdmin(UserAdmin):
    list_display = ("email",)
    ordering = ("email",)  # Use the actual field in your model
    read_only_fields = ('role',)


admin.site.register(MyUser, UserAdmin)
admin.site.register(Analyst, AnalystAdmin)
admin.site.register(Hod, HodAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Marketing, MarketingAdmin)
