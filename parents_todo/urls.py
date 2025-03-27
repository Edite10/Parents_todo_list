"""
URL configuration for parents_todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todo import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
    path('home', views.home, name='home'),
    path("admin/", admin.site.urls),
    path('welcome-page/', views.welcome_page, name='welcome_page'),  # Welcome page
    path('sign-in/', views.sign_in, name='sign_in'),    # Sign In page
    path('register/', views.register, name='register'), # Register page

    path("todo", include("todo.urls"), name="todo"),   # Include todo app's URLs
    path('templates/', include('django.contrib.auth.urls')),

]
