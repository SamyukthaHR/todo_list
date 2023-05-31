from django.urls import path

from todo_app import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("tasks", views.TaskListView.as_view(), name="tasks"),
    path("tasks/<int:id>/<int:func>", views.SingleTaskView.as_view(), name="task"),
    path("form/<int:id>", views.TaskFormView.as_view(), name="forms"),
    path("form", views.AddTaskFormView.as_view(), name="add_form")
]
