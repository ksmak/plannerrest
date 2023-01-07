from rest_framework import serializers
from .models import RepeatOver, Task, File, PerfomanceInfo


class RepeatOverSerializer(serializers.ModelSerializer):
   class Meta:
      model = RepeatOver
      fields = [
         'id',
         'task_id',
         'repeat'
      ]


class FileSerializer(serializers.ModelSerializer):
   class Meta:
      model = File
      fields = [
         'id',
         'task_id',
         'name',
         'file'
      ]


class PerfomanceInfoSerializer(serializers.ModelSerializer):
   class Meta:
      model = PerfomanceInfo
      fields = [
         'id',
         'task_id',
         'executor_id',
         'execute_date',
         'comment'
      ]


class TaskSerializer(serializers.ModelSerializer):
   repeat_over = RepeatOverSerializer(
      many=True,
      read_only=True
   )

   files = FileSerializer(
      many=True,
      read_only=True
   )

   perfomance_info = PerfomanceInfoSerializer(
      many=True,
      read_only=True
   )
   
   class Meta:
      model = Task
      fields = [
         'id',
         'state',
         'title',
         'description',
         'is_all_day',
         'start_date',
         'end_date', 
         'repeat_type',
         'repeat_over',        
         'files',
         'perfomance_info'
      ]
