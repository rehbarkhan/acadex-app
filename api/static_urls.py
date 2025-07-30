from django.urls import path, re_path
from . import static_view

urlpatterns = [
    path('', getattr(static_view, 'Login').as_view(), name='login'),
    re_path(r'hr', getattr(static_view, "HrView").as_view(), name='hr-view')
]