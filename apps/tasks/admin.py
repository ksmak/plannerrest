
# Python modules
from typing import Any
# Django modules
from django.contrib import admin
# Project modules
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = (
        'state',
        'title',
        'description',
        'is_all_day',
        'start_date',
        'end_date'
    )

    readonly_fields = (
        'create_date',
        'create_user',
        'change_date',
        'change_user'
    )

    def save_model(
        self,
        request: Any,
        obj: Any,
        form: Any,
        change: Any
    ) -> None:

        if change:
            obj.change_user = request.user
        else:
            obj.create_user = request.user

        obj.save()
