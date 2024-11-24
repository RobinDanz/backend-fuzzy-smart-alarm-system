from typing import Iterable
from django.db import models
import uuid
from datetime import datetime
from fuzzy.fuzzy_systems import (
    sleep_quality_fuzz, 
    fatigue_level_fuzz, 
    weather_fuzz, 
    schedule_importance_fuzz, 
    global_system
)

class AlarmSettings(models.Model):
    stress_level = models.IntegerField(null=True)
    wind_speed = models.IntegerField(null=True)
    temperature = models.IntegerField(null=True)
    humidity = models.IntegerField(null=True)
    last_night_sleep = models.IntegerField(null=True)
    sleep_debt = models.IntegerField(null=True)
    meetings = models.IntegerField(null=True)
    urgent_tasks = models.IntegerField(null=True)
    physical_well_being = models.IntegerField(null=True)

    #Static settings
    user_age = models.IntegerField(null=True)
    preffered_wake_method = models.IntegerField(null=True)
    bed_quality = models.IntegerField(null=True)
    ambient_noise = models.IntegerField(null=True)

    user_id = models.UUIDField(default=uuid.uuid4, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    #Fuzzy systems output
    fatigue_level_out = models.FloatField(null=True)
    schedule_importance_out = models.FloatField(null=True)
    sleep_quality_out = models.FloatField(null=True)
    weather_out = models.FloatField(null=True)
    wake_time_adjustment = models.FloatField(null=True)    

    def get_sleep_quality_data(self):
        return {
            'stress_level': self.stress_level,
            'bed_quality': self.bed_quality,
            'ambient_noise': self.ambient_noise,
        }
    
    def get_fatigue_level_data(self):
        return {
            'last_night_sleep': self.last_night_sleep,
            'sleep_debt': self.sleep_debt,
        }
    
    def get_weather_data(self):
        return {
            'wind_speed': self.wind_speed,
            'temperature': self.temperature,
            'humidity': self.humidity,
        }
    
    def get_schedule_importance_data(self):
        return {
            'meeting_time': self.meetings,
            'urgent_tasks': self.urgent_tasks,
        }
    
    def get_global_fuzzy_data(self):
        return {
            'sleep_quality': self.sleep_quality_out,
            'schedule_importance': self.schedule_importance_out,
            'mood': 5, #TODO
            'weather': self.weather_out,
            'preferred_wake_method': 2, #TODO
        }

    def save(self, **kwargs) -> None:
        self.sleep_quality_out = sleep_quality_fuzz.process_sleep_quality(self.get_sleep_quality_data())
        self.weather_out = weather_fuzz.process_weather(self.get_weather_data())
        self.fatigue_level_out = fatigue_level_fuzz.process_fatigue_level(self.get_fatigue_level_data())
        self.schedule_importance_out = schedule_importance_fuzz.process_schedule_importance(self.get_schedule_importance_data())
        
        self.wake_time_adjustment = global_system.set_alarm_settings(self.get_global_fuzzy_data())
        
        return super().save(**kwargs)
