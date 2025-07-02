from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import EmailTokenObtainPairSerializer

class EmailLoginView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer

from django.shortcuts import render

def login_page(request):
    return render(request, "login.html")


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser


def register(request):
    return render(request, "register.html")


@api_view(["POST"])
def register_user(request):
    email = request.data.get("email")
    password = request.data.get("password")
    location = request.data.get("location", "Hyderabad")  # fallback default

    if not email or not password:
        return Response("Missing email or password", status=400)

    if CustomUser.objects.filter(email=email).exists():
        return Response("Email already registered", status=400)

    user = CustomUser.objects.create_user(
        email=email,
        password=password,
        location=location
    )
    user.is_active = True
    user.save()

    return Response("User registered successfully")

