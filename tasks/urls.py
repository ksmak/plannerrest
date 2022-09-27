from django.urls import path, include
from rest_framework import routers
from . import views, services 

router = routers.DefaultRouter()
router.register('task/', services.TaskViewSet, basename='Task')
router.register('executor/', services.ExecutorViewSet, basename='Executor')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]