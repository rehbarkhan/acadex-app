from django.db import models
from django.utils import timezone

class AgedoutModel(models.Model):
    is_agedout = models.BooleanField(default=False)
    agedout_timestamp = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
    
    def delete(self, force = False, *args, **kwargs):
        if force:
            return super().delete(*args, **kwargs)
        self.is_agedout = True
        self.agedout_timestamp = timezone.now()
        return self.save(*args, **kwargs)
