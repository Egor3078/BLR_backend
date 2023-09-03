from django.db import models
from django.contrib.auth import models as auth_models


class UserManager(auth_models.BaseUserManager):

    def create_user(self, first_name: str, last_name: str, email: str, password: str = None, is_staff=False, is_superuser=False) -> "User":
        if not email:
            raise ValueError("You must have email")
        if not first_name:
            raise ValueError("You must have first_name")
        if not last_name:
            raise ValueError("You must have last_name")

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(self, first_name: str, last_name: str, email: str, password: str) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save()

        return user


class User(auth_models.AbstractUser):
    email = models.CharField(verbose_name="email", max_length=250, unique=True)
    password = models.CharField(max_length=250)
    first_name = models.CharField(verbose_name="first_name", max_length=250, unique=True)
    last_name = models.CharField(verbose_name="last_name", max_length=250, unique=True)
    username = None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

   # def __str__(self):
    #    return "username: {}, password: {}, first_name: {}, last_name: {}".format(self.username, self.password,
     #                                                                          self.first_name, self.last_name)

