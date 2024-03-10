from django.urls import path
from . import views

urlpatterns = [
    path('', views.weekdays_all, name='weekdays_all'),
    path('<str:lang>/', views.weekdays_lang, name='weekdays_lang'),
]
