from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FamilyViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'families', FamilyViewSet, basename='families')
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls))
]