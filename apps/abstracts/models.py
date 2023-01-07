from django.db import models

class AbstractModel(models.Model):
    create_date = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True
    )
    
    create_user = models.CharField(
        verbose_name='кем создан',
        max_length=50
    )

    change_date = models.DateTimeField(
        verbose_name='дата изменения',
        auto_now=True
    )

    change_user = models.CharField(
        verbose_name='кем изменен',
        max_length=50
    )
