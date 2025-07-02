from django.db import models

# Create your models here.
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
# from django.contrib.auth.models import User
from .managers import CustomUserManager

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
#from django.utils.translation import ugettext_lazy as _
# from django_countries.fields import CountryField


    
######################################################

class CustomUser(AbstractUser, PermissionsMixin):
    #username=None
    email=models.EmailField(('email address'), unique=True)
    username = models.CharField(max_length=150, blank=True, null=True, unique=True)
    country = models.CharField(max_length=150, blank=True, null=True, unique=True)
    location = models.CharField(max_length=100, blank=True, null=True)  # 👈 Add this line
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()
    def __str__(self):
        return self.email
