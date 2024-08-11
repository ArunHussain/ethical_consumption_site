from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#custom user model for taking emails too
class CustomUser(AbstractUser):
    user_email=models.CharField(max_length=30, blank=True)
