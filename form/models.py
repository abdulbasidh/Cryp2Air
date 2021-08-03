from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.
class Form(models.Model):
    username = models.CharField(max_length=60)
