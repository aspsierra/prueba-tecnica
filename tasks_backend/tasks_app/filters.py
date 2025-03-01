import django_filters
from .models import Task, Family

class TaskListFilter(django_filters.FilterSet):
    family = django_filters.NumberFilter(field_name="family__id")
    title = django_filters.CharFilter(field_name="title", lookup_expr='icontains')
    due_date = django_filters.DateFromToRangeFilter()
    state = django_filters.MultipleChoiceFilter(choices=Task.STATES)

    class Meta:
        model= Task
        fields = ['family', 'title', 'due_date', 'state']
            
class FamilyListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')
    id = django_filters.NumberFilter(field_name="id", lookup_expr='exact')

    class Meta:
        model= Family
        fields = ['name', 'id']
            
        