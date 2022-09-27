from .serializers import TaskSerializer, ExecutorSerializer
from rest_framework import viewsets, permissions, pagination
from .models import Task, Executor

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 5000

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination