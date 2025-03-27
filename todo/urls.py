from django.urls import path, include
from . import views

urlpatterns = [
    path("create/",
         views.create_todo,
         name='create_todo'),
]
