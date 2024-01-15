from django.contrib.auth.models import BaseUserManager
from django.db import models

from accounts.config import ROLE_ANALYST, ROLE_ADMIN, ROLE_CHOICES, ROLE_HOD,ROLE_MANAGEMENT, ROLE_MARKETING


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not password:
            raise ValueError("Password is must !")

        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class HodManager(models.Manager):
    def create_user(self, email, password=None):
        email = email.lower()
        user = self.model(email=email)
        user.is_staff = True

        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(role=ROLE_HOD)
        return queryset


class AnalystManager(models.Manager):
    def create_user(self, email, password=None):
        email = email.lower()
        user = self.model(email=email)
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(role=ROLE_ANALYST)
        return queryset

class ManagementManager(models.Manager):
    def create_user(self, email, password=None):
        email = email.lower()
        user = self.model(email=email)
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(role=ROLE_MANAGEMENT)
        return queryset
    
class MarketingManager(models.Manager):
    def create_user(self, email, password=None):
        email = email.lower()
        user = self.model(email=email)
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(role=ROLE_MARKETING)
        return queryset
