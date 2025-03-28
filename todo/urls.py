from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.parent_list.as_view(), name='view'),
    path("create/",
         views.create_todo,
         name='create_todo'),
    path("update/<int:task_id>/",
         views.update_todo,
         name="update_todo"),
    path("detail/<int:task_id>/",
         views.task_detail,
         name="task_detail"),
    path("delete/<int:task_id>/",
         views.task_delete,
         name="task_delete"),
     path("accounts/", include("allauth.urls")),
     path("welcome/", views.welcome, name="welcome"),
]
