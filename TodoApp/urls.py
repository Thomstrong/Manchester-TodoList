from django.conf.urls import url, include
from rest_framework import routers

from TodoApp import views

router = routers.DefaultRouter()
router.register(r'todoList', views.TodoListItem)

urlpatterns = [
    url(r'api/', include(router.urls))
]
