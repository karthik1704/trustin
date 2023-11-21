from django.contrib.auth.models import BaseUserManager
from django.db import models


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
        queryset = queryset.filter(is_hod=True)
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
        queryset = queryset.filter(is_analyst=True)
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
        queryset = queryset.filter(is_management=True)
        return queryset
