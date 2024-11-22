from django.contrib import admin
from django.urls import path
from fuzzy import views
# from hello import views


urlpatterns = [
    path('', views.FuzzyView.as_view()),
    # path('alarm/',set_alarm_values,name='set_alarm_values'),
]