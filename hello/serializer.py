from rest_framework import serializers
from .models import Alarm_Settings,Static_Settings

class AlarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm_Settings
        fields = '__all__'
        
class StaticSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Static_Settings
        fields = '__all__'