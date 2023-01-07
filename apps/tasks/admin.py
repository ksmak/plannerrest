from django.contrib import admin
from .models import Task, File, PerfomanceInfo

admin.site.register(Task)
admin.site.register(File)
admin.site.register(PerfomanceInfo)
