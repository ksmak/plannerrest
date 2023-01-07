from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birth_date = models.DateField(
        verbose_name='день рождения',
        blank=True,
        null=True,
    )

    management = models.CharField(
        verbose_name='организация',
        max_length=150,
        blank=True,
        null=True,

    )

    department = models.CharField(
        verbose_name='подразделение',
        max_length=150,
        blank=True,
        null=True,
    )

    job = models.CharField(
        verbose_name='должность',
        max_length=150,
        blank=True,
        null=True,
    )
