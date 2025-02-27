from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FamilyViewSet, TaskViewSet, TaskListViewSet, get_task_states

router = DefaultRouter()
router.register(r'families', FamilyViewSet, basename='families')
router.register(r'tasks-list', TaskListViewSet, basename='tasks-list')
router.register(r'task/<int:id>', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('task-states/', get_task_states, name='task-states')
]