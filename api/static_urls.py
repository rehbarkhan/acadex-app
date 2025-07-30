from django.urls import path
from . import static_view

urlpatterns = [
    path('', getattr(static_view, 'Login').as_view(), name='login'),
]