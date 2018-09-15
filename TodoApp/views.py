# -*- coding: utf-8 -*-
import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response

from TodoApp.models import TodoListItem
from TodoApp.serializers import TodoListItemSerializer


class TodoListItem(viewsets.ModelViewSet):
    serializer_class = TodoListItemSerializer
    queryset = TodoListItem.objects.all()