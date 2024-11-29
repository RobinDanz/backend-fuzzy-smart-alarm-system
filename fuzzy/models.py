from django.db import models
import uuid
from fuzzy.fuzzy_systems import (
    sleep_quality_fuzz, 
    fatigue_level_fuzz, 
    weather_fuzz, 
    schedule_importance_fuzz, 
    global_system
)

class AlarmSettings(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
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
    
    timestamp = models.DateTimeField(auto_now_add=True)

    def static_settings_filled(self):
        ret = self.user_age is not None and self.preffered_wake_method is not None and self.bed_quality is not None and self.ambient_noise is not None
        
        return ret
    
    def dynamic_settings_filled(self):
        ret =  self.stress_level is not None and \
        self.wind_speed is not None and \
        self.temperature is not None and \
        self.humidity is not None and \
        self.last_night_sleep is not None and \
        self.sleep_debt is not None and \
        self.meetings is not None and \
        self.urgent_tasks is not None and \
        self.physical_well_being is not None

        return ret
            
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

    def save(self, **kwargs) -> None:
        s = super().save(**kwargs)

        if self.static_settings_filled() and self.dynamic_settings_filled():
            sleep_quality_out = sleep_quality_fuzz.process_sleep_quality(self.get_sleep_quality_data())
            weather_out = weather_fuzz.process_weather(self.get_weather_data())
            fatigue_level_out = fatigue_level_fuzz.process_fatigue_level(self.get_fatigue_level_data(), self.user_age)
            schedule_importance_out = schedule_importance_fuzz.process_schedule_importance(self.get_schedule_importance_data())

            # wake_time_adjustment = global_system.set_alarm_settings(self.get_global_fuzzy_data())

            f = FuzzyOuput.objects.create(
                fatigue_level_out=fatigue_level_out, 
                sleep_quality_out=sleep_quality_out, 
                weather_out=weather_out, 
                schedule_importance_out=schedule_importance_out,
                wake_time_adjustment=0,
                alarm_setting=self
            )

            self.fuzzy_outputs.add(f)
        
        return s


class FuzzyOuput(models.Model):
    #Fuzzy systems output
    fatigue_level_out = models.FloatField(null=True)
    schedule_importance_out = models.FloatField(null=True)
    sleep_quality_out = models.FloatField(null=True)
    weather_out = models.FloatField(null=True)
    wake_time_adjustment = models.FloatField(null=True)  
    timestamp = models.DateTimeField(auto_now_add=True)
    alarm_setting = models.ForeignKey(to=AlarmSettings, related_name='fuzzy_outputs', on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']

    def get_fuzzy_variables(self):
        return {
            'sleep_quality': self.sleep_quality_out,
            'schedule_importance': self.schedule_importance_out,
            'mood': 5,
            'weather': self.weather_out,
            'fatigue_level': self.fatigue_level_out
        }
    
    def save(self, **kwargs):
        self.wake_time_adjustment = global_system.set_alarm_settings(self.get_fuzzy_variables())
        return super().save(**kwargs)