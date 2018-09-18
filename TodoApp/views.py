# -*- coding: utf-8 -*-

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from TodoApp.models import TodoListItem
from TodoApp.serializers import TodoListItemSerializer


class TodoListItem(viewsets.ModelViewSet):
    serializer_class = TodoListItemSerializer
    queryset = TodoListItem.objects.all()

    @action(methods=['post'])
    def SetStatus(self, request, pk):
        instance = self.get_object()
        instance.status = int(request.DATA['status'])
        instance.save()
        return Response({"message": "success"}, status=status.HTTP_200_OK)
