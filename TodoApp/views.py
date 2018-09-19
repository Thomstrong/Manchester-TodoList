# -*- coding: utf-8 -*-
import re

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from TodoApp.models import TodoListItem
from TodoApp.serializers import TodoListItemSerializer


class TodoListItem(viewsets.ModelViewSet):
    serializer_class = TodoListItemSerializer
    queryset = TodoListItem.objects.all()

    def get_queryset(self):
        try:
            m = re.match("(-?)(.*)", self.request.QUERY_PARAMS["sorting"])
            if m.group(1) == '-':
                return self.queryset.order_by(m.group(2), ).reverse()
            else:
                return self.queryset.order_by(m.group(0), )
        except Exception as e:
            return self.queryset

    @action(methods=['post'])
    def SetStatus(self, request, pk):
        instance = self.get_object()
        instance.status = int(request.DATA['status'])
        instance.save()
        return Response({"message": "success"}, status=status.HTTP_200_OK)
