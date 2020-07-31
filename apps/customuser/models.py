from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    location = models.CharField(max_length=60, blank=True)
    birth_date = models.DateField(null=True, blank=True)
