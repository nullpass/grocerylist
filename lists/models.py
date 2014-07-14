# lists/models.py
from __future__ import absolute_import

from django.db import models
from django.core.urlresolvers import reverse

from core.models import UltraModel

from items.models import Item
from stores.models import Store

class List(UltraModel):
    """
    name of list
    created date [um]
    M2M pointing to items
    
    """
    name = models.CharField(max_length=64)
    store = models.ForeignKey(Store, related_name='list')
    items = models.ManyToManyField(Item, related_name='list')

    def get_absolute_url(self):
        return reverse('lists:detail', kwargs={'pk' : self.pk})
