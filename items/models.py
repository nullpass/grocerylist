# items/models.py

from django.db import models

from core.models import UltraModel

from stores.models import Store
from isles.models import Isle

class Item(UltraModel):
    """
    """
    name = models.CharField(max_length=2)
    description = models.TextField(max_length=1024)
    store = models.ForeignKey(Store, related_name='item')
    isle = models.ForeignKey(Isle, related_name='isle')
