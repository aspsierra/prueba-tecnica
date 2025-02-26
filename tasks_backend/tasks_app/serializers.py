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
    family = FamilySerializer()
    class Meta:
        model = Task
        fields = ['title', 'state', 'due_date', 'family']