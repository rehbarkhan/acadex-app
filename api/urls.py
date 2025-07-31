from rest_framework.routers import DefaultRouter
from api import views
from django.urls import path, re_path, include
from django.apps import apps


router = DefaultRouter()

for model in apps.get_app_config('api').get_models():
    name = model._meta.object_name
    router.register(
        r'{}'.format(name),
        getattr(views, '{}'.format(name)),
        basename='{}'.format(name)
    )


urlpatterns = [
    path('Login/', getattr(views, "Login").as_view(), name='login'),
    path('', include(router.urls)),
]