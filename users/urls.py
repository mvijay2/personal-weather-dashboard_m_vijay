from django.urls import path
from django.views.generic import TemplateView

# urlpatterns = [
#     path('login/', TemplateView.as_view(template_name="login.html")),
#     # path('', TemplateView.as_view(template_name="dashboard.html")),
# ]

from .views import EmailLoginView, login_page,register_user, register
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('api/users/login/', EmailLoginView.as_view(), name='email_login'),
    path('login/', login_page, name="login"),  # ✅ This serves login.html via GET
    path('api/users/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/register/", register_user, name="user_register"),
    path("register/", register, name="register")    


]


