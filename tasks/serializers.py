from rest_framework import serializers
from .models import Task, File, Executor, PerfomanceInfo

class FileSerializer(serializers.ModelSerializer):
   class Meta:
      model = File
      fields = ['id', 'task_id', 'name', 'file']

class PerfomanceInfoSerializer(serializers.ModelSerializer):
   class Meta:
      model = PerfomanceInfo
      fields = ['id', 'task_id', 'executor_id', 'execute_date', 'comment']

class ExecutorSerializer(serializers.ModelSerializer):
   class Meta:
      model = Executor
      fields = ['id', 'department', 'management', 'job', 'firstname', 'middlename', 'lastname']

class TaskSerializer(serializers.ModelSerializer):
   files = FileSerializer(many=True, read_only=True)
   perfomance_info = PerfomanceInfoSerializer(many=True, read_only=True)
   class Meta:
      model = Task
      fields = ['id', 'state', 'name', 'description', 'start_date', 'end_date', \
         'repeat_type', 'repeat_over', 'repeat_in_days', 'repeat_in_months'
         'files', 'perfomance_info']
