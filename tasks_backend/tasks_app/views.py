from rest_framework import viewsets, filters
from .models import Family, Task
from .serializers import FamilySerializer, TaskSerializer

class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['state', 'due_date']
    search_fields = ['title', 'description']
