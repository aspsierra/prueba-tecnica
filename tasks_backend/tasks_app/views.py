from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Family, Task
from .serializers import FamilySerializer, TaskReadSerializer, TaskListSerializer, TaskWriteSerializer
from .filters import TaskListFilter, FamilyListFilter
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_class = FamilyListFilter
    ordering_fields = ['name']
    permission_classes=[IsAdminOrReadOnly]


class TaskListViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_class = TaskListFilter
    ordering_fields = ['state', 'due_date']
    permission_classes=[IsAdminOrReadOnly]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes=[IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TaskReadSerializer
        return TaskWriteSerializer
    
    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         return [] 
    #     return [IsAdminOrReadOnly] 
    
    @action(detail=True, methods=['put'], url_path='update')
    def update_task(self, request, pk=None):
        task = self.get_object()
        serializer = TaskWriteSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'], url_path='delete')
    def delete_task(self, request, pk=None):
        task = self.get_object()
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['post'], url_path='create-task')
    def create_task(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_task_states(request):
    states = [{'value' : state[0], 'label': state[1]} for state in Task.STATES]
    return Response(states)

