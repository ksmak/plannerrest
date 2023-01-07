# Python modules
import os
# Django modules
from django.db import models
# Project modules
from django.conf import settings
from abstracts.models import AbstractModel
from auths.models import CustomUser

def file_path():
    return os.path.join(settings.BASE_DIR, 'files')


class Task(AbstractModel):
    STATE_NEW = 0
    STATE_PROCESS = 1
    STATE_DONE = 2
    
    STATES = [
        (STATE_NEW, 'Новое задание'),
        (STATE_PROCESS, 'На исполнении'),
        (STATE_DONE, 'Исполнено'),
    ]
    
    NO_REPEAT = 0
    REPEAT_DAY = 1
    REPEAT_WEEK = 2
    REPEAT_MONTH = 3
    REPEAT_YEAR = 4
    
    REPEATES = [
        (NO_REPEAT, 'Не повторять'),
        (REPEAT_DAY, 'Ежедневно'),
        (REPEAT_WEEK, 'Еженедельно'),
        (REPEAT_MONTH, 'Ежемесячно'),
        (REPEAT_YEAR, 'Ежегодно'),
    ]

    state = models.SmallIntegerField(
        verbose_name='состояние',
        choices=STATES,
        default=STATE_NEW
    )

    title = models.CharField(
        verbose_name='наименование',
        max_length=50
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True,
        null=True
    )
    
    is_all_day = models.BooleanField(
        verbose_name='на целый день',
        default=False
    )

    start_date = models.DateTimeField(
        verbose_name='дата начало',
        blank=True,
        null=True
    )
    
    end_date = models.DateTimeField(
        verbose_name='дата конец',
        blank=True,
        null=True
    )

    repeat_type = models.SmallIntegerField(
        verbose_name='повторять',
        choices=REPEATES,
    )

    class Meta:
        verbose_name = 'задание'
        verbose_name_plural = 'задания'
        ordering = ['-change_date']


class RepeatOver(models.Model):
    task = models.ForeignKey(
        to='Task',
        on_delete=models.CASCADE,
        related_name='repeat_over'
    )

    repeat = models.SmallIntegerField(
        verbose_name='повторять'
    )

    class Meta:
        verbose_name = 'повторение'
        verbose_name_plural = 'повторения'


class File(models.Model):
    task = models.ForeignKey(
        to='Task',
        on_delete=models.CASCADE,
        verbose_name='задание'
    )
    
    name = models.CharField(
        verbose_name='наименование',
        max_length=50
    )
    
    file = models.FilePathField(
        path=file_path
    )

    class Meta:
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'


class PerfomanceInfo(models.Model):
    task = models.ForeignKey(
        to='Task',
        on_delete=models.CASCADE,
        verbose_name='задание'
    )

    executor = models.ForeignKey(
        to=CustomUser,
        on_delete=models.RESTRICT,
        verbose_name='исполнитель'
    )

    execute_date = models.DateTimeField(
        verbose_name='дата исполнения',
        blank=True,
        null=True
    )

    comment = models.TextField(
        verbose_name='Примечание',
        max_length=500,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'сведение об исполнении'
        verbose_name_plural = 'сведения об исполнении'