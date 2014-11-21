# items/models.py

from django.db import models
from django.contrib.auth.models import User

from core.models import UltraModel

from stores.models import Store
from isles.models import Isle

class Item(UltraModel):
    """    """
    name  = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    #
    user  = models.ForeignKey(User,  related_name='item')
    store = models.ForeignKey(Store, related_name='item')
    #
    # v4 refactor, remove, items now stored in Isle
    isle  = models.ForeignKey(Isle,  related_name='item')

    class Meta:
        unique_together = (("store", "name"),)
