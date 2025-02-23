from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hero", views.hero, name="hero"),
    path("main", views.main, name="main"),
    path("create/list", views.create_list_form, name="create_list_form"),
    path("tasks/<int:list_num>", views.new_tasks, name="tasks"),
    path("tasks/<int:list_num>/new_tasks", views.new_tasks, name="new_task"),
    path("update-task/<int:task_id>/", views.update_task_status, name="update_task_status"),
    # path("update-name/<int:task_id>/<str:updated_name>", views.update_task_name, name="update_task_name"),
    path("edit_task/<int:task_id>", views.edit_task, name="edit_task"),
    path("cancel_task/<int:task_id>", views.cancel_task, name="cancel_task"),
    path("save_task/<int:task_id>", views.save_task, name="save_task"),
    path("delete-task/<int:task_id>/", views.delete_task, name="delete_task"),
]