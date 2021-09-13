from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers
    for authentication instead of usernames."
    """
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email field must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Wrapper method around _create_user() to create users with no admin privileges.
        """
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Wrapper method around _create_user() to create users with highest admin privileges.
        NB:
        DO NOT EXPOSE TO ANY PUBLIC ENDPOINT.
        Preferred way is  through a management command:
        $ python manage.py createsuperuser
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)