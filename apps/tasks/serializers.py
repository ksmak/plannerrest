# Project modules
from .models import RepeatOver, Task
# Third part modules
from rest_framework import serializers


class RepeatOverSerializer(serializers.ModelSerializer):
   class Meta:
      model = RepeatOver
      fields = (
         'id',
         'task_id',
         'repeat',
      )


class TaskSerializer(serializers.ModelSerializer):
   repeat_over = RepeatOverSerializer(
      many=True,
      read_only=True
   )

   class Meta:
      model = Task
      fields = (
         'id',
         'state',
         'title',
         'description',
         'is_all_day',
         'start_date',
         'end_date',
         'repeat_type',
         'repeat_over',
      )
