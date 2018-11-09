# -*- coding: utf-8 -*-

from django.db import models

STATUS = (
    (0, u'待完成'),
    (1, u'已完成'),
    (2, u'已放弃')
)


class TodoListItem(models.Model):
    id = models.CharField(primary_key=True, blank=True, max_length=255)
    description = models.CharField(blank=False, max_length=255)
    priority = models.IntegerField()
    deadline = models.DateTimeField()
    #测试
    status = models.IntegerField(choices=STATUS, default=0)



