from __future__ import absolute_import

from django.urls import path

from shigoto_q.tasks import views

app_name = "tasks"

urlpatterns = [
    path(
        "task/create/",
        views.TaskCreateView.as_view(),
        name="shigoto_q.tasks.task.create"
    ),
    path(
        "tasks/list/",
        views.UserTaskListView.as_view(),
        name="shigoto_q.tasks.tasks.list",
    ),
    path(
        "task/run/",
        views.TaskRunView.as_view(),
        name="shigoto_q.tasks.task.run",
    ),
]
