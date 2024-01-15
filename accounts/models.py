from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models import Avg
from django.utils.translation import gettext_lazy as _

from accounts.config import ROLE_ANALYST, ROLE_ADMIN, ROLE_CHOICES, ROLE_HOD,ROLE_MANAGEMENT, ROLE_MARKETING
from accounts.managers import (
    CustomUserManager,
    HodManager,
    AnalystManager,
    ManagementManager,
    MarketingManager
)

# Create your models here.
class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("e-mail"), unique=True,)
    phone = models.CharField(
        _("phone number"),
        unique=True,
        max_length=30,
    )

    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), blank=True, null=True, max_length=50)

    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    last_login = models.DateTimeField(_("last login"), auto_now=True)

    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("staff"), default=False)
    is_superuser = models.BooleanField(_("superuser"), default=False)

    role = models.CharField(_('Role'), choices=ROLE_CHOICES, default=ROLE_ADMIN)

  
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    # def get_email_field_name(self):
    #     return self.EMAIL_FIELD

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name if self.last_name  else ''}"

    def get_short_name(self):
        return self.first_name

    # def get_username(self):
    #     return self.username

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name if self.last_name  else ''}"

    # # this methods are require to login super user from admin panel
    # def has_perm(self, perm, obj=None):
    #     return self.is_staff

    # # this methods are require to login super user from admin panel
    # def has_module_perms(self, app_label):
    #     return self.is_staff


class Management(MyUser):
    class Meta:
        proxy = True

    objects = ManagementManager()

    def save(self, *args, **kwargs) -> None:
        self.role = ROLE_MANAGEMENT
        super().save(*args, **kwargs)


class Marketing(MyUser):
    class Meta:
        proxy = True

    objects = MarketingManager()

    def save(self, *args, **kwargs) -> None:
        self.role = ROLE_MARKETING
        super().save(*args, **kwargs)


class Hod(MyUser):
    class Meta:
        proxy = True

    objects = HodManager()

    def save(self, *args, **kwargs) -> None:
        self.role = ROLE_HOD
        super().save(*args, **kwargs)


class Analyst(MyUser):
    class Meta:
        proxy = True

    objects = AnalystManager()

    def save(self, *args, **kwargs) -> None:
        self.role = ROLE_ANALYST
        super().save(*args, **kwargs)
