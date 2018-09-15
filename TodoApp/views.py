# -*- coding: utf-8 -*-
import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response

from TodoApp.models import TodoListItem
from TodoApp.serializers import TodoListItemSerializer


class TodoListItem(viewsets.ModelViewSet):
    serializer_class = TodoListItemSerializer
    queryset = TodoListItem.objects.all()

    def create(self, request, *args, **kwargs):
        request.DATA['id'] = str(uuid.uuid4())
        serializer = self.get_serializer(data=request.DATA, files=request.FILES)

        if serializer.is_valid():
            self.pre_save(serializer.object)
            self.object = serializer.save(force_insert=True)
            self.post_save(self.object, created=True)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
