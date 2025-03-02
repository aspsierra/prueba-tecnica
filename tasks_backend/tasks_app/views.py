from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Family, Task
from .serializers import FamilySerializer, TaskReadSerializer, TaskListSerializer, TaskWriteSerializer
from .filters import TaskListFilter, FamilyListFilter
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView


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
@permission_classes([IsAdminOrReadOnly])
def get_task_states(request):
    states = [{'value' : state[0], 'label': state[1]} for state in Task.STATES]
    return Response(states)


class CustomOAuth2Client(OAuth2Client):
    def __init__(self, *args, scope_delimiter=" ", **kwargs):
        super().__init__(*args, **kwargs)
        self.scope_delimiter = scope_delimiter



class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = 'http://localhost:5173/github/callback/'
    client_class = CustomOAuth2Client
    # def get_client(self, request):
    #     return OAuth2Client(request) 


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = CustomOAuth2Client
    callback_url = 'http://localhost:5173/google/callback/'

    # def get_scope(self, request):
    #     print("DEBUG: get_scope() recibió estos argumentos:", request)
    #     return super().get_scope(request)
