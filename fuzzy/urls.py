from django.contrib import admin
from django.urls import path
from fuzzy import views
# from hello import views


urlpatterns = [
    path('fuzzy/', views.AlarmSettingsList.as_view()),
    path('fuzzy/<uuid:pk>/', views.AlarmSettingsDetail.as_view()),
]