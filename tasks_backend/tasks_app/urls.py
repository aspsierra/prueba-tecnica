from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import FamilyViewSet, TaskViewSet, TaskListViewSet, get_task_states

router = DefaultRouter()
router.register(r'families', FamilyViewSet, basename='families')
router.register(r'tasks-list', TaskListViewSet, basename='tasks-list')
router.register(r'task-detail', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('task-states/', get_task_states, name='task-states'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/github/", include("allauth.socialaccount.urls")),
]