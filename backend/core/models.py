from django.db import models
from django.utils import timezone


class Promotion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="promotion")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    @property
    def is_active(self):
        now = timezone.now()
        return (now >= self.start_date) and (now <= self.end_date)
    
    def __str__(self):
        return self.title