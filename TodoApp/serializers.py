from rest_framework import serializers
from TodoApp.models import TodoListItem


class TodoListItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoListItem
        fields = ('id', 'description', 'deadline', 'priority', 'status', 'url',)
