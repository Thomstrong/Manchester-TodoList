import uuid
from datetime import datetime

import pytz
from rest_framework import serializers

from TodoApp.models import TodoListItem


class TodoListItemSerializer(serializers.HyperlinkedModelSerializer):
    restTime = serializers.SerializerMethodField("getRestTime")

    class Meta:
        model = TodoListItem
        fields = ('id', 'description', 'deadline', 'restTime', 'priority', 'status', 'url',)

    def save(self, *args, **kwargs):
        if not self.object.id:
            self.object.id = str(uuid.uuid4())
        super(TodoListItem, self.object).save(*args, **kwargs)

    def getRestTime(self, instance):
        return instance.deadline - datetime.now(tz=pytz.timezone('Asia/Shanghai'))
