from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    h1 = models.CharField(max_length=200)