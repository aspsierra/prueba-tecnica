from rest_framework import serializers
from .models import Family, Task

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields= '__all__'


class TaskSerializer(serializers.ModelSerializer):
    family = FamilySerializer()
    class Meta:
        model = Task
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    state_display = serializers.CharField(source="get_state_display")
    family = FamilySerializer()
    class Meta:
        model = Task
        fields = ['id', 'title', 'state', 'state_display', 'due_date', 'family']