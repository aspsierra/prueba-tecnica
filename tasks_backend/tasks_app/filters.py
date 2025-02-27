import django_filters
from .models import Task

class TaskListFilter(django_filters.FilterSet):
    family = django_filters.NumberFilter(field_name="family__id")

    class Meta:
        model= Task
        fields = ['family']
            
        