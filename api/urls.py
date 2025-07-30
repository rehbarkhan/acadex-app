from rest_framework.routers import DefaultRouter
from api import views
from django.urls import path, re_path


urlpatterns = [
    path('Login/', getattr(views, "Login").as_view(), name='login'),
]