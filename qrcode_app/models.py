from django.db import models
from django.contrib.auth.models import User

class QRCode(models.Model):
    data = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
