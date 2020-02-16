from django.urls import path

from .views import view

urlpatterns = [
    path('', view.WeatherView.as_view(), name='index'),
]
