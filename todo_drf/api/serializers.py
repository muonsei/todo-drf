from rest_framework import serializers
from .models import Task

# Similar syntax to a ModelForm
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"