from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Family, Task
from .serializers import FamilySerializer, TaskSerializer, TaskListSerializer
from .filters import TaskListFilter, FamilyListFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response

class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_class = FamilyListFilter
    ordering_fields = ['name']


class TaskListViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_class = TaskListFilter
    ordering_fields = ['state', 'due_date']

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@api_view(['GET'])
def get_task_states(request):
    states = [{'value' : state[0], 'label': state[1]} for state in Task.STATES]
    return Response(states)

