# Python modules
from typing import Any
# Django modules
from django.contrib import admin
# Project modules
from .models import BirthDay


class BirthDayAdmin(admin.ModelAdmin):
    model = BirthDay

    list_display = (
        'first_name',
        'last_name',
        'middle_name',
        'birth_date'
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



admin.site.register(BirthDay, BirthDayAdmin)
