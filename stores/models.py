# stores/models.py

from django.db import models

from core.models import UltraModel

class Store(UltraModel):
    """
    
    """
    name = models.CharField(max_length=64)
    address = models.TextField(max_length=1024)
    