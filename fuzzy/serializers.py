from rest_framework import serializers
from fuzzy.models import AlarmSettings, FuzzyOuput


class FuzzyOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuzzyOuput
        fields = '__all__'


class AlarmSettingsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')

        if fields:
            fields = fields.split(',')
            allowed = set(fields)
            existing = set(self.fields.keys())

            for field_name in existing-allowed:
                self.fields.pop(field_name)

    fuzzy_outputs = FuzzyOutputSerializer(many=True, read_only=True)

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
        extra_kwargs = {
            'user_id': {  'read_only': True },
            'sleep_debt': {'read_only': True},
            'fuzzy_outputs': {  'read_only': True }
        }