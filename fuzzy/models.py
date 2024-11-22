from django.db import models

class AlarmSettings(models.Model):
    #Sleep Quality Fuzzy Variables
    stress_level = models.IntegerField(null=True)
    bed_quality = models.IntegerField(null=True)
    ambient_noise = models.IntegerField(null=True)

    #Weather Fuzzy Variables
    wind_speed = models.IntegerField(null=True)
    temperature = models.IntegerField(null=True)
    humidity = models.IntegerField(null=True)

    #Fatigue Level Fuzzy Variables
    last_night_sleep = models.IntegerField(null=True)
    sleep_debt = models.IntegerField(null=True)

    #Schedule Importance Fuzzy Variables
    meetings = models.IntegerField(null=True)
    urgent_tasks = models.IntegerField(null=True)

    #General variables
    user_age = models.IntegerField(null=True)
    preffered_wake_method = models.IntegerField(null=True)

    #Mood Fuzzy Variables
    physical_well_being = models.IntegerField(null=True)
    
    def __str__(self):
        return self.message
    

class AlarmSettings_old(models.Model):
    """
    Old model
    """
    sleep_quality = models.IntegerField(null=True)
    schedule_importance = models.IntegerField(null=True)
    mood = models.IntegerField(null=True)
    weather = models.IntegerField(null=True)
    preferred_wake_method = models.IntegerField(null=True)

    abstract = True
