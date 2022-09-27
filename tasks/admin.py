from django.contrib import admin
from .models import Task, File, Executor, PerfomanceInfo

admin.site.register(Task)
admin.site.register(File)
admin.site.register(Executor)
admin.site.register(PerfomanceInfo)
