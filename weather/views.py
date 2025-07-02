from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .weather_api import get_weather

def dashboard(request):
    
    return render(request, "dashboard.html")

from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .weather_api import get_weather
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def weather_api_view(request):
    city = request.user.location or "Hyderabad"
    # city = getattr(request.user, "location", None) or "Hyderabad"

    data = get_weather(city)
    
    return JsonResponse({
        "location": city,
        "temperature": data.get("main", {}).get("temp"),
        "description": data.get("weather", [{}])[0].get("description"),
        "icon": data.get("weather", [{}])[0].get("icon")
    })


