from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    is_premium = models.BooleanField(default=False)
    limit_date = models.DateField(blank=True, null=True)
    limit_requests = models.PositiveIntegerField(default=3, blank=True, null=True)
    requests = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.email