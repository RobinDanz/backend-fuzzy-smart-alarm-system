from django.db import models

# Create your models here.

class Alarm_Settings(models.Model):
    message = models.CharField(max_length=20000)
    
    
    def __str__(self):
        return self.message
