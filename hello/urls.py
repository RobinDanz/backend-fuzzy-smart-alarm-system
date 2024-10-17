from django.contrib import admin
from django.urls import path
from hello import views
from .views import set_alarm_values


urlpatterns = [
    path('', views.HelloWorldView.as_view()),
    path('alarm/',set_alarm_values,name='set_alarm_values'),
]