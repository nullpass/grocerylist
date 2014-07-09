# items/models.py

from django.db import models

from core.models import UltraModel

from stores.models import Store

class Item(UltraModel):
    """
    """
    name = models.CharField(max_length=2)
    description = models.TextField(max_length=1024)
    store = models.ForeignKey(Store, related_name='isle')
