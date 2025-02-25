from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Family, Task
from .serializers import FamilySerializer, TaskSerializer
from .filters import TaskFilter

class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['state', 'family']
    filterset_class = TaskFilter
    ordering_fields = ['state', 'due_date']
    search_fields = ['title']
