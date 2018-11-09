# coding=utf-8
import uuid
from datetime import datetime

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
        delta = instance.deadline - datetime.now()
        days, hours, minute = delta.days, delta.seconds // 3600, (delta.seconds // 60) % 60

        if days < 0:
            hours = 23 - hours
            minute = 60 - minute
        if minute == 60:
            hours += 1
        if hours == 24:
            days += 1

        reStr = u" %d 天 %d 小时 %d 分钟"
        if days >= 0:
            reStr = u"还剩" + reStr % (days, hours, minute + 1)
        else:
            reStr = u"逾期" + reStr % (-days, hours, minute - 1)
        return reStr




    #sadsad aas dsa
