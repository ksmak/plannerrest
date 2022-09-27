import os
from django.db import models
from django.conf import settings

def file_path():
    return os.path.join(settings.BASE_DIR, 'files')

class Task(models.Model):
    STATES = [
        (1, 'Новое задание'),
        (2, 'На исполнении'),
        (3, 'Исполнено'),
    ]
    REPEAT_TYPES = [
        (1, 'Ежедневно'),
        (2, 'Еженедельно'),
        (3, 'Ежемесячно'),
        (4, 'Ежегодно'),
    ]
    state = models.BigIntegerField('Статус', choices=STATES, default=1)
    name = models.CharField('Наименование', max_length=100)
    description = models.CharField('Краткое описание', max_length=500, blank=True, null=True)
    start_date = models.DateTimeField('Дата начало', blank=True, null=True)
    end_date = models.DateTimeField('Дата конец', blank=True, null=True)
    repeat_type = models.BigIntegerField('Повторять', choices=REPEAT_TYPES, blank=True, null=True)
    repeat_over = models.IntegerField('Повторять каждые', default=1)
    repeat_in_days = models.CharField('Повторять в (дни)', max_length=500, blank=True, null=True)
    repeat_in_months = models.CharField('Повторять в (месяцы)', max_length=500, blank=True, null=True)
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)
    create_author = models.CharField('Автор создания', max_length=50, blank=True, null=True)
    change_date = models.DateTimeField('Дата изменения', auto_now=True, blank=True, null=True)
    change_author = models.CharField('Автор изменения', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'задание'
        verbose_name_plural = 'задания'
        ordering = ['-change_date']

class Executor(models.Model):
    department = models.CharField('Организация', max_length=150, blank=True, null=True)
    management = models.CharField('Подразделение', max_length=150, blank=True, null=True)
    job = models.CharField('Должность', max_length=150, blank=True, null=True)
    firstname = models.CharField('Фамилия', max_length=50)
    middlename = models.CharField('Имя', max_length=50, blank=True, null=True)
    lastname = models.CharField('Отчество', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'исполнитель'
        verbose_name_plural = 'исполнители'
        ordering = ['firstname', 'middlename', 'lastname']
        
class File(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задание')
    name = models.CharField('Наименование', max_length=50)
    file = models.FilePathField(path=file_path)

    class Meta:
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'


class PerfomanceInfo(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задание')
    executor = models.ForeignKey(Executor, on_delete=models.DO_NOTHING, verbose_name='Исполнитель')
    execute_date = models.DateTimeField('Дата')
    comment = models.CharField('Примечание', max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'сведение об исполнении'
        verbose_name_plural = 'сведения об исполнении'