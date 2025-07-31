from django.db import models
from django.conf import settings

class MainModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if getattr(settings, "READ_ONLY", False) :
            raise Exception("Database is in read-only-mode.")
        return super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if getattr(settings, "READ_ONLY", False):
            raise Exception("Database is in read-only-mode.")
        return super().delete(*args, **kwargs)