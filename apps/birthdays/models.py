# Python modules
import os
# Django modules
from django.db import models
from django.conf import settings
# Project modules
from abstracts.models import AbstractModel


def file_path():
    return os.path.join(settings.BASE_DIR, 'files')


class BirthDay(AbstractModel):
    """ BirtDate model class """

    first_name = models.CharField(
        verbose_name='имя',
        max_length=50
    )

    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=50
    )

    middle_name = models.CharField(
        verbose_name='отчество',
        max_length=50
    )

    birth_date = models.DateField(
        verbose_name='день рождения'
    )

    photo = models.ImageField(
        verbose_name='фото',
        upload_to=file_path
    )
