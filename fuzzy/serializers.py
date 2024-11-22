from rest_framework import serializers
from fuzzy.models import AlarmSettings

class AlarmSerializer(serializers.ModelSerializer):
    def get_sleep_quality_data(self):
        return {
            'stress_level': self.data['stress_level'],
            'bed_quality': self.data['bed_quality'],
            'ambient_noise': self.data['ambient_noise'],
        }

    def get_weather_data(self):
        return {
            'wind_speed': self.data['wind_speed'],
            'temperature': self.data['temperature'],
            'humidity': self.data['humidity'],
        }

    def get_fatigue_level_data(self):
        return {
            'last_night_sleep': self.data['last_night_sleep'],
            'sleep_debt': self.data['sleep_debt'],
        }

    def get_schedule_importance_data(self):
        return {
            'meetings': self.data['meetings'],
            'urgent_tasks': self.data['urgent_tasks'],
        }

    def get_mood_data(self):
        pass

    class Meta:
        model = AlarmSettings
        fields = '__all__'