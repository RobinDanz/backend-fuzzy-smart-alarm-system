from django.contrib import admin
from django.urls import path
from fuzzy import views
# from hello import views


urlpatterns = [
    path('fuzzy/', views.AlarmSettingsList.as_view()),
    path('fuzzy/<int:pk>/', views.AlarmSettingsDetail.as_view()),
    path('fuzzy/<uuid:user_id>/', views.AlarmSettingsDetail.as_view()),  
]