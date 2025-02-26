import django_filters
from .models import Task

class TaskListFilter(django_filters.FilterSet):
    class Meta:
        model= Task
        fields = {
            'due_date': ['gte', 'lte']
        }