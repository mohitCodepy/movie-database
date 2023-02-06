from django.contrib.auth.models import AbstractUser

from generics.generics import CreatedUpdatedMixin

from .managers import CustomUserManager


class User(CreatedUpdatedMixin, AbstractUser):

    """
    User
        Custom user for adding created_at and updated_at field.
    """

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.username
