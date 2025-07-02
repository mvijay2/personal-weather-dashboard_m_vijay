from django.urls import path
from .views import dashboard, weather_api_view, home

from .views import dashboard, weather_api_view

urlpatterns = [
    path("dashboard/", dashboard, name="weather_dashboard"),  # returns HTML
    path("api/weather/", weather_api_view, name="weather_api_dashboard"),  # returns JSON 🔥
    path("", home, name="home"),  # returns HTML

]