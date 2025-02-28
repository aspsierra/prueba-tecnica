from datetime import date
from rest_framework import serializers
from .models import Family, Task

class FamilySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Family
        fields= '__all__'


class TaskReadSerializer(serializers.ModelSerializer):
    family = FamilySerializer()
    state_full = serializers.SerializerMethodField()
   
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('creation_date',)

    def get_state_full(self, obj):
        return {'value': obj.state, 'display': obj.get_state_display()}

    
class TaskWriteSerializer(serializers.ModelSerializer):
    # family = serializers.PrimaryKeyRelatedField(queryset=Family.objects.all())
    family = FamilySerializer()
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('creation_date',)

    def validate_due_date(self, value):
        if value and value < date.today():
            raise serializers.ValidationError("La fecha de vencimiento no puede ser anterior a la actual")
        return value
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    

class TaskListSerializer(serializers.ModelSerializer):
    state_display = serializers.CharField(source="get_state_display")
    family = FamilySerializer()
   
    class Meta:
        model = Task
        fields = ['id', 'title', 'state', 'state_display', 'due_date', 'family']