from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="todo/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),  # Signup view
    path('', views.welcome_page, name='welcome_page'),  # Welcome page
    path('create/', views.create_todo, name='create_todo'),  # Create todo
]

