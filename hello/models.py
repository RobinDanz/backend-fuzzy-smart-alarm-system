from django.db import models

# Create your models here.

class Alarm_Settings(models.Model):
    sleep_quality = models.IntegerField(null=True)
    schedule_importance = models.IntegerField(null=True)
    mood = models.IntegerField(null=True)
    weather = models.IntegerField(null=True)
    preferred_wake_method = models.IntegerField(null=True)
    
    def __str__(self):
        return self.message
