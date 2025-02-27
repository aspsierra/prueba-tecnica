from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Family, Task
from .serializers import FamilySerializer, TaskSerializer, TaskListSerializer
from .filters import TaskListFilter

class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class TaskListViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['state']
    filterset_class = TaskListFilter
    ordering_fields = ['state', 'due_date']
    search_fields = ['title']

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
