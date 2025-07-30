from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        groups = ['admin', 'hr']
        [Group.objects.get_or_create(name = x) for x in groups]
        permissions = Permission.objects.all()
        admin_group = Group.objects.get(name='admin')
        for permission in permissions:
            admin_group.permissions.add(permission)