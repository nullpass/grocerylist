# items/models.py

from django.db import models

from core.models import UltraModel

from stores.models import Store
from isles.models import Isle

class Item(UltraModel):
    """
    """
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    store = models.ForeignKey(Store, related_name='item')
    isle = models.ForeignKey(Isle, related_name='isle')
    selected = models.BooleanField(default=False)
