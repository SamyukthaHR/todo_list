from rest_framework import serializers

from todo_app.models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'due_date', 'status']