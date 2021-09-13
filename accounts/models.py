import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
        Other fields like first_name, last_lame, etc should not be placed
        in this table. This table should only be concerned with user
        authentication and permissions and other essential user-related
        activities.
    """
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    email_is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=True,
        help_text='Designates whether this user should be treated as active. '
                  'Make this false instead of deleting accounts. '
    )

    USERNAME_FIELD = 'email'
    objects = UserManager()

