from django.db import models

# Create your models here.
class Event(models.Model):
    event_name =models.CharField(max_length=30)
    event_description=models.TextField()
    venue =models.CharField(max_length=30)
    event_date=models.DateTimeField()
    attendees =models.EmailField()
